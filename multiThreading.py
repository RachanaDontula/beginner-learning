"""
breaking a big problem into parts,
each part is called thread in programming
Multitasking:  at a time multiple applications can be run.
Multitasking can be done using multi threading.

By using threads, multiple functions can be run simultaneously.

"""
from time import sleep
from threading import *


class Hello(Thread):

    def run(self):
        for i in range(5):
            print("hello")
            sleep(1)  # used for huge code execution will be neat.


class Hi(Thread):
    def run(self):
        for j in range(5):
            print("hi")
            sleep(1)


obj1 = Hello()
obj2 = Hi()
obj1.start()
sleep(0.2)  # avoid collision
obj2.start()

obj1.join()  # join will execute first then print statements.
obj2.join()
print("bye")