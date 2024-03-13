def min_for_loop(inputList):
    minValue = inputList[0]
    for i in range(1,len(inputList)):
        if inputList[i] < minValue:
            minValue = inputList[i]
    return minValue
    
def max_for_loop(inputList):
    maxValue = inputList[0]
    for i in range(1,len(inputList)):
        if inputList[i] > maxValue:
            maxValue = inputList[i]
    return maxValue
    
def min_while_loop(inputList):
    i = 1
    minValue = inputList[0]
    while i <len(inputList):
        if inputList[i] < minValue:
            minValue = inputList[i]
        i += 1
    return minValue

def max_while_loop(inputList):
    i = 1
    maxValue = inputList[0]
    while i < len(inputList):
        if inputList[i] >maxValue:
            maxValue = inputList[i]
        i += 1  
    return maxValue

inputList = [2,4,5,7,8,1]
print(min_for_loop(inputList))
print(max_for_loop(inputList))
print(min_while_loop(inputList))
print(max_while_loop(inputList))

inputList = [4,6,8,9,0,1]
print(min_for_loop(inputList))
print(max_for_loop(inputList))
print(min_while_loop(inputList))
print(max_while_loop(inputList))

inputList = [5,8,10,3,-1,-4]
print(min_for_loop(inputList))
print(max_for_loop(inputList))
print(min_while_loop(inputList))
print(max_while_loop(inputList))