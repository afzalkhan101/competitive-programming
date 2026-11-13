# Competitive programming

Save your C++ file, then run these commands from this folder or a subfolder:

```sh
runcode
```

Compiles the most recently saved `.cpp`, `.cc`, or `.cxx` file with C++17 and runs it with interactive input. Scratch files and build folders are skipped. Compilation errors prevent execution. Generated programs go in the ignored `build/runcode/` folder.

To choose a specific file:

```sh
runcode "A_Beautiful_Matrix.cpp"
```

To stage all changes, commit them, and push the current branch to GitHub:

```sh
push this
push this "Solve Beautiful Matrix"
```

The default commit message is `Update competitive programming solutions`. If there are no changes, it still pushes existing commits. GitHub SSH authentication must already work. Tracked files remain tracked even when listed in `.gitignore`.

## Shell setup

Add this line to `~/.zshrc`, then open a new terminal or run `source ~/.zshrc`:

```sh
source /Users/laptopheaven/competitive-programming/scripts/terminal.zsh
```
