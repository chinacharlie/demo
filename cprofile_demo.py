import random

def a():
    return sum([random.randint(1, 100) for i in range(100000)])

def b():
    for i in range(10):
        a()

def c():
    k = 0
    for i in range(100000000):
        k += i

a()
b()
c()

