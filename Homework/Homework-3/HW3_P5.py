def rotating_digits(numInput):
    numOutput1 = numInput % 10
    numOutput2 = numInput // 10
    if numOutput2 == 0:
        numOutputFinal = numInput
    else:
        zeroValue = (len(str(numOutput2+1)))
        numOutput3 =(10 ** zeroValue)
        numOutput4 = numOutput3 * numOutput1
        numOutputFinal = numOutput4 + numOutput2
    return numOutputFinal
    
print(rotating_digits(45557))
print(rotating_digits(7))
print(rotating_digits(6899379889))

