import random
import threading
import time

results = []

def compute():
    results.append(sum([random.randint(1, 100) for i in range(1000000)]))

for i in range(8):
    compute()

print('Results: %s' % results)

