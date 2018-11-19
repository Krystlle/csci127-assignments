#2 - RLE

d = {'abbaaacddaaa': ,'abcd':, 'abba':}
d2 = {}
def encode(w):
    string = d.keys()
    s = string.split("") #split key phrase into characters, e.g. 'abc' is 'a', 'b', 'c'
    [i[0] for word in string]
        d.setdefault(s[i],[])
        d[s[i]].append(s[i+1])
    return d        

def count_letters(w):
    d={}
    for i in string.split():
        d.setdefault(string,0)
        d[string]=d[string]+1
    return d

print(encode(count_letters))