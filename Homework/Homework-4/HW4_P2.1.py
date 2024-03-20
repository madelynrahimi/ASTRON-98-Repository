#numList = []                #Problem 2 Part 1 first iteration
#for i in range (0,51):
    #numList += i            #TypeError on line 3, invalid to update numList in such fashion, must append list to update 
#print (numList)

numList = []                #Problem 2 Part 1 second iteration
for i in range (0,51):
    numList.append(i)            
print (numList)

