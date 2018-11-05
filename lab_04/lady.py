
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
            
b = input()
print(happyLadybugs(n,b))

#issue with 'return' indentation to getting count to work 
#count = [] 

#for i in b:
 #   if i is "YES":
  #      count = counter + 1 
#return count

