#!/usr/bin/env python3
import os
import json
import subprocess

# Path to config file (hidden in home directory)
CONFIG_FILE = os.path.expanduser("~/.keno_aliases.json")

# Your ASCII art – replace with your own logo (use raw triple quotes)
LOGO = r"""
        /\ \/ /    /\  ___\   /\ '-.\ \   /\  __ \
        \ \  _'-.  \ \  __\   \ \ \-.  \  \ \ \/\ \
         \ \_\ \_\  \ \_____\  \ \_\\'\_\  \ \_____\
          \/_/\/_/   \/_____/   \/_/ \/_/   \/_____/
"""

def clear_screen():
    """Clear the terminal screen (Linux/macOS)."""
    os.system('clear')

def load_aliases():
    """Load aliases from JSON file."""
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as f:
            return json.load(f)
    else:
        return {}

def save_aliases(aliases):
    """Save aliases to JSON file."""
    with open(CONFIG_FILE, 'w') as f:
        json.dump(aliases, f, indent=4)

def show_menu():
    """Display the main menu."""
    print(LOGO)
    print("[L]ist")
    print("[A]dd")
    print("[R]emove")
    print("[S]tart")
    print("[Q]uit")
    print("Your choice: ", end='', flush=True)

def list_aliases(aliases):
    if not aliases:
        print("\nNo aliases stored.\n")
    else:
        print("\nSaved aliases:")
        for name, command in aliases.items():
            print(f"  {name} -> {command}")
        print()

def add_alias(aliases):
    name = input("Alias name: ").strip()
    if not name:
        print("Invalid name.\n")
        return
    if name in aliases:
        overwrite = input(f"Alias '{name}' already exists. Overwrite? (y/n): ").lower()
        if overwrite != 'y':
            print("Cancelled.\n")
            return
    command = input("Command (e.g. /path/to/program or 'java -jar ...'): ").strip()
    if not command:
        print("No command entered.\n")
        return
    aliases[name] = command
    save_aliases(aliases)
    print(f"Alias '{name}' saved.\n")

def remove_alias(aliases):
    if not aliases:
        print("No aliases stored.\n")
        return
    name = input("Alias name to remove: ").strip()
    if name in aliases:
        del aliases[name]
        save_aliases(aliases)
        print(f"Alias '{name}' removed.\n")
    else:
        print(f"Alias '{name}' not found.\n")

def start_alias(aliases):
    if not aliases:
        print("No aliases stored.\n")
        return
    name = input("Alias name to start: ").strip()
    if name not in aliases:
        print(f"Alias '{name}' not found.\n")
        return
    command = aliases[name]
    print(f"Starting: {command}")
    try:
        subprocess.run(command, shell=True, check=False)
    except Exception as e:
        print(f"Error starting command: {e}")
    print()

def main():
    aliases = load_aliases()
    while True:
        clear_screen()
        show_menu()
        choice = input().strip().lower()
        if choice == 'l':
            list_aliases(aliases)
        elif choice == 'a':
            add_alias(aliases)
        elif choice == 'r':
            remove_alias(aliases)
        elif choice == 's':
            start_alias(aliases)
        elif choice == 'q':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please use L, A, R, S or Q.\n")
        input("Press Enter to continue...")

if __name__ == "__main__":
    main()
