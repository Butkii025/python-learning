# - Modes:
# - "r" → Read (default)
# - "w" → Write (creates new file or overwrites existing)
# - "a" → Append (adds to end of file)
# - "b" → Binary mode (e.g., images, PDFs)
# - "x" → Create (fails if file exists)

# Syntax: open(filename, mode)
f = open("mod 8/sample.txt", "r")  # 'r' = read mode

# Reading a File
f = open("sample.txt", "r")
print(f.read())        # Reads entire file
print(f.readline())    # Reads one line
print(f.readlines())   # Reads all lines into a list
f.close()



# Writing to a File
f = open("sample.txt", "w")
f.write("Hello, Vijay!\n")
f.write("This is a new line.")
f.close()



# Appending to a File
f = open("sample.txt", "a")
f.write("\nAdding more content at the end.")
f.close()



# Using with Statement (Best Practice)
with open("sample.txt", "r") as f:
    data = f.read()
    print(data)
# File closes automatically after block ends



# Working with Binary Files
with open("image.png", "rb") as f:
    content = f.read()

with open("copy.png", "wb") as f:
    f.write(content)


# delete file
import os
os.remove("sample.txt")


# Checking File Existence
import os

if os.path.exists("sample.txt"):
    print("File exists!")
else:
    print("File not found.")







