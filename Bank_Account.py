# Thread synchronization
# a race condition also called, happens when multiple threads access and use the same resource
# race conditions are hard to debug
# this script shows why we need thread synchronization (without Lock, instead, w/ Lock, the problem is solved!)

import time
from threading import Thread, Lock


class RobBob:
    money = 100
    mutex = Lock()

    def rob(self):
        for i in range(1_000_000):
            self.mutex.acquire()
            self.money += 10
            self.mutex.release()
        print("rob done")

    def bob(self):
        for i in range(1_000_000):
            self.mutex.acquire()
            self.money -= 10
            self.mutex.release()
        print("bob done")


RB = RobBob()
Thread(target=RB.bob, args=()).start()
Thread(target=RB.rob, args=()).start()
time.sleep(5)
print("Money in the end", RB.money)

