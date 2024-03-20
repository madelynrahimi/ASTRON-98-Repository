#listA = [1,2,3,4,5,6,7,8,9,10]                  #Probelm 2 Part 3 first iteration
#listB = [20,21,22,23,24,25,26,27,28,29,30]

#newListA = []
#newListB = []

#for i in range(len(listA)):
    #if listA[i] % 2 == 1:
        #newListA.append[listA[i]]               #TypeError built in append function requires parenthesis to denote what to append list to
#for i in range(len(listB)):
    #if listB[i] % 2 == 1:
        #newListB.append[listB[i]]
        
#jointList = newListA + newListB
#print(jointList)

listA = [1,2,3,4,5,6,7,8,9,10]                  #Probelm 2 Part 3 first iteration
listB = [20,21,22,23,24,25,26,27,28,29,30]

newListA = []
newListB = []

for i in range(len(listA)):
    if listA[i] % 2 == 1:
        newListA.append(listA[i])              
for i in range(len(listB)):
    if listB[i] % 2 == 1:
        newListB.append(listB[i])
        
jointList = newListA + newListB
print(jointList)