words = ["Halloween","Special","apple"] 
def compress_word(w):
    vowels = ["a","e","i","o","u","A","E","I","O","U"]
    vowels = str(["a","e","i","o","u","A","E","I","O","U"])
    for w in words:
        if vowels in w:
            print(w,len(w))
            select = len(w).replace(" ")
            sans_vowels[select] = w - vowels
            print(sans_vowels)
        else:
            return sans_vowels
        
#test
print(compress_word("Halloween"))