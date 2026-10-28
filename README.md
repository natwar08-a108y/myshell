# 🐚 MyShell — A Minimal Command-Line Shell in Python

**A lightweight, interactive command-line shell built with Python.**

MyShell recreates essential shell behavior through a custom terminal prompt, built-in directory navigation, external command execution, and basic error handling.

## ✨ Features

- 🖥️ **Interactive Terminal:** Runs continuously until the user exits.
- 📂 **Custom Prompt:** Displays the current working directory and uses `~` for the home directory.
- 🔄 **Directory Navigation:** Supports `cd`, `cd ..`, `cd -`, and navigation to specified paths.
- ⚙️ **Command Execution:** Runs external programs using Python's `subprocess` module.
- 📝 **Smart Input Parsing:** Uses `shlex.split()` to handle quoted arguments containing spaces.
- 🚦 **Exit Status Tracking:** Records command return codes and handles common execution failures.
- 🛡️ **Error Handling:** Detects unmatched quotes, missing commands, invalid directories, and permission errors.
- ⌨️ **Keyboard Interrupts:** Handles `Ctrl+C` and `Ctrl+D` appropriately.
- 🔧 **Directory Recovery:** Attempts to recover if the current working directory has been deleted.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| 🐍 Python 3 | Core programming language |
| `shlex` | Command-line input parsing |
| `subprocess` | External command execution |
| `os` | Filesystem and directory management |
| `sys` | Program termination and exit status handling |

**Dependencies:** No third-party Python packages required.

## 🚀 Getting Started

### Prerequisites

- Python 3.9 or later recommended.
- A terminal with Python installed.
- System commands available in your environment.

### Installation

**1. Clone the repository**

```bash
git clone https://github.com/YOUR-USERNAME/MyShell.git
```

**2. Navigate to the project directory**

```bash
cd MyShell
```

**3. Launch MyShell**

```bash
python3 shell.py
```

On Windows, you can use:

```powershell
python shell.py
```

Replace `YOUR-USERNAME` and `MyShell` with your actual GitHub username and repository name.

## 💻 Usage

Once launched, MyShell displays a prompt based on your current working directory.

```text
myshell:~$ pwd
/home/user

myshell:~$ cd Documents
myshell:~/Documents$ pwd
/home/user/Documents

myshell:~/Documents$ cd ..
myshell:~$ echo "Hello from MyShell"
Hello from MyShell

myshell:~$ exit
```

*Example paths and output are illustrative and may vary by operating system.*

### 📌 Built-in Commands

| Command | Description |
|---|---|
| `cd` | Navigate to the home directory |
| `cd /path/to/dir` | Navigate to a specified directory |
| `cd ..` | Move to the parent directory |
| `cd -` | Return to the previous directory |
| `exit` | Exit the shell |
| `exit 1` | Exit with the specified numeric status |

Commands such as `pwd`, `echo`, `ls`, `python3`, and `git` are executed as external programs when available in the environment.

### ⚠️ Error Handling

MyShell provides readable error messages for common failures.

```text
myshell:~$ unknowncommand
myshell: command not found: unknowncommand

myshell:~$ cd /nonexistent
myshell: cd: no such file or directory: /nonexistent

myshell:~$ echo "unfinished
myshell: syntax error: unmatched quote
```

## ⚙️ How It Works

MyShell follows a **Read-Evaluate-Execute loop**:

1. **Display Prompt** — Shows the current working directory.
2. **Read Input** — Accepts a command from the user.
3. **Parse Input** — Converts the command into tokens using `shlex.split()`.
4. **Identify Command** — Separates the command name from its arguments.
5. **Execute Built-ins** — Processes `cd` and `exit` internally.
6. **Run External Commands** — Launches other programs through `subprocess.run()`.
7. **Update Status** — Records the command's return code or an appropriate error status.
8. **Repeat** — Waits for the next command until the shell terminates.

## 🚦 Exit Status Codes

| Code | Meaning |
|---|---|
| `0` | Successful command or normal exit |
| `1` | Common directory-navigation errors |
| `2` | Syntax error or invalid numeric exit argument |
| `126` | Execution denied |
| `127` | Command not found |
| `130` | Interrupted by `Ctrl+C` |

These codes follow common shell conventions where applicable. MyShell implements a subset of standard shell behavior.

## 📁 Project Structure

```text
MyShell/
├── shell.py
└── README.md
```

- `shell.py` — Main implementation containing the interactive loop, command parsing, directory navigation, process execution, and error handling.
- `README.md` — Project documentation and usage guide.

## 🎯 Learning Outcomes

Through this project, I explored:

- Command parsing and tokenization.
- Filesystem navigation and working-directory management.
- External process execution.
- Exception handling and keyboard interrupts.
- Exit codes and command failure handling.
- Building an interactive command-line application in Python.

---

<p align="center">
  <b>🐚 MyShell</b><br/>
  <i>Understanding the command line by building one from scratch.</i>
</p>
