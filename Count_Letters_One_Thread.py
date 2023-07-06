# MEMORY SHARING
# Inter Process communication
# message passing (two threads sending messages to each other)
# shared memory (two friends, instead of talking, are exchanging information looking at a "blackboard".
# the advantage here, wrt to message passing, is efficiency
# w/ threads memory sharing is helpful

import json
import urllib.request
import time
from urllib.error import HTTPError



def count_letters(url, frequency):
    response = urllib.request.urlopen(url)
    txt = str(response)
    for l in txt:
        letter = l.lower()
        if letter in frequency:
            frequency[letter] += 1


def main():
    frequency = {}
    for c in "abcdefghijklmnopqrstuvwxyz":
        frequency[c] = 0
    start = time.time()
    for i in range(1, 100):
        try:
            count_letters(f"https://www.rfc-editor.org/rfc/rfc{i}.txt", frequency)
        except HTTPError as e:
            print("Error occured")
            print(e)
    end = time.time()
    print(json.dumps(frequency, indent=4))
    print("Done, time taken = ", end - start)

main()

