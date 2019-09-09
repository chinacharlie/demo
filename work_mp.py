import random
import multiprocessing

g = 0

def compute(n):
    global g
    g += 1
    print('g = %d' % g)
    return sum([random.randint(1, 100) for i in range(1000000)])


pool = multiprocessing.Pool(4)
print('Results: %s' % pool.map(compute, range(8)))

