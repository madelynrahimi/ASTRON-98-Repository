import numpy as np

myarr = np.array(['python', 'is', 'cool!'])
newList = []

def spaceBetween(myarr):
    for i in range(len(myarr)):
       newWord = ' '.join(myarr[i])
       newList.append(newWord)
    return newList
print(spaceBetween(myarr))