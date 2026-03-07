# 👻 GhostPass - Secure Password Leak Checker

![Python](https://img.shields.io/badge/Python-3.7+-blue?logo=python)
![License](https://img.shields.io/badge/License-MIT-green)
![HIBP](https://img.shields.io/badge/Powered%20by-Have%20I%20Been%20Pwned-red)

A command-line tool that checks if your passwords have been exposed in data breaches — **without ever sending your password over the internet**.

Uses the [Have I Been Pwned](https://haveibeenpwned.com/) **k-Anonymity API**. Only the first 5 characters of the SHA-1 hash are sent. Your full password **stays on your machine**.

## Features

- Animated ghost intro with leak effects
- Color-coded breach results (red = leaked, green = safe)
- Hidden password input (never shown on screen)
- Batch check passwords from a file
- Scan progress with hacking-style output
- Works on Linux, macOS, and Windows

## Installation

```bash
# Step 1: Clone the repo
git clone https://github.com/ghayth-1/GhostPass.git

# Step 2: Enter the folder
cd GhostPass

# Step 3: Create virtual environment
python3 -m venv venv

# Step 4: Activate it
source venv/bin/activate

# Step 5: Install (IMPORTANT: use this exact command)
pip install --target=./venv/lib/python3.*/site-packages -e .

# Step 6: Run it
python -m ghostpass
```

### Quick Install (copy-paste all at once)

```bash
git clone https://github.com/ghayth-1/GhostPass.git && cd GhostPass && python3 -m venv venv && source venv/bin/activate && pip install requests colorama && python -m ghostpass
```

## Usage

### Interactive Mode
```bash
python -m ghostpass
```

### Check passwords from a file
```bash
python -m ghostpass -f passwords.txt
```

## Demo

```
  [GHOSTPASS] > Enter password: ********

  [*] Hashing with SHA-1...
  [*] Querying HIBP (k-Anonymity)...
  [*] Comparing locally...

  +====================================================+
  |            !! PASSWORD BREACHED !!                  |
  +====================================================+
  |  Target  : Your password
  |  Leaked  : 3,355,328 time(s)
  |  Status  : CRITICAL - CHANGE IMMEDIATELY
  +====================================================+
```

## Security

| Concern | How GhostPass handles it |
|---|---|
| Password transmission | Only 5 chars of SHA-1 hash sent |
| Screen display | Passwords are NEVER shown |
| Storage | Nothing is logged or saved |
| Local comparison | All matching done on YOUR machine |

## Requirements

- Python 3.7+
- requests
- colorama

## License

MIT License - see [LICENSE](LICENSE) for details.

## Author

Made by [@ghayth-1](https://github.com/ghayth-1)
