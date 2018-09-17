#1 
def capitalize_name(name):
    """
    input: name --> a string in the form "first last"
    output: returns a string with each of the two words capitalized
    note: this is the one we started in class
    """
    first_last=name.title()
    return (first_last)

print(capitalize_name("krystlle fajardo"))
#2
def init(name):
    """
    Input: name --> a string in the form "first last"
    Returns: a string in the form "F. Last" where it's a capitalized first inital 
    and capitalized last name
    """
    s= name.title()
    first=s[0]
    last=s.split()
    first_last=first + last
    return first_last

print(init("krystlle fajardo"))
#couldn't figure ot how to get last name to show up, was able to get intial only

#3

def part_pig_latin(name):
    """
    Input: A string that is a single lower case word
    Returns: that string in fake pig latin -> move the first letter of the word to the end and add "ay"
    so: "hello" --> "ellohay"
    """
# 4-5 from codingbat 

def make_tags(tag,word):
    result="<"+tag+">"+word+"<"+tag+">"
    return result

def make_out_word(out,word):
    result=out[:2]+word+[out][2:]
    return result