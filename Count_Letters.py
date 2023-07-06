import json
import urllib.request
import time
from threading import Thread

# but be careful, here, we have thread synchronization!

finished_count = 0


def count_letters(url, frequency):
    response = urllib.request.urlopen(url)
    txt = str(response)
    for l in txt:
        letter = l.lower()
        if letter in frequency:
            frequency[letter] += 1
    global finished_count
    finished_count += 1


def main():
    frequency = {}
    for c in "abcdefghijklmnopqrstuvwxyz":
        frequency[c] = 0
    start = time.time()
    for i in range(1, 100):
        Thread(target=count_letters, args=(f"https://www.rfc-editor.org/rfc/rfc{i}.txt", frequency)).start()
    while finished_count < 20:
        time.sleep(0.5)
    end = time.time()
    print(json.dumps(frequency, indent=4))
    print("Done, time taken = ", end - start)

main()