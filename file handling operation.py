file = open("sample.txt", "r")
content = file.read()
print("First 10 characters:", content[:10])
file.seek(0)
print("First line:", file.readline().strip())
file.seek(0)
print("First 4 lines:")
for i in range(4):
    print(file.readline().strip())
file.seek(0)
print("\nAll lines:")
for line in file:
    print(line.strip())
file.close()