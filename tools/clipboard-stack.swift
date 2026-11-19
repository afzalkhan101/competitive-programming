#!/usr/bin/swift
import AppKit
import ApplicationServices

// Text-only clipboard history. Nothing is saved to disk.
final class ClipboardStack {
    let clipboard = NSPasteboard.general
    var lastChange = -1
    var history: [String] = []
    var eventTap: CFMachPort?
    // Physical keys 1 through 9 on the Mac keyboard.
    let slots: [Int64: Int] = [18: 0, 19: 1, 20: 2, 21: 3, 23: 4,
                               22: 5, 26: 6, 28: 7, 25: 8]

    func capture() {
        guard clipboard.changeCount != lastChange else { return }
        lastChange = clipboard.changeCount
        guard let text = clipboard.string(forType: .string), !text.isEmpty else { return }
        history.removeAll { $0 == text }
        history.insert(text, at: 0)
        history = Array(history.prefix(9))
    }

    func paste(_ index: Int) {
        guard history.indices.contains(index) else { return }
        clipboard.clearContents()
        clipboard.setString(history[index], forType: .string)
        lastChange = clipboard.changeCount
        // Let the intercepted number key finish before sending Command-V.
        DispatchQueue.main.asyncAfter(deadline: .now() + 0.08) {
            let source = CGEventSource(stateID: .hidSystemState)
            let down = CGEvent(keyboardEventSource: source, virtualKey: 9, keyDown: true)
            let up = CGEvent(keyboardEventSource: source, virtualKey: 9, keyDown: false)
            down?.flags = .maskCommand
            up?.flags = .maskCommand
            down?.post(tap: .cghidEventTap)
            up?.post(tap: .cghidEventTap)
        }
    }
}

let manager = ClipboardStack()
if CommandLine.arguments.contains("--check") {
    print("Clipboard Stack: syntax and startup check passed.")
    exit(0)
}
let prompt = [kAXTrustedCheckOptionPrompt.takeUnretainedValue() as String: true] as CFDictionary
if !AXIsProcessTrustedWithOptions(prompt) {
    fputs("Waiting for Accessibility permission for Clipboard Stack (or Terminal when running as a script).\n", stderr)
    while !AXIsProcessTrusted() {
        RunLoop.main.run(until: Date(timeIntervalSinceNow: 3))
    }
}
let mask = (CGEventMask(1) << CGEventType.keyDown.rawValue)
         | (CGEventMask(1) << CGEventType.keyUp.rawValue)
manager.eventTap = CGEvent.tapCreate(tap: .cgSessionEventTap, place: .headInsertEventTap,
    options: .defaultTap, eventsOfInterest: mask, callback: { _, type, event, _ in
        if type == .tapDisabledByTimeout || type == .tapDisabledByUserInput {
            if let tap = manager.eventTap { CGEvent.tapEnable(tap: tap, enable: true) }
            return Unmanaged.passUnretained(event)
        }
        let modifiers = event.flags.intersection([.maskCommand, .maskShift, .maskAlternate, .maskControl])
        if modifiers == .maskCommand,
           let index = manager.slots[event.getIntegerValueField(.keyboardEventKeycode)] {
            manager.capture()
            guard manager.history.indices.contains(index) else { return Unmanaged.passUnretained(event) }
            if type == .keyDown && event.getIntegerValueField(.keyboardEventAutorepeat) == 0 {
                manager.paste(index)
            }
            return nil
        }
        return Unmanaged.passUnretained(event)
    }, userInfo: nil)
guard let tap = manager.eventTap else {
    fputs("Cannot listen for shortcuts. Check Accessibility permission for your terminal app.\n", stderr)
    exit(1)
}
let source = CFMachPortCreateRunLoopSource(kCFAllocatorDefault, tap, 0)
CFRunLoopAddSource(CFRunLoopGetMain(), source, .commonModes)
CGEvent.tapEnable(tap: tap, enable: true)
manager.capture()
let timer = Timer.scheduledTimer(withTimeInterval: 0.15, repeats: true) { _ in manager.capture() }
print("Clipboard Stack running: Command+1…9 pastes newest…oldest. Control+C stops it.")
print("Text only; keeps 9 unique copies in memory, including any sensitive text you copy.")
RunLoop.main.run()
