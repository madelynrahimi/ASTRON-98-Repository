wholeList = []              #Problem 3 Part 2 first iteration; no errors!
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

for i in range(5):
    if partList1[i] % 3 == 0:
        partList1[i] = "?"
    if partList2[i] % 3 == 0:
        partList2[i] = "?"
    if partList3[i] % 3 == 0:
        partList3[i] = "?"
    if partList4[i] % 3 == 0:
        partList4[i] = "?"
    if partList5[i] % 3 == 0:
        partList5[i] = "?"

finalList = [partList1, partList2, partList3, partList4, partList5]
print(finalList)
