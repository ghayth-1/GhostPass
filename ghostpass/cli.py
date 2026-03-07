import sys
import hashlib
import getpass
import argparse
import os
import time

try:
    import requests
except ImportError:
    print("[ERROR] pip install requests")
    sys.exit(1)

try:
    from colorama import init, Fore, Style
except ImportError:
    print("[ERROR] pip install colorama")
    sys.exit(1)

init(autoreset=True)
HIBP_API_URL = "https://api.pwnedpasswords.com/range/"

GHOST_1 = Fore.RED + r"""


                           ..:::::::::..
                        .::::::::::::::::::..
                      .:::::::::::::::::::::::::
                    .:::::::::::::::::::::::::::::.
                   ::::::::::::::::::::::::::::::::: 
                  ::::::::::::::::::::::::::::::::::: 
                 :::::::::::::::::::::::::::::::::::::
                :::::::::::::::::::::::::::::::::::::::
                :::::::::::::::::::::::::::::::::::::::
                :::::::::::::::::::::::::::::::::::::::
                :::::::::::::::::::::::::::::::::::::::
                 :::::::::::::::::::::::::::::::::::::
                  ::::::::::::::::::::::::::::::::::: 
                   ::::::::::::::::::::::::::::::::: 
                    .:::::::::::::::::::::::::::::.
                      .:::::::::::::::::::::::::
                        .::::::::::::::::::..
                           ..:::::::::..


""" + Style.RESET_ALL

GHOST_2 = Fore.YELLOW + r"""


                           ..:::::::::..
                        .::::::::::::::::::.
                      .:::::::::::::::::::::::.
                    .:::::::: :::::::::: ::::::::. 
                   :::::::::: :::::::::: ::::::::::
                  ::::::::::  :::::::::: :::::::::::
                 ::::::::::::::::::::::::::::::::::::
                :::::::::::::::::::::::::::::::::::::
                :::::::::::::::::::::::::::::::::::::
                :::::::::::::::::::::::::::::::::::::
                :::::::::::::::::::::::::::::::::::::
                 ::::::::::::::::::::::::::::::::::::
                  ::::::::::::::::::::::::::::::::::
                   ::::::::::::::::::::::::::::::::
                    .::::::::::::::::::::::::::::.
                      .:::::::::::::::::::::::.
                        .::::::::::::::::::.
                           ..:::::::::..


""" + Style.RESET_ALL

GHOST_LEAK = Fore.CYAN + Style.BRIGHT + r"""

                           ████████████
                        ████░░░░░░░░░░████
                      ███░░░░░░░░░░░░░░░░███
                    ███░░░░░░░░░░░░░░░░░░░░███
                   ██░░░░████░░░░░░████░░░░░░██
                  ██░░░░██████░░░░██████░░░░░░██
                  ██░░░░██████░░░░██████░░░░░░██
                  ██░░░░░████░░░░░░████░░░░░░░██
                  ██░░░░░░░░░░████░░░░░░░░░░░░██
                  ██░░░░░░░░░██████░░░░░░░░░░░██
                  ██░░░░░░░░░░████░░░░░░░░░░░░██
                  ██░░░░░░░░░░░░░░░░░░░░░░░░░░██
                   ██░░░░░░░░░░░░░░░░░░░░░░░░██
                   ██░░░░░░░░░░░░░░░░░░░░░░░░██
                    ██░░░░░░░░░░░░░░░░░░░░░░██
                    ██░░░██░░░░░░░░░░██░░░░██
                   ██░░██ ██░░░░░░░██ ██░░░██
                  ██░░██   ██░░░░██   ██░░░░██
                  █████     ██████     ███████
""" + Style.RESET_ALL

LEAK_DRIP = Fore.RED + Style.BRIGHT + r"""
                  ██                          ██
                  ██                          ██
                   █         ████████        █
                   █        ██      ██       █
                    █       █ LEAKED █      █
                    █       ██      ██      █
                     █       ████████      █
                      █                   █
                       █     ████████    █
                        ██  ██PASS██  ██
                          ████WORD████
                             ██████
                               ██
                               ██
                                █
                                █
                                .
                                .
""" + Style.RESET_ALL

