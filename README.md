# Problem the Program Solves

Accessing files and folders with spaces in their names can be cumbersome, especially in command-line environments where spaces require escaping or quoting. This often leads to inefficiencies, errors, and frustration. Additionally, inconsistent naming with trailing spaces or multiple spaces can make directories appear untidy and hard to manage.

The File Renamer Tool solves this problem by replacing spaces in file and folder names with underscores, ensuring names are clean, consistent, and easy to access. It simplifies command-line interactions, enhances automation workflows, and improves overall file organization.


# Target Audience

This tool is ideal for:

Command-Line Users: Developers, system administrators, and anyone who frequently interacts with files and directories through the command-line.

Automation Enthusiasts: Individuals setting up scripts or workflows that require predictable and consistent file names.

Professionals and Creators: Those managing large collections of files who need to ensure accessibility and readability of names.

Casual Users: Anyone wanting to make their file system more navigable and organized.


# What the Program Does
The program:

1. Scans a specified directory for files and subdirectories.
2. Identifies names with spaces and replaces them with underscores for uniformity.
3. Handles additional inconsistencies by:
    * Removing trailing spaces before file extensions.
    * Consolidating multiple spaces into single underscores.
    * Supports optional "dry run" mode for previewing changes without making modifications.
4. Saves a backup of the original names, allowing users to undo changes if needed.
5. Offers flexibility to target:
    * Files only.
    * Directories only.
    * Both files and directories.


# Features
- **Main Functionality:** Replaces spaces in names with underscores to improve accessibility and compatibility.
- **Dry Run Mode:** Simulates renaming to preview changes without committing them.
- **Backup and Undo:** Allows restoration of original names using a backup file.
- **Custom Modes:** Provides options to target only files, only directories, or both.
- **Cross-Platform Compatibility:** Works seamlessly on macOS, Linux, and Windows systems.
- **Color-Coded Output:** Makes it easy to track changes during execution with clear visual feedback.


# Command Line Interface

The program provides an easy-to-use command-line interface with the following options:

* Rename files and directories (default):
 ```python
python rename_files.py <directory> -a
 ```

* Rename files only:
 ```python
python rename_files.py <directory> -f
 ```

* Rename directories only:
 ```python
python rename_files.py <directory> -d
 ```

* Dry run (simulate changes):
 ```python
python rename_files.py <directory> -drymod
 ```

* Undo changes:
 ```python
python rename_files.py -undo
 ```

* View help message:
 ```python
python rename_files.py -h
 ```

# How It Works

1. *User Input:* Specify the directory to process and select the desired mode (files, directories, or both).
2. *Directory Scanning:* The program iterates through all files and subdirectories.
3. *Space Replacement:* Replaces all spaces in names with underscores and removes unnecessary spaces.
4. *Backup Creation:* Saves a backup of the original names to a backup.json file.
5. *Undo Support:* Allows restoration of names using the backup file.


# Example

## Before Running

 ``` example_dir/
├── file with spaces.txt
├── another  file   .docx
├── sub folder/
│   ├── messy   name.jpg
 ```

## Command

 ``` pythone
python rename_files.py example_dir -a
 ```

## After Renaming

 ```
example_dir/
├── file_with_spaces.txt
├── another_file.docx
├── sub_folder/
│   ├── messy_name.jpg
 ```


# Potential Use Cases

- **Command-Line Navigation:** Simplifies access to files and directories without needing escape sequences or quotes.
- **Automation Scripts:** Ensures compatibility with workflows that require clean and predictable file names.
- **File Management:** Organizes files and folders by replacing spaces with underscores for better readability and usability.
- **Cross-Platform Access:** Improves file handling across different systems, including those with strict naming rules.
