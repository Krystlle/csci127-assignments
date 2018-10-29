import random

""" 100 tems, value 0-10, find the location of  one of the largest, then the frequency of a specific value, for (2,7) e-> # of times appears"""

list = []
highest = max(list)

largest = list[0]
for i in range (0,10):
    list.append(random.randrange(0,11,1))
    if i == highest : 
        list.index(max(values))
    
print (max(values))