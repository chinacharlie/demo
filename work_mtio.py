import random
import threading
import time

results = []

def sleep_or_io():
    time.sleep(5)
    results.append(0)


workers = [threading.Thread(target=sleep_or_io) for x in range(8)]
for worker in workers:
    worker.start()
for worker in workers:
    worker.join()

print('Results: %s' % results)

