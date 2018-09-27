def seq(n):
    count = 0
    while (n != 1):
        if (n % 2==0):
           n == n // 2
           count+=1
        else:
            n == n * 3 +1
            count+=1
            print(n)
        return "this is the number of steps" + str(count)
print(seq(10))
#Krystlle Fajardo with Madison Chen, Nursima Donuk
#will fix 
            