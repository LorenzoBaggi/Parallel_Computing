from threading import Barrier, Thread
import time


barrier = Barrier(2)


def wait_on_barrier(name, time_to_sleep):
    for i in range(10):
        print(name, "running")
        time.sleep(time_to_sleep)
        print(name, "waiting on barrier")
        barrier.wait()
    print(name, "finished")


red = Thread(target=wait_on_barrier, args=("red", 4))
blue = Thread(target=wait_on_barrier, args=("blue", 8))
red.start()
blue.start()

