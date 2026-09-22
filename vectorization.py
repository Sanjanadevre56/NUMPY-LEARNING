#NumPy avoids loops by applying operations to entire arrays at once using SIMD
# (Single Instruction, Multiple Data) and other low-level optimizations. SIMD is a
# CPU-level optimization provided by modern processors

import numpy as np

array1 = np.array([[1,2,3,4,5]])

array1 = array1**2

print(array1)