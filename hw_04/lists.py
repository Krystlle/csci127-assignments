#asked Stacey Li for help on #3 and #5

import random


def build_random_list(size,max_value):
    """
    Parameters:
      size : the number of elements in the lsit
      max_value : the max random value to put in the list
    """
    l = [] # start with an empty list

    # make a loop that counts up to size
    i = 0
    while i < size:
        l.append(random.randrange(0,max_value))
        # we could have written this instead of the above line:
        # l = l + [random.randrange(0,max_value)]
        i = i + 1
    return l
l = build_random_list(15,100)
print(l)

#1

def locate(l,value):
    """
    This routine should accept a list
    as the first parameter and a value
    for the second. The function will
    look for value in the list
    and return its index.
    Return -1 if value isn’t in the list.
    """
    l = []
    i = 0

    while locate(l,value):
        l.append(random.range(i,value))
        if i in l:
            print(l)
        else:
            print(-1)
        l = locate(l,7)     
    return l

print(l)

#2
def count(l,value):
    """
    This routine should accept a
    list as the first parameter
    and a value for the second.
    It should return the number
    of times value appears in the list l
    """
#3
def reverse(l):
    """
    This function should accept a list as its parameter.
    It will build and return a new list which has the
    same elements as the original but with the
    values reversed.
    """
 search = len(l) - 1
    l2 = []
    while search != -1:
        l2.append(l(search))
        search -= 1
    return l2
#4
def isIncreasing(l):
    """
    This function should accept a list as its parameter.
    It will return True if the list is strictly increasing,
    that is starting with the first element, each successive
    element is greater than the previous. For example, the list 1,5,10,11,13
    is increasing while 1,5,3,6 and 1,4,4,6 are not.
    """
    
#5
def palindrome(l):
    """
    This function should return True if the list represents a palindrome
    and False otherwise. A list is a palindrome if it has the same elements
    left to right as it does right to left.

    """