#def square(lis):                #Problem 2 Part 2 first iteration
    #squareLis = []
    #for i in range(len.lis):      #AttributeError in denoting the lenght of the defined lis, should be len(lis) for proper range
        #squareLis.append(i**2)
    #return squareLis

#print(square([2,3,4]))

#def square(lis):                #Problem 2 Part 2 second iteration
    #squareLis = []
    #for i in range(len(lis)):      #No error denoted by terminal, however, output of testcase was [0,1,4]; new list is appended with squares of the indexes instead of input lis values
        #squareLis.append(i**2)
    #return squareLis


#print(square([2,3,4]))

def square(lis):                #Problem 2 Part 2 third iteration
    squareLis = []
    for i in range(len(lis)):     
        squareLis.append(lis[i]**2)
    return squareLis

print(square([2,3,4]))
print(square([4,5,6]))
print(square([22,34,73]))