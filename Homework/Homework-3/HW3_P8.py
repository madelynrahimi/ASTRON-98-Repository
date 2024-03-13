def digital_root(numInput):
    stringInput= str(numInput)
    digitalRootVal = 0
    for i in range (0,len(stringInput)):
        digitalRootVal = digitalRootVal + int(stringInput[i])
    return digitalRootVal

print(digital_root(4588))
print(digital_root(688934))
print(digital_root(32490))
