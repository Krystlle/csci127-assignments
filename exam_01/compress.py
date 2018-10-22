
def compress_word(w):
    vowels = ["a","e","i","o","u","A","E","I","O","U"]
 
    for w in len(s):
        if vowels in w:
            sans_vowels = w - vowels
            print(sans_vowels)
        else:
            return sans_vowels
        
#test
print(compress_word("Halloween"))