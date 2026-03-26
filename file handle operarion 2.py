import os
with open("my_file.txt", "w") as file:
    file.write("Hello! I am Musa, THE GREATEST OF ALL TIME.\n")
with open("my_file.txt", "r") as file:
    content = file.read()
    words = content.split()
    print("Words in file:", words)
if os.path.exists("My_File.txt"):
    print("My_File.txt exists")
else:
    print("My_File.txt does not exist")
    with open("My_File.txt", "w") as file:
        file.write("Hello! I am Musa, a student who loves learning.\n")
if os.path.exists("sample_doc.txt"):
    os.remove("sample_doc.txt")
    print("sample_doc.txt deleted")
else:
    print("sample_doc.txt does not exist")