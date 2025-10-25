"""
   1. Create and Write: Create a new file and write your name to it.
   2. Read Entire File: Read and display the entire content of a file.
   3. Append Text: Append a line of text to an existing file.
   4. Count Lines: Count the number of lines in a file.
   5. Count Words: Count the number of words in a file.
   6. Count Characters: Count the number of characters in a file.
   7. Copy File: Create a copy of a file with a different name.
   8. Display with Line Numbers: Display file content with line numbers.
   9. Search Word: Check if a specific word exists in a file.
   10. Create Multiple Files: Create 5 files with names file1.txt to file5.txt.

"""
"""
f = open("files/files.txt", "w+")
f.write("Anasbek")
f.close()

"""

f = open("files/files.txt", "r+")

lines = f.readline()
print(len(lines))
f.seek(0)
text = f.read()

print(len(text.split()))


f.close()


