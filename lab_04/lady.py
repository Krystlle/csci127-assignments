
def happyLadybugs(n,b):


    for i in b:
        if i != "_" :
            return "NO"
        elif n == 0:
            return "NO"
        elif len(b) < 2:
            return "NO"
        elif b[0] == b[1]:
            return "YES"
    for i in range(0,(len(b) - 1)):
        if b[i] != b[i-1] and b[i] != [i+1]: #check if the letters match the ones beside each other 
            return "NO"
        else:
            return "YES"
        
def count_bugs(b):
    bugs = {}
    for i in b:
        if i in b: 
            bugs[i] = 0 
            bugs[i] = bugs[i] + 1
        else:
            bugs[i] = bugs[i] + 0 
return bugs
            
b = input()
print(happyLadybugs(n,b))

#issue with 'return' indentation to getting count to work 
#count = [] 

#for i in b:
 #   if i is "YES":
  #      count = counter + 1 
#return count

