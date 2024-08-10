"""
Copies pre-existing navigation data from PMDG directory to the backup directory.
It will automatically skip any files that already exist. This is to prevent inadvertently
copying modified files into the backup directory. If you wish to make new backups, delete the files
in the backup directory.
"""

import os
import shutil
from _paths import *

def make_backups():
    file_names = os.listdir(NAVDATA_FOLDER)
    source_names = [SOURCE_FOLDER+file_name for file_name in file_names]
    backup_names = [BACKUP_FOLDER+file_name for file_name in file_names]

    for src, des, name in zip(source_names, backup_names, file_names):
        # Skip existing files
        if os.path.exists(des):
            print(f'{name} already exists in backup folder. Skipping...') 
        # Copy files to backup.
        else:
            shutil.copy(src, des)
            print(f'{name} successfully backed up.')

if __name__ == "__main__":
    make_backups()