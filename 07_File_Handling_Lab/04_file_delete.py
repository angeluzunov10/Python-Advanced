import os
try:
    os.remove("my_first_file.txt")
    print("File was successfully removed")
except FileNotFoundError:
    print("File not found! File could be removed already.")