def build_word_counts(words):
    d={}
    for word in words.split():
        d.setdefault(word,0)
        d[word]=d[word]+1
    return d

def clean_data(s):
    result=""
    for letter in s:
        if letter in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
            result = result + letter.lower()
        else:
            result = result + " "
    return result


filename="/home/krystlle/Documents/moby-small.txt"
f = open(filename)
s = f.read()
words_uncleaned = build_word_counts(s)
print(words_uncleaned)
print("-------------------")
print(s)
f.close()
print("-------")

f = open(filename)
s = f.readline()
print(s)
s = f.readline()
print(s)
f.close()
print('------')
f = open(filename)
for line in f.readlines():
    print(line)
print('------')
common_words = []


d=build_word_counts(s)
print(d(filename))

common_words = [ [k,words[k]] for k in words if words[k] > 50 ]
cw = common_words
print(cw)

add_values= [k for k in range(0,len(s)-1)]
print(add_values)