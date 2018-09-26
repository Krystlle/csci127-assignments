def fizzbuzz(max_value):
    i=1
    while i <= 100:
        if i == 100:
            return(max_value//15)
        elif (i%3 == 0) and (i % 5 ==0) :
            print("fizzbuzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
    
        else:
            print(i)
        i = i + 1
   
print(fizzbuzz(100))


#Worked with Jadeja Baptiste and Emily Fang
