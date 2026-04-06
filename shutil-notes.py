# 📝 OS and File Shell Operations: Copying, Moving, and Deleting

import shutil
import os

# 1. Why use shutil?
# Because the 'os' module is for low-level (creating folders),
# while 'shutil' is for high-level (copying entire folder structures).

# 2. Copying Files and Folders
# shutil.copy(source, destination) # Copies file + contents
# shutil.copy2(source, destination) # Copies file + metadata (times, owner)
# shutil.copytree(source_dir, dest_dir) # Copies an entire directory

# 3. Moving Files and Folders
# shutil.move(source, destination) # Works like rename/move

# 4. Deleting Entire Folders (High risk!)
# Be careful! It will delete everything inside!
# shutil.rmtree(folder_name) # Recursively delete directory tree

# 5. Disk Usage and Management
# Checking free space
total, used, free = shutil.disk_usage("/")
print("Total Disk Space:", total // (2**30), "GB")
print("Used Disk Space:", used // (2**30), "GB")
print("Free Disk Space:", free // (2**30), "GB")

# 6. Archiving (Creating .zip or .tar files)
# shutil.make_archive("my_backup", "zip", "source_folder")
# shutil.unpack_archive("my_backup.zip", "extracted_folder")

# Summary Table
"""
| Method            | Purpose                                        |
|-------------------|------------------------------------------------|
| shutil.copy()     | Copy a single file                             |
| shutil.copytree() | Copy an ENTIRE directory                       |
| shutil.move()     | Rename or relocate file/folders                |
| shutil.rmtree()   | Use with EXTREME caution (Delete folder)!      |
| shutil.make_archive()| Create a ZIP or TAR backup of anything       |
| shutil.disk_usage()| Find out how much space you have left           |
"""
