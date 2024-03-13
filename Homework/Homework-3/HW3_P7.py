def vowel_count(wordInput):
    wordInputLower = wordInput.lower()
    vowelNum = 0
    for i in range(0,len(wordInputLower)):
        if wordInputLower[i] == "a":
            vowelNum += 1
        if wordInputLower[i] == "e":
            vowelNum += 1
        if wordInputLower[i] == "i":
            vowelNum += 1
        if wordInputLower[i] == "o":
            vowelNum += 1
        if wordInputLower[i] == "u":
            vowelNum += 1
    return vowelNum

print(vowel_count("handy"))
print(vowel_count("University of California Berkeley"))
print(vowel_count("Madelyn Rahimi"))