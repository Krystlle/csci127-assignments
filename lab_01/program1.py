def greeter(name):
    return "Hello "+name+"!"

print(greeter("Stan"))
print(greeter("Ollie"));

def make_tags(tag,word)
    result="<"+tag+">"+word+"<"+tag+">"
    return result

def make_out_word(out,word):
    result=out[:2]+word+[out][2:]
    return result

#looked up how to halve syntax or 'out' symbols, python syntax splicing:
#a[start:end] # items start through end-1
#a[start:]    # items start through the rest of the array
#a[:end]      # items from the beginning through end-1
#a[:]         # a copy of the whole array

def extra_end(str):
    s=[-2:] * 3
    return s
# negative numbers in [ ] refer to last characters in string
def first_two(str):
    result=str
    return result[:2]
def first_half(str):
    length=len(str)
    first_half=str[length/2]
    return first_half
# len means length of characters in string
#can divide or manipulate a named variable

def without_end(str):
    length=len(str)
    without_end=lstr[1:length-1]
    return without_end