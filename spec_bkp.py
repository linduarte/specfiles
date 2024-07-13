"""
This script performs backups of specified files and directories
to a designated backup directory.

Usage:
1. Define the paths to backup in the PATHS_TO_BACKUP list.
2. Specify the destination directory for the backup in BACKUP_DIRECTORY.
3. Run the script.

The script will create the backup directory if it does not exist
and copy the specified files and directories into it.
"""

import shutil
from pathlib import Path


def backup_files(paths, backup_dir):
    """
    Backup the specified files/directories to the backup directory.

    Args:
    - paths (list): List of paths to backup.
    - backup_dir (str): Destination directory for the backup.
    """
    backup_dir = Path(backup_dir)

    # Create backup directory if it doesn't exist
    backup_dir.mkdir(parents=True, exist_ok=True)

    # Iterate over each path and copy the files/directories
    # to the backup directory
    for path in paths:
        path = Path(path)
        print(f"Backing up: {path}")  # Debugging statement
        if path.exists():
            # Get the base name of the file or directory
            base_name = path.name
            # Destination path for the backup
            destination_path = backup_dir / base_name
            if path.is_dir():
                # If the path is a directory, check if it already
                # exists in the backup directory
                if not destination_path.exists():
                    # If it doesn't exist, copy the entire directory
                    shutil.copytree(path, destination_path)
                    print(f"Backup created for {path} at {destination_path}")
                else:
                    print(
                        "Skipping backup for "
                        + str(path)
                        + " as it already exists in the backup directory."
                    )
            else:
                # If the path is a file, copy the file
                shutil.copy2(path, destination_path)
                print(f"Backup created for {path} at {destination_path}")
        else:
            print(f"Path {path} does not exist, skipping backup.")


if __name__ == "__main__":
    # Define the paths to backup
    PATHS_TO_BACKUP = [
        r"C:\Users\clldu\.gnupg",
        r"C:\Users\clldu\.sops",
        r"C:\Users\clldu\.bash_profile",
        r"C:\Users\clldu\.bashrc",
        r"C:\Users\clldu\.gitconfig",
        r"C:\Users\clldu\.gitconfig-personal-D",
        r"C:\Users\clldu\.gitconfig-work-D",
    ]

    # Destination directory for the backup
    BACKUP_DIRECTORY = r"C:\Users\clldu\OneDrive\Documentos\spec_files_bkp"

    # Call the backup_files function to perform the backup
    backup_files(PATHS_TO_BACKUP, BACKUP_DIRECTORY)
