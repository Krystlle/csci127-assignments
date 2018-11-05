def countApplesAndOranges(s, t, a, b, apples, oranges):
    
    countApple = 0
    countOrange = 0

    for x in apples:
        if  (x + a) >= s and (x + b) <= t:
            countApple += 1
    
    for x in oranges:
        if (x + a) >= s and (x + b) <= t:
            countOrange += 1 

#int(input())

print(countApple)
print(countOrange)