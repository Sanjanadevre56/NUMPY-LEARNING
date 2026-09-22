import sys
import numpy as np 

list_data = list(range(1000))
array1 = np.array(list_data)

memo1 = sys.getsizeof(list_data)*len(list_data)
memo2 = array1.nbytes

print(memo1 ,memo2)