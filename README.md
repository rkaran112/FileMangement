# FileMangement

A command-line file and directory management tool written in Python.

## What it does

`fileDirclass.py` is a single-file, menu-driven CLI application that wraps common file/directory operations behind an interactive text menu. Supported operations:

- **Files:** open (read and print contents), create, delete, search by wildcard pattern (e.g. `*.txt`), append text to a file
- **Files (copy/move):** copy a file between locations, move a file between locations
- **Directories:** list subdirectories, remove a directory tree (with confirmation to create missing directories)
- **Archives:** create a ZIP archive from a directory's contents, extract a ZIP archive to a directory

The program runs as an infinite loop presenting a numbered menu (1-12); the user picks an option and is prompted for further input (paths, filenames, patterns, etc.) until they choose "Exit".

## Tech stack

- Python 3 (standard library only: `os`, `shutil`, `zipfile`, `fnmatch`)
- No third-party dependencies, no `requirements.txt`/`pyproject.toml` in the repo

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/rkaran112/FileMangement.git
   cd FileMangement
   ```
2. No dependency installation is needed — everything used is part of the Python standard library. Python 3 must be installed.

## Usage

Run the script directly:

```bash
python fileDirclass.py
```

You'll see a menu like:

```
1. Open File
2. Create File
3. Delete File
4. Search File
5. Write File
6. Copy File
7. Move File
8. Create Zip Archive
9. Extract Zip Archive
10. List Directories
11. Remove Directory
12. Exit
```

Enter a number and follow the prompts (e.g. entering a directory path, then a filename) to perform the chosen action.

## Status

**Work in progress.** The core menu and each operation are implemented and mostly reachable end-to-end, but there are known issues in the current code:

- `DirectoryManagement.check_dir()` has inconsistent return values: it returns the path string when the directory already exists, but returns `True` (not the path) when the directory is newly created — code that calls `check_dir()` and then does `os.path.join(dir_path, ...)` will break in the "directory just created" case. It also has no `return` for the "don't create it" branch, so that path implicitly returns `None`.
- `AddFunction.create_Zip()` contains duplicated/copy-pasted `except` blocks and its docstring/comment mentions a password-protected archive, but the password logic is commented out and not implemented.
- `AddFunction` methods (`create_Zip`/`extract_Zip`) have inconsistent indentation relative to the rest of the file (not a syntax error, but a style issue).
- The script has no `if __name__ == "__main__":` guard — it executes the menu loop at import time, and there is a stray extra `main_menu()` call after the loop ends (line 276) that has no effect but is dead/leftover code.
- No automated tests, no `requirements.txt`, and no license file are present.

In short: functional for basic manual use, but has real bugs (notably the `check_dir()` return-value inconsistency) and rough edges that would need cleanup before it could be considered production-ready.
