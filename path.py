import os

# Example /Users/Desktop/env
PATH = input("Enter path: ")
file_count = 0
dir_count = 0
for root, dirs, files in os.walk(PATH):
    for directories in dirs:
        dir_count += 1
    for Files in files:
        file_count += 1

print("Number of Files: ", file_count)
print("Number of Directories: ", dir_count)
print("Total: ", (dir_count + file_count))