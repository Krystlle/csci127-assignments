#Krystlle Fajardo and Christopher He 
def piglatinfy(name):
    vowels= 'aeiouAEIOU'
    if name[0] in vowels:
        return name + "ay" 
    return name[1:]+name[:1]+"ay"

print(piglatinfy("hello"))
print(piglatinfy("eat"))
print(piglatinfy("test"))
print(piglatinfy("Out"))
        