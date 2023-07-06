# threads run in the same memory space (different from processes)
# threads are lightweight, resource light
# process gives you more isolation
# in python you don't have the limitation of the GIL w/ processes
# with spawn it is lower to start but consumes less memory
import multiprocessing
from multiprocessing import Process


def do_work():
    print("Starting to work")
    i = 0
    for _ in range(20_000_000):
        i = i + 1
    print("Finished to work")


if __name__ == "__main__":
    multiprocessing.set_start_method('spawn')
    for _ in range(5):
        p = Process(target=do_work, args=())
        p.start()
        # this uses all our CPU, instead, before, with threads, we were using just one processor