GHOST_FULL = Fore.GREEN + Style.BRIGHT + r"""
                           ████████████
                        ████          ████
                      ███    ██    ██    ███
                    ███      ██    ██      ███
                   ██     ██████████████    ██
                  ██                         ██
                  ██   ██              ██    ██
                  ██    ████████████████     ██
                  ██                         ██
                  ██     ██   ██   ██   ██   ██
                   ██   ████ ████ ████ ████ ██
                    ██ █  ██ █  █ ██ █  ██ ██
                     ██    ██    ██    ██  ██
                      █    ██    ██    ██  █
                     ██    ██    ██    ██   █
                     █  ████  ██  ████  ██  █
                     ████   ████  ████   ████
                     ██      ██    ██      ██
""" + Style.RESET_ALL

TITLE = Fore.RED + Style.BRIGHT + """
   ██████╗  ██╗  ██╗  ██████╗  ███████╗ ████████╗
  ██╔════╝  ██║  ██║ ██╔═══██╗ ██╔════╝ ╚══██╔══╝
  ██║  ███╗ ███████║ ██║   ██║ ███████╗    ██║   
  ██║   ██║ ██╔══██║ ██║   ██║ ╚════██║    ██║   
  ╚██████╔╝ ██║  ██║ ╚██████╔╝ ███████║    ██║   
   ╚═════╝  ╚═╝  ╚═���  ╚═════╝  ╚══════╝    ╚═╝   
""" + Style.RESET_ALL

TITLE2 = Fore.YELLOW + Style.BRIGHT + """
  ██████╗   █████╗  ███████╗ ███████╗
  ██╔══██╗ ██╔══██╗ ██╔════╝ ██╔════╝
  ██████╔╝ ███████║ ███████╗ ███████╗
  ██╔═══╝  ██╔══██║ ╚════██║ ╚════██║
  ██║      ██║  ██║ ███████║ ███████║
  ╚═╝      ╚═╝  ╚═╝ ╚══════╝ ╚══════╝
""" + Style.RESET_ALL

SUBTITLE = (
    Fore.WHITE + Style.BRIGHT +
    "  +-------------------------------------------------+\n" +
    "  |   " + Fore.RED + "YOUR PASSWORDS LEAK..." + Fore.WHITE + "  WE CATCH THEM  " + Fore.RED + "!!" + Fore.WHITE + "  |\n" +
    "  |   " + Fore.CYAN + "Powered by Have I Been Pwned API" + Fore.WHITE + "            |\n" +
    "  |   " + Fore.GREEN + "Your password NEVER leaves your machine" + Fore.WHITE + "    |\n" +
    "  +-------------------------------------------------+" +
    Style.RESET_ALL
)

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def typewrite(text, delay=0.01):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def animate_intro():
    try:
        for i in range(2):
            clear_screen()
            print(GHOST_1)
            time.sleep(0.2)
            clear_screen()
            print(GHOST_2)
            time.sleep(0.2)
        clear_screen()
        for line in GHOST_LEAK.split("\n"):
            print(line)
            time.sleep(0.05)
        time.sleep(0.6)
        clear_screen()
        print(GHOST_LEAK)
        for line in LEAK_DRIP.split("\n"):
            print(line)
            time.sleep(0.08)
        time.sleep(0.5)
        clear_screen()
        print(GHOST_FULL)
        time.sleep(0.3)
        clear_screen()
        print(GHOST_FULL)
        for line in TITLE.split("\n"):
            print(line)
            time.sleep(0.05)
        for line in TITLE2.split("\n"):
            print(line)
            time.sleep(0.05)
        time.sleep(0.3)
        print()
        for line in SUBTITLE.split("\n"):
            typewrite(line, 0.008)
        print()
        time.sleep(0.5)
        sys.stdout.write(Fore.RED + "  [" + Style.RESET_ALL)
        for i in range(30):
            sys.stdout.write(Fore.RED + Style.BRIGHT + "#" + Style.RESET_ALL)
            sys.stdout.flush()
            time.sleep(0.04)
        sys.stdout.write(Fore.RED + "] " + Fore.GREEN + "READY\n\n" + Style.RESET_ALL)
        time.sleep(0.3)
    except KeyboardInterrupt:
        clear_screen()

def sha1_hash(pw):
    return hashlib.sha1(pw.encode("utf-8")).hexdigest().upper()

def check_password(pw):
    h = sha1_hash(pw)
    r = requests.get(HIBP_API_URL + h[:5], timeout=10)
    r.raise_for_status()
    for line in r.text.splitlines():
        parts = line.split(":")
        if parts[0].strip() == h[5:]:
            return int(parts[1].strip())
    return 0

