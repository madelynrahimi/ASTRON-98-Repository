import numpy as np

def checkerboard():
    arr = np.eye(8, dtype=int)

    for i in range(8):
        for j in range(8):
            if i%2 == 0 and j%2 == 0:
                arr[i,j] = 1
            elif i%2 != 0 and j%2 != 0:
                arr[i,j] = 1
            elif i%2 != 0 and j%2 == 0:
                arr[i,j] = 0
    return arr

print(checkerboard())

