# 👻 GhostPass - Secure Password Leak Checker

![Python](https://img.shields.io/badge/Python-3.7+-blue?logo=python)
![License](https://img.shields.io/badge/License-MIT-green)
![HIBP](https://img.shields.io/badge/Powered%20by-Have%20I%20Been%20Pwned-red)

A command-line tool that checks if your passwords have been exposed in data breaches — **without ever sending your password over the internet**.

## Installation

```bash
git clone https://github.com/ghayth-1/GhostPass.git
cd GhostPass
python3 -m venv venv
source venv/bin/activate
pip install .
ghostpass
```

## Usage

```bash
ghostpass                    # Interactive mode
ghostpass -f passwords.txt   # Check from file
ghostpass --help             # Show help
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

## License

MIT License - see [LICENSE](LICENSE) for details.

## Author

Made by [@ghayth-1](https://github.com/ghayth-1)
