<a class="practice-back" href="vscode://local.codeforces-practice/dashboard">← Back to Dashboard</a>

# 729A · Interview with Oleg

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="mixed">Mixed Practice</span><span class="practice-tag">implementation</span><span class="practice-tag">strings</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/729/A) · Rating 900

Time: 1.0 seconds · Memory: 256.0 MB

## Problem

Polycarp has interviewed Oleg and has written the interview down without punctuation marks and spaces to save time. Thus, the interview is now a string s consisting of n lowercase English letters.

There is a filler word ogo in Oleg's speech. All words that can be obtained from ogo by adding go several times to the end of it are also considered to be fillers. For example, the words ogo, ogogo, ogogogo are fillers, but the words go, og, ogog, ogogog and oggo are not fillers.

The fillers have maximal size, for example, for ogogoo speech we can't consider ogo a filler and goo as a normal phrase. We should consider ogogo as a filler here.

To print the interview, Polycarp has to replace each of the fillers with three asterisks. Note that a filler word is replaced with exactly three asterisks regardless of its length.

Polycarp has dealt with this problem in no time. Can you do the same? The clock is ticking!

## Input

The first line contains a positive integer n (1 ≤ n ≤ 100) — the length of the interview.

The second line contains the string s of length n, consisting of lowercase English letters.

## Output

Print the interview text after the replacement of each of the fillers with "***". It is allowed for the substring "***" to have several consecutive occurences.

## Sample 1

Input

```text
7
aogogob
```

Output

```text
a***b
```

## Sample 2

Input

```text
13
ogogmgogogogo
```

Output

```text
***gmg***
```

## Sample 3

Input

```text
9
ogoogoogo
```

Output

```text
*********
```

## Note

The first sample contains one filler word ogogo, so the interview for printing is "a***b".

The second sample contains two fillers ogo and ogogogo. Thus, the interview is transformed to "***gmg***".

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
