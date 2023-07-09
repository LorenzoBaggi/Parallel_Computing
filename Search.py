import os
from os.path import isdir, join
import time

matches = []


def file_search(root, filename):
    print("searching in: ", root)
    for file in os.listdir(root):
        full_path = join(root, file)
        if filename in file:
            matches.append(full_path)
        if isdir(full_path):
            file_search(full_path, filename) # recursive call


def main():
    start = time.time()
    file_search(r"C:\Users\lawre\Desktop", "nada.txt")
    for m in matches:
        print("Matched:", m)
        end = time.time()
        print("it took: ", end - start)
main()



