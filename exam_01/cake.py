#midterm
#this doesn't output an integer or what I want it to return
def cake (A,B,u):
    
    while B > 0: 
        if A < 0 or B < 0 or u < 0:
            str = "No possible cake distribution"
            return str
        elif A > 0 or B > 0:
            return A % B == u
        
#test        
print(cake(0,0,1))
print(cake(10,20,1))

'''cake is u units right
and each person gets A/B of cake
return the number of people to invite'''