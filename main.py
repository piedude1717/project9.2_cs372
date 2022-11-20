import threading
import time

#place ur desired ranges in the rangess variable
rangess = [
    [10, 20],
    [1, 5],
    [70, 80],
    [27, 92],
    [0, 16]
]
def range_calc(start, end):
    results.append(sum(range(start, end+1)))





THREAD_COUNT = len(rangess)
threads = []
results = []
for i in range(THREAD_COUNT):




    t = threading.Thread(target=range_calc, args=(rangess[i][0], rangess[i][1]))
    t.start()

# Join all the threads back up to this, the main thread. The main thread
# will block on the join() call until the thread is complete. If the
# thread is already complete, the join() returns immediately.

for t in threads:
    t.join()

print(results)
print(sum(results))

