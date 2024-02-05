
'''
1. Opening and Closing Files:

open(filename, mode): Opens a file and returns a file object.
filename: The name or path of the file to open.
mode: Specifies the mode in which to open the file:
"r": Read mode (default).
"w": Write mode (overwrites existing files).
"a": Append mode (adds to the end of existing files).
"r+": Read and write mode.
"w+": Write and read mode (overwrites existing files).
"a+": Append and read mode.
"b": Binary mode (for binary files like images or audio).
close(): Closes the file, releasing resources and ensuring data is written to disk.
2. Reading from Files:

read(size): Reads up to size bytes from the file. If size is omitted, reads the entire file.
readline(): Reads a single line from the file.
readlines(): Reads all lines from the file and returns them as a list of strings.
3. Writing to Files:

write(string): Writes a string to the file.
writelines(lines): Writes a list of strings to the file, each string on a separate line.
4. Other File Methods:

tell(): Returns the current position of the file pointer.
seek(offset, whence): Moves the file pointer to a specific position.
truncate(size): Truncates the file to a specified size.
isatty(): Returns True if the file is connected to a terminal device, False otherwise.
Key Points:

Always use close() to properly close files after working with them.
Choose the appropriate mode ("r", "w", "a", etc.) depending on your intended actions.
For binary files, use the "b" mode.
Use tell() and seek() for random access to file content.
Example:

'''
with open("my_file.txt","r") as file:
    contents=file.read()
    print(contents)

