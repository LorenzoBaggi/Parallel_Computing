import time
from threading import Thread


def child():
    print("Child Thread is doing some work ... ")
    time.sleep(2)
    print("Child Thread done")


def parent():
    t = Thread(target=child, args=())
    t.start()
    print("Parent Thread is waiting ...")
    t.join() # we are waiting for the execution of the thread
    print("Parent Thread is unblocked ...")


parent()
