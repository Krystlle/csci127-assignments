def addLine(d,line):
    d = {}
    line = line.lower()
    words = line.split("")
    print(words)
    theRange = words.range(0, len(words))
    print(line)
    for letter in theRange:
        if letter in words[letter] == words[letter - 1] and letters in words[letter] == words[letter+1]:
        d.setdefault(0,line)
        d[words[letter]].append(words)
            return d 
        else:
            return d

#3.3
def spellcheck(d,word):
    word = word.lower()
        if word is in d:
            return True
        else:
            return False

    
print(addLine(d, "Four for you, Glenn Coco! You go, Glenn Coco!"))
print(addLine(d,"I will travel across the land, searching far and wide. Each Pokemon to understand the power that's inside!"))