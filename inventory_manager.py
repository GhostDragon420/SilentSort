import os
import time

LOG_FILE = "log.txt"
CONFIG_FILE = "config.txt"

# File extensions to include
FILE_EXTENSIONS = ['.xml', '.json']


def load_default_path():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as file:
            return file.read().strip()
    return os.getcwd()


def save_default_path(path):
    with open(CONFIG_FILE, 'w') as file:
        file.write(path)


DEFAULT_SEARCH_PATH = load_default_path()


def log_message(message):
    with open(LOG_FILE, 'a') as log:
        log.write(message + '\n')
    print(message)


def clear_log():
    with open(LOG_FILE, 'w') as log:
        log.write('')


def find_files(path, extensions):
    found_files = []
    for root, _, files in os.walk(path):
        for file in files:
            if any(file.endswith(ext) for ext in extensions):
                found_files.append(os.path.join(root, file))
    return found_files


def scan_files(file_list):
    for file in file_list:
        log_message(f"[Scan] Found: {file}")


def manual_scan():
    print("\nManual Scan:")
    scan_type = input("Quick or Full scan? (q/f) [Default: q]: ").lower()
    if scan_type not in ['f', 'full']:
        scan_type = 'quick'

    custom_path = input(f"Enter path to scan or press Enter to use default [{DEFAULT_SEARCH_PATH}]: ")
    path = custom_path if custom_path else DEFAULT_SEARCH_PATH

    if not os.path.exists(path):
        print("Invalid path. Scan aborted.")
        return

    print(f"{scan_type.capitalize()} scan started.")
    file_list = find_files(path, FILE_EXTENSIONS)
    scan_files(file_list)
    print(f"{scan_type.capitalize()} scan completed.")


def search_keyword():
    keyword = input("Enter keyword to search for: ").strip()
    if not keyword:
        print("No keyword entered. Returning to menu.")
        return

    custom_path = input(f"Enter path to search or press Enter to use default [{DEFAULT_SEARCH_PATH}]: ")
    path = custom_path if custom_path else DEFAULT_SEARCH_PATH

    file_list = find_files(path, FILE_EXTENSIONS)
    found = False
    for file_path in file_list:
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
                for i, line in enumerate(file):
                    if keyword.lower() in line.lower():
                        preview = line.strip()[:100]
                        log_message(f"[Match] {file_path} (Line {i + 1}): {preview}")
                        found = True
        except Exception as e:
            log_message(f"Error reading {file_path}: {e}")

    if not found:
        print("No matches found.")
    else:
        print("Keyword search complete. Check log.txt for details.")


def view_log():
    try:
        with open(LOG_FILE, 'r') as log:
            print("\n--- Log File ---")
            print(log.read())
        open_choice = input("Open in Notepad? (y/n): ").lower()
        if open_choice == 'y':
            os.system(f'notepad {LOG_FILE}')
    except FileNotFoundError:
        print("Log file not found.")


def set_default_path():
    new_path = input("Enter the new default folder path: ").strip()
    if os.path.exists(new_path):
        save_default_path(new_path)
        print(f"Default path updated to: {new_path}")
    else:
        print("Invalid path. Default not changed.")


def main():
    clear_log()
    while True:
        print("\n=== 7 Days to Die Inventory Manager ===")
        print("1. Manual Scan (Quick or Full)")
        print("2. Search for Keyword")
        print("3. View Logfile")
        print("4. Set Default Scan Folder")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                manual_scan()
            elif choice == 2:
                search_keyword()
            elif choice == 3:
                view_log()
            elif choice == 4:
                set_default_path()
            elif choice == 5:
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


if __name__ == "__main__":
    main()
