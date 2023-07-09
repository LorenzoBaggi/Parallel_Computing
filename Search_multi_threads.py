import os
from os.path import isdir, join
from threading import Lock, Thread
import time

mutex = Lock()
matches = []


def file_search(root, filename):
    print("searching in: ", root)
    child_threads = []
    for file in os.listdir(root):
        full_path = join(root, file)
        if filename in file:
            mutex.acquire()
            matches.append(full_path)
            mutex.release()
        if isdir(full_path):
            t = Thread(target=file_search, args=([full_path, filename]))
            t.start()
            child_threads.append(t)
    for t in child_threads:
        t.join()

def main():
    start = time.time()
    t = Thread(target=file_search, args=([r"C:\Users\lawre\Desktop", "nada.txt"]))
    t.start()
    t.join()
    for m in matches:
        print("Matched:", m)
        end = time.time()
        print("it took: ", end - start)
main()
