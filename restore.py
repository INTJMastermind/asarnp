'''
Restores files from the backup folder back to the PMDG installation folder.
'''
import os
import shutil
from _paths import *

def restore_files():
    # If the backup folder does not exist, abort.
    if not os.path.exists(BACKUP_FOLDER):
        print("Unable to restore files. Backup folder does not exist.")
        return

    file_names = os.listdir(BACKUP_FOLDER)

    # If the backup folder is empty, abort.
    if len(file_names) == 0:
        print('No files detected in backup folder!')
    else:        
        dest_names = [SOURCE_FOLDER+file_name for file_name in file_names]
        backup_names = [BACKUP_FOLDER+file_name for file_name in file_names]
        for src, des, name in zip(backup_names, dest_names, file_names):
            shutil.copy(src, des)
            print(f'{name} successfully restored.')

if __name__ == '__main__':
    restore_files()