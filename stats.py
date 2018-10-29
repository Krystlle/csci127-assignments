from random import randrange

l = []
def build_list(items,max_value):
    i = 0
    for i in range (100):
        l.append(randrange(1,100))
    return l
print(l)
    

def index_largest(l):
    li = 0
    for i in range(1,len(l)):
        if l[i] > l [i]:
            li = i
    return li

def freq(l,value):
    freq_list= []
    for i in l:
        count = freq_list.count(max(items))
        count.append()
    return count

#doesn't work :
def mode(l):
    for i in range(len(l)):
        if i in l:
           count += 1
        else:
           count = 1
    return 

li = index_largest(l)
print(build_list(li,l[li]))
print(freq(count))
print(mode(l))
