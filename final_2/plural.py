def countPlurals(line):
    count = 0 
    a = line.split()
    print(a)
    for a in line: 
        if a == "s": 
            count = count + 1 
        else:
            count = count + 0
    return count
    
print("Plural words : ", countPlurals("through my eyes either, nor take things from me,"))
print("Pural words: ", countPlurals("The Rainbow Connection, the lovers, the dreamers and me"))

def notPossessive(line):
    count = 0 
    a = line.split()
    print(a)
    for a in line: 
        if a == "s": 
            count = count + 1
        elif a == "'":
            count = count - 1
        else:
            count + count + 0
    return count
    
print("Plural words, no apostrophe: ", notPossessive("the young man's heart's complaint,"))
print("Plural words, no apostrophe: ", notPossessive("the avatar's power of the other avatars"))

            