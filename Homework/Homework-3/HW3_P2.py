
def min_max_tuple(allNumList):
    minValue = allNumList[0]
    maxValue = allNumList[0]
    for i in range (0,len(allNumList)):
        if allNumList[i] < minValue:
            minValue = allNumList[i]
        
    for i in range (0,len(allNumList)):
        if allNumList[i] > maxValue:
            maxValue = allNumList[i]

    minMaxTuple = (minValue, maxValue)
    return (minMaxTuple)
   

allNumList = [2,4,5,6,8,3,1]
print (min_max_tuple(allNumList))

allNumList = [3,5,7,8,9,7,9]
print(min_max_tuple(allNumList))

allNumList = [6,8,4,5,3,4,2]
print(min_max_tuple(allNumList))

