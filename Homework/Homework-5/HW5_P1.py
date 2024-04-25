import numpy as np

arr = np.array([[1,1,1], [1,2,3], [2,2,2]])


def findEqual2(arr):
   finalVal = []
   for row in arr:
        same = True
        for i in range(len(row)):
            if row[i] != row[0]:
               same = False
        if same == True:
            finalVal.append(row)
   return finalVal

print(findEqual2(arr))