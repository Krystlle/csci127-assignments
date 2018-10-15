l=[1,2,3,4,5,6,7,8]

def filteroff(l):
    new_list = []
    for i in l:
        if 1 % 2 == 1:
            new_list.append(i)
        return new_list
    
print(filter(l))

#it doesn't work b/c of arguments athough i think the general gist is ok

l = [4,2,5,3,5]
def mapsquare(l):
    new_list = []
    for i in l:
        sqrt = i** 2
        new_list.append(i)
    return new_list

        
        

print(mapsquare(l))

#curious about these formats though: 
#mapsquaring = [i ** 2 for i in list]

