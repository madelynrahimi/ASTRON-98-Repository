import numpy as np

np.random.seed(12345)
a = np.random.randint(1,50, (4,5))

def sorting(a):
    aNew = np.sort(a, axis=0)
    return aNew 

print(sorting(a))