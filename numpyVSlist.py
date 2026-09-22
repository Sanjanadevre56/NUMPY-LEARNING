import numpy as np
import time

size= 1_000_000

list1=list(range(size))
list2=list(range(size))

stime = time.time()
data = [x + y for x , y in zip(list1 , list2)]
etime = time.time()

print(etime-stime)

l1 = np.array(size)
l2 = np.array(size)

s = time.time()
ans = l1 + l2
e=time.time()

print(e-s)
