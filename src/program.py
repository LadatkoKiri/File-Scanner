import os

path = input("Enter path to folder: ")

files = os.listdir(path)

print("Papa's files:")
for f in files:
    print(f)

print("Number of files:", len(files))

search = input("Enter a file name to search for: ")

if search in files:
    print("File found")
else:
    print("File not found")