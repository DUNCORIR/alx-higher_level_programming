0x0B. Python - Input/Output

Reading and Writing Files (Python Docs)

open(): Opens a file in different modes, like reading ('r'), writing ('w'), or appending ('a').
read(): Reads the entire file or a specific number of characters from the file.
write(): Writes a string to the file.
with statement: Handles automatic file closing after the block ends.
Key Takeaways:

Always use with to ensure that files are properly closed.
Understand how file modes work (r, w, a, rb, etc.).
Learn how to handle reading, writing, and appending data.

 Predefined Clean-up Actions (Python Docs)

The importance of the with statement, which simplifies error handling and ensures that resources (like files) are cleaned up properly. This is essential when working with files, network connections, or any resource that needs proper management.

Key Takeaways:

Learn how with is used for managing resources.
Understand that with makes your code cleaner by eliminating the need for explicit closing.

Files
Reading files line-by-line: Useful when working with large files.
Reading files in chunks: For memory-efficient file reading.
Writing binary files: Until "11.4 Binary Files."
# Reading a file line by line
with open('file.txt', 'r') as file:
    for line in file:
        print(line.strip())

JSON Encoder and Decoder (Python Docs)
Key Functions:

json.dump(): Write Python objects to a file in JSON format.
json.dumps(): Convert Python objects to a JSON string.
json.load(): Parse JSON from a file into a Python object.
json.loads(): Parse a JSON string into a Python object.

Reading/Writing Files
# Writing data to a file
with open('output.txt', 'w') as file:
    file.write("Hello, world!")

Automate the Boring Stuff with Python
File Modes: Understand different file modes (r, w, a, etc.) and how they influence file operations.
Using with: Always use the with statement to manage files automatically and ensure they are closed properly.
Reading/Writing Files: Learn different methods of reading and writing files—whether in chunks, line by line, or all at once.
Binary vs Text Mode: Learn the difference between reading files as text vs binary and when to use each.
JSON Serialization: Master working with JSON in Python, especially using json.dump() and json.load().
