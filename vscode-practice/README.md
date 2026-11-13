# Your Practice Path

Local-only VS Code dashboard for the curriculum stored in `practice/catalog.json`.
Opens automatically in trusted folders containing that catalogue. Use **Practice: Open Dashboard** in the Command Palette, or `cf dashboard` in the terminal.

Read Full Statement opens the local Markdown beside the C++ solution. Run, Test samples, and Submit & watch use the repository's Python commands. Source files are saved before these button actions run. Terminal `runcode` and `testcode` use the selected problem. Saving a curriculum C++ source in VS Code selects it automatically.

No network requests originate in the dashboard. Manual-submit/verdict commands access Codeforces and GitHub only when invoked. Credentials, progress and submission snapshots remain in ignored `.cf-local/`.
