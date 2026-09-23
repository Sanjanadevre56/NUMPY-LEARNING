import numpy as np

print(np.zeros((3,3)))

print(np.ones((3,3)))

print(np.full((3,3),5))

print(np.eye(2))

print(np.arange(1,5,2))

print(np.linspace(0,1,6))

arr = np.array([1, 2, 3], dtype=np.float32) # Explicit type
print(arr.dtype) # float32
