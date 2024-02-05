'''Key Modules:

os module: Provides basic functions for interacting with the operating system, including file and directory operations.
shutil module: Offers higher-level file operations, such as copying and moving files and directories.
pathlib module: Provides an object-oriented approach to working with file paths, making code more readable and maintainable.
Common Operations:

Listing Directories and Files:

os.listdir(path): Lists the contents of a directory.
pathlib.Path(path).iterdir(): Iterates over files and directories within a path.
Creating Directories:

os.mkdir(path): Creates a single directory.
os.makedirs(path): Creates nested directories (if they don't exist).
pathlib.Path(path).mkdir(parents=True, exist_ok=True): Creates a path, including parent directories, without errors if it exists.
Checking for Existence:

os.path.exists(path): Checks if a file or directory exists.
os.path.isfile(path): Checks if a path is a file.
os.path.isdir(path): Checks if a path is a directory.

Getting Information:

os.path.getsize(path): Gets the size of a file in bytes.
os.path.getmtime(path): Gets the last modification time of a file.

Renaming and Deleting:

os.rename(old_path, new_path): Renames a file or directory.
os.remove(path): Deletes a file.
os.rmdir(path): Deletes an empty directory.
shutil.rmtree(path): Recursively deletes a directory and its contents (use with caution).

Copying and Moving:

shutil.copy(src, dst): Copies a file.
shutil.copytree(src, dst): Recursively copies a directory and its contents.
shutil.move(src, dst): Moves a file or directory.
Working with Paths:

os.path.join(path1, path2, ...): Joins path components correctly for the OS.
os.path.basename(path): Gets the base filename from a path.
os.path.dirname(path): Gets the directory name from a path.
pathlib.Path(path).parent: Gets the parent directory of a path.

Handle paths carefully to avoid errors.
Use pathlib for a more intuitive and modern approach.
Consider context managers (e.g., with open(...)) for proper file handling.'''




import os

print(os.getcwd())

print(os.getcwdb())

os.chdir(r'E:\python training_Anuj\python training udemy\pythonProject1')

print(os.listdir())

os.rename('Test','New_One')












