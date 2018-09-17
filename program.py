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
#success

#2
def init(name):
    """
    Input: name --> a string in the form "first last"
    Returns: a string in the form "F. Last" where it's a capitalized first inital 
    and capitalized last name
    """
    s=name.title()
    first=s[0]
    last=s.split()
    f_l=first + last
    return f_l

print(init("krystlle fajardo"))
#couldn't figure out how to get last name to show up, was able to get intial only, the last=s.split() part seems to detect return as a list
#and will not print anything b/c of the 'last' component. if it was only first, it would print successfully


#3

def part_pig_latin(name):
    """
    Input: A string that is a single lower case word
    Returns: that string in fake pig latin -> move the first letter of the word to the end and add "ay"
    so: "hello" --> "ellohay"
    """
    s=name[1:]+name[0]
    pig_word=s + "ay"
    return pig_word

print(part_pig_latin("krystlle"))
#success

# 4-5 from codingbat 

def make_tags(tag,word):
    result="<"+tag+">"+word+"<"+tag+">"
    return result
print(make_tags("i","oof"))

#success

def make_out_word(out,word):
    result=out[:2] + word + [out][2:]
    return result
print(make_out_word("oh","okay"))

#works on codingbat, not on here?
