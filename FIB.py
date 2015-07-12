# Project Rosalind Problem 4: FIB

import functools
import time

''' Recursive function to calculate # of rabbits alive after month'''
@functools.lru_cache(maxsize=32)          # Built in memoization, saves a ton of time 
def rabbitsAlive(month, k):

    if(month < 3):
        return 1

    return rabbitsAlive(month-2, k)*k + rabbitsAlive(month-1, k)


with open('FIB_dataset.txt', 'r') as df:
    data = df.read()
print(data)

n = data.split()[0]
k = data.split()[1]
print("n:{0} k:{1}".format(n, k))

start_time = time.clock()
print(rabbitsAlive(int(n), int(k)))
print(time.clock() - start_time)
