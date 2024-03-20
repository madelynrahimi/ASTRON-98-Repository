
#wholeList = []                              #Problem 3 Part 1 first iteration
#partList1 = []
#partList2 = []#
#partList3 = []
#partList4 = []
#partList5 = []
#finalList = []
#for i in range (1,26):
    #wholeList.append(i)

#for i in range(5):
    #for j in range(1,6):
        #if i == 0:
            #partList1 = [(wholeList[j-1])]              #Terminal did not denote an error, however the list printed was [[5], [10], [15], [20], [25]] which is incorrect. Appending the list instead of altering the list must be used respectiely.
        #elif i == 1:
            #partList2 = [(wholeList[j+4])]
        #elif i == 2:
            #partList3 = [(wholeList[j+9])]
        #elif i == 3:
            #partList4 = [(wholeList[j+14])]
        #elif i == 4:
            #partList5 = [(wholeList[j+19])]

#finalList = [partList1, partList2, partList3, partList4, partList5]

#print(finalList)

wholeList = []              #Problem 3 Part 1 second iteration
partList1 = []
partList2 = []
partList3 = []
partList4 = []
partList5 = []
finalList = []
for i in range (1,26):
    wholeList.append(i)

for i in range(5):
    for j in range(1,6):
        if i == 0:
            partList1.append(wholeList[j-1])
        elif i == 1:
            partList2.append(wholeList[j+4])
        elif i == 2:
            partList3.append(wholeList[j+9])
        elif i == 3:
            partList4.append(wholeList[j+14])
        elif i == 4:
            partList5.append(wholeList[j+19])

finalList = [partList1, partList2, partList3, partList4, partList5]

print(finalList)