def display_result(label, count):
    if count > 0:
        print(Fore.RED + Style.BRIGHT)
        print("  +====================================================+")
        print("  |            !! PASSWORD BREACHED !!                  |")
        print("  +====================================================+")
        print("  |  Target  : " + label)
        print("  |  Leaked  : " + str(count) + " time(s)")
        print("  |  Status  : " + Fore.YELLOW + "CRITICAL - CHANGE IMMEDIATELY" + Fore.RED)
        print("  +====================================================+")
        print(Style.RESET_ALL)
    else:
        print(Fore.GREEN + Style.BRIGHT)
        print("  +====================================================+")
        print("  |                  SECURE                             |")
        print("  +====================================================+")
        print("  |  Target  : " + label)
        print("  |  Leaked  : 0 breaches")
        print("  |  Status  : CLEAN - No leaks found")
        print("  +====================================================+")
        print(Style.RESET_ALL)

def print_separator():
    print(Fore.RED + "  " + "=" * 52 + Style.RESET_ALL)

def interactive_mode():
    print(Fore.CYAN + Style.BRIGHT + "\n  >> INTERACTIVE MODE <<" + Style.RESET_ALL)
    print(Fore.WHITE + "  Type 'q' to quit | Passwords are hidden\n" + Style.RESET_ALL)
    print_separator()
    while True:
        try:
            pw = getpass.getpass(Fore.YELLOW + "\n  [GHOSTPASS] > Enter password: " + Style.RESET_ALL)
        except (EOFError, KeyboardInterrupt):
            print(Fore.CYAN + "\n\n  Session terminated. Stay safe!\n" + Style.RESET_ALL)
            break
        if pw.lower() in ("q", "quit"):
            print(Fore.CYAN + "\n  Session terminated. Stay safe!\n" + Style.RESET_ALL)
            break
        if not pw.strip():
            print(Fore.YELLOW + "  [!] Empty input." + Style.RESET_ALL)
            continue
        try:
            print(Fore.WHITE + "  [*] Hashing with SHA-1..." + Style.RESET_ALL)
            time.sleep(0.3)
            print(Fore.WHITE + "  [*] Querying HIBP (k-Anonymity)..." + Style.RESET_ALL)
            time.sleep(0.4)
            count = check_password(pw)
            print(Fore.WHITE + "  [*] Comparing locally..." + Style.RESET_ALL)
            time.sleep(0.2)
            display_result("Your password", count)
        except requests.exceptions.ConnectionError:
            print(Fore.RED + "  [X] Network error." + Style.RESET_ALL)
        except requests.exceptions.Timeout:
            print(Fore.RED + "  [X] Timed out." + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + "  [X] Error: " + str(e) + Style.RESET_ALL)
        print_separator()

def file_mode(filepath):
    if not os.path.isfile(filepath):
        print(Fore.RED + "  [X] File not found: " + filepath + Style.RESET_ALL)
        sys.exit(1)
    print(Fore.CYAN + Style.BRIGHT + "\n  >> FILE SCAN MODE <<" + Style.RESET_ALL)
    print(Fore.WHITE + "  Target: " + filepath + Style.RESET_ALL)
    print_separator()
    with open(filepath) as f:
        lines = f.readlines()
    total = 0
    leaked = 0
    safe = 0
    for num, raw in enumerate(lines, 1):
        pw = raw.strip()
        if not pw or pw.startswith("#"):
            continue
        total += 1
        try:
            count = check_password(pw)
            display_result("Line " + str(num), count)
            if count > 0:
                leaked = leaked + 1
            else:
                safe = safe + 1
        except Exception as e:
            print(Fore.RED + "  [X] Error line " + str(num) + ": " + str(e) + Style.RESET_ALL)
    print_separator()
    print(Fore.CYAN + Style.BRIGHT + "\n  SCAN COMPLETE" + Style.RESET_ALL)
    print(Fore.WHITE + "  Total  : " + str(total) + Style.RESET_ALL)
    print(Fore.RED + "  Leaked : " + str(leaked) + Style.RESET_ALL)
    print(Fore.GREEN + "  Safe   : " + str(safe) + Style.RESET_ALL)
    print()

def main():
    animate_intro()
    parser = argparse.ArgumentParser(prog="ghostpass")
    parser.add_argument("-f", "--file", type=str, help="File with passwords")
    args = parser.parse_args()
    if args.file:
        file_mode(args.file)
    else:
        interactive_mode()

if __name__ == "__main__":
    main()
