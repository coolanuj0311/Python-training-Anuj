'''Escape Sequences:

Special characters in strings preceded by a backslash (\) for formatting (e.g., \n for newline).
Use escape sequences to represent characters that would otherwise have special meanings in strings.
Employ them for formatting text, embedding special characters, controlling output, and working with raw data.
Choose the appropriate escape sequence based on your specific needs and the context of your code.'''

#1.Single Quotes within Double Quotes:

message = "He said, \"Hello, world!\""  # Prints: He said, "Hello, world!"
print(message)

#2. Double Quotes within Single Quotes:
path = 'The file is in "Documents".'  # Prints: The file is in "Documents".
print(path)

#3. Backslashes:
windows_path = "C:\\Users\\Anuj\\Documents"  # Prints: C:\Users\Anuj\Documents
print(windows_path)

#4. Raw Strings (r-strings):
raw_string = r"C:\Windows\System32"  # Backslashes are treated literally
print(raw_string)  # Prints: C:\Windows\System32

#5. Octal Values:
beep_sound = "\007"
print(beep_sound)  # ASCII bell character (produces a beep sound)

#6. Hexadecimal Values:
heart_emoji = "\u2764"  # Unicode heart symbol
print(heart_emoji)

#7. Formatting Strings with f-strings (Python 3.6+):
name = "Anuj"
age = 23
greeting = f"Hello, {name}! You are {age} years old."
print(greeting)  # Prints: Hello, Anuj! You are 30 years old.

#8. Multiline Strings with Triple Quotes:
long_text = """This is a multiline string.
It can span multiple lines and preserve indentation.
Use it for code blocks, paragraphs, or long messages."""
print(long_text)

#9. Disabling Newlines with Backslashes:
address = "123 Main St\nAnytown, CA"  # Prints on two lines
print(address)

address = "123 Main St\\nAnytown, CA"  # Prints on one line
print(address)
    
#10. Customizing Output:

print("Progress: 30% \r", end="")  # Overwrites previous line

