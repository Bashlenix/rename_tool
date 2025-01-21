import os
import shutil
import re
import sys
import json

# ANSI escape codes for colors
GREEN = '\033[32m'
RED = '\033[31m'
YELLOW = '\033[33m'
RESET = '\033[0m'

# Function to rename files and directories by removing trailing spaces and replacing sequences of spaces before file extensions with no spaces
def rename_files_in_directory(directory, dry_run=False, files_only=False, directories_only=False):
    # Define the regex patterns
    spaces_before_extension = re.compile(r"\s+(?=\.)")
    multiple_spaces = re.compile(r"\s+")

    files_to_rename = []
    dirs_to_rename = []
    backup_data = load_backup_data()  # Load existing backup data to avoid overwriting

    # Walk through the directory and its subdirectories
    for root, dirs, files in os.walk(directory, topdown=False):
        # If directories_only is True, rename only directories, not files
        if not directories_only:
            # For files
            for file_name in files:
                # Remove spaces before the file extension and replace all spaces with underscores
                new_name = re.sub(r"\s+(?=\.)", "", file_name)  # Remove spaces before file extensions
                new_name = re.sub(r"\s+", "_", new_name)  # Replace spaces with underscores

                old_path = os.path.join(root, file_name)
                new_path = os.path.join(root, new_name)

                # Check if renaming is needed
                if dry_run:
                    if new_name != file_name:
                        # Print color-coded output for dry-run
                        print(f"{RED}Dry run: '{old_path}' would be renamed to '{new_path}'{RESET}")
                    else:
                        print(f"{YELLOW}Dry run: No change for '{old_path}'{RESET}")
                else:
                    if new_name != file_name:
                        shutil.move(old_path, new_path)  # Rename the file
                        print(f"Renamed '{old_path}' to '{new_path}'")
                        backup_data[old_path] = new_path  # Add to backup data

                    files_to_rename.append((old_path, new_path))

        # Rename directories (only if directories_only is False, or if we're in -a or -d mode)
        if not files_only or directories_only:
            for dir_name in dirs:
                new_name = re.sub(r"\s+(?=\.)", "", dir_name)  # Remove spaces before directory name
                new_name = re.sub(r"\s+", "_", new_name)  # Replace spaces with underscores

                old_path = os.path.join(root, dir_name)
                new_path = os.path.join(root, new_name)

                if dry_run:
                    if new_name != dir_name:
                        # Print color-coded output for dry-run
                        print(f"{RED}Dry run: '{old_path}' would be renamed to '{new_path}'{RESET}")
                    else:
                        print(f"{YELLOW}Dry run: No change for '{old_path}'{RESET}")
                else:
                    if new_name != dir_name:
                        os.rename(old_path, new_path)  # Rename the directory
                        print(f"Renamed '{old_path}' to '{new_path}'")
                        backup_data[old_path] = new_path  # Add to backup data

                    dirs_to_rename.append((old_path, new_path))

    # After renaming, save the backup data (only if it's not a dry run)
    if not dry_run:
        save_backup_data(backup_data)
        
# Load the backup data from the backup file
def load_backup_data():
    try:
        with open("backup.json", "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

# Save the backup data to a backup file
def save_backup_data(data):
    with open("backup.json", "w") as f:
        json.dump(data, f, indent=4)

# Restore the original names from the backup
def restore_names(backup_data):
    for old_path, new_path in backup_data.items():
        try:
            os.rename(new_path, old_path)
            print(f"Restored file: '{new_path}' to '{old_path}'")
        except FileNotFoundError:
            print(f"Error: Could not restore '{new_path}' to '{old_path}'")

# Undo the renaming by restoring from backup
def undo_changes():
    backup_data = load_backup_data()
    if not backup_data:
        print("No rename operations found to undo.")
        return

    restore_names(backup_data)
    print("Renaming completed.")

# Print usage instructions
def print_usage():
    print("Usage: python rename_files.py <directory> [options]")
    print("Options:")
    print("-f           Rename files only")
    print("-d           Rename directories only")
    print("-a           Rename both files and directories (default)")
    print("-drymod      Dry run (simulates renaming without making changes)")
    print("-undo        Undo the renaming (restores original names)")
    print("-h           Show this help message")

# Main function
def main():
    if len(sys.argv) < 2:
        print_usage()
        return

    directory = sys.argv[1]
    dry_run = "-drymod" in sys.argv
    files_only = "-f" in sys.argv
    directories_only = "-d" in sys.argv
    undo = "-undo" in sys.argv
    all_mode = "-a" in sys.argv

    # If undo is specified, execute undo logic
    if undo:
        undo_changes()
        return

    # If -a is specified, rename both files and directories (default behavior)
    if all_mode:
        files_only = False
        directories_only = False
    
    try:
        rename_files_in_directory(directory, dry_run, files_only, directories_only)
        if dry_run:
            print("Testing completed successfully.")
        else:
            print("Renaming completed successfully.")
    except Exception as e:
        print(f"Error: {e}")

# Start the script
if __name__ == "__main__":
    main()
