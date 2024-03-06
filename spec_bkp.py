import os
import shutil


def backup_files(paths_to_backup, backup_directory):
    """
    Backup the specified files/directories to the backup directory.

    Args:
    - paths_to_backup (list): List of paths to backup.
    - backup_directory (str): Destination directory for the backup.
    """
    # Create backup directory if it doesn't exist
    if not os.path.exists(backup_directory):
        os.makedirs(backup_directory)

    # Iterate over each path and copy the files/directories to the backup directory
    for path in paths_to_backup:
        print(f"Backing up: {path}")  # Debugging statement
        if os.path.exists(path):
            # Get the base name of the file or directory
            base_name = os.path.basename(path)
            # Destination path for the backup
            destination_path = os.path.join(backup_directory, base_name)
            if os.path.isdir(path):
                # If the path is a directory, check if it already exists in the backup directory
                if not os.path.exists(destination_path):
                    # If it doesn't exist, copy the entire directory
                    shutil.copytree(path, destination_path)
                    print(f"Backup created for {path} at {destination_path}")
                else:
                    print(
                        f"Skipping backup for {path} as it already exists in the backup directory."
                    )
            else:
                # If the path is a file, copy the file
                shutil.copy2(path, destination_path)
                print(f"Backup created for {path} at {destination_path}")
        else:
            print(f"Path {path} does not exist, skipping backup.")


if __name__ == "__main__":
    # List of paths to backup
    paths_to_backup = [
        r"C:\Users\clldu\.bashrc",
        r"C:\Users\clldu\.gitconfig",
        r"C:\Users\clldu\.gitconfig-personal",
        r"C:\Users\clldu\.gitconfig-work",
        r"C:\Users\clldu\AppData\Roaming\jupyter\kernels",
    ]

    # Destination directory for the backup
    backup_directory = r"C:\Users\clldu\OneDrive\Documentos\spec_files_bkp"

    # Call the backup_files function to perform the backup
    backup_files(paths_to_backup, backup_directory)
