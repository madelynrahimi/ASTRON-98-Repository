
#def removeDuplicates(lis):              #Problem 4 first iteration
    #updateList = [lis[0]]
    #comparisonVal = lis[0]
    #for i in range(len(lis)):           #Range should begin at 1 as index of 0 is already considered
        #if lis[i] != comparisonVal: 
            #updateList.append[i]        #TypeError listed as append uses parenthesis and value appended should not be the index but value of lis at the idex
        #comparisonVal = lis[i]
    #return updateList


#print(removeDuplicates([1,1,2,3,4,4]))

def removeDuplicates(lis):              #Problem 4 second iteration
    updateList = [lis[0]]
    comparisonVal = lis[0]
    for i in range(1,len(lis)):           
        if lis[i] != comparisonVal: 
            updateList.append(lis[i])        
        comparisonVal = lis[i]
    return updateList


print(removeDuplicates([1,1,2,3,4,4]))
print(removeDuplicates([4,7,7,8,7,9,10,10,3]))
print(removeDuplicates([2,2,2,2,2,2]))