# Java, C++, GO are different wrt Python
# let's say we have 4 CPUs free to execute 4 threads. when we have one thread executed by one
# CPU, the python interpreter will lock the remaining threads of that program.
# only one thread at a time is executed on any processor: it's the GIL
# hence there is no point of using threads to speed the program when the program is CPU bound
# (usually, when there are a lot of calculations to be done, like, GAMING / GRAPHING / ENCRYPTION / VIDEO
# AUDIO / ML ...)
# the opposite of a CPU bound process is a I/O process (file transfer, webpage crawler, web servers)
# to speed up a CPU BOUND, use multi-processes.
import time
from threading import Thread


def do_work():
    print("Starting to work")
    i = 0
    for _ in range(20_000_000):
        i = i + 1
    print("Finished to work")


for _ in range(5):
    t = Thread(target=do_work, args=())
    t.start()
    # while a thread goes to sleep, one another arrives in, so, it looks like they are executing in parallel
    # in reality we are using just one at a time due to GIL, so, just one processor 