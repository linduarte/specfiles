# SpecFiles Backup Script

This repository contains a Python script designed to perform backups of specified files and directories to a designated backup location. The script ensures that important configuration files and directories are safely copied to a backup directory, making it easier to restore them when needed.

## Features

- Backup multiple files and directories.
- Automatically creates the backup directory if it does not exist.
- Skips files or directories that already exist in the backup directory.
- Provides detailed logs of the backup process.

## Usage

1. Clone this repository to your local machine.
2. Open the `spec_bkp.py` script in your preferred code editor.
3. Define the paths to backup by modifying the `PATHS_TO_BACKUP` list in the script.
4. Specify the destination directory for the backup by updating the `BACKUP_DIRECTORY` variable.
5. Run the script using Python:

   ```bash
   python spec_bkp.py

Configuration
Paths to Backup: Update the PATHS_TO_BACKUP list with the absolute paths of the files and directories you want to back up.
Backup Directory: Set the BACKUP_DIRECTORY variable to the absolute path of the directory where backups should be stored.

Example
Here is an example configuration:   

PATHS_TO_BACKUP = [
    r"C:\Users\admin\.bashrc",
    r"C:\Users\admin\.gitconfig",
    r"C:\Users\admin\.config"
]

BACKUP_DIRECTORY = r"C:\Users\Admin\Backups"

Requirements
Python 3.13 or higher
shutil and pathlib modules (included in the Python standard library)
License
This project is licensed under the MIT License. See the LICENSE file for details.

Contributing
Feel free to submit issues or pull requests to improve this script. Contributions are welcome! ```