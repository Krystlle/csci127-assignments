def canMakeWord(letters,word):
    a = letters.split()
    b = word.split()
    a2 = a.sort()
    b2 = b.sort()
    print(a,b)
    while len(letters) == len(word):
        for letter in letters:
            if a == b:
                return True
            elif a2 == b2:
                return True
            else:
                return False
    while len(letters) != len(word):
        if True: 
            return False
        elif a2 != b2:
            return False
        else:
            return True
    
print("True means it is possible, False means it is not possible")
print("Word Possible? : ", canMakeWord("avatkkr","avatar"))    
print("Word Possible? :", canMakeWord("water","water"))
print("Word Possible? : ", canMakeWord("rfie","fire"))
print("Word Possible? : ", canMakeWord("ria","air"))
print("Word Possible? : ", canMakeWord("reaths","earth"))

