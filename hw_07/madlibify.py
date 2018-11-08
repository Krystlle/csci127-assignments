#Dictionary version of madlibs lab
#Worked with Kyra Abbu

import random

#choices made into dictionary

choices = {}
#commented stuff below does not work but will look into later
#choices = {
#"noun_place":["New York","California","Florida","Ohio","Massachusetts"]
#'noun_char': ["James", "Mary", "John", "Patricia", "Robert"]
#'pronoun': ["He", "She"]
#'adj_bad': ["antisocial", "cocky", "devious", "evil", "greedy"]
#'adj_good': ["loyal", "honest", "respectful", "responsible", "humble"]
#'verb': ["cry", "eat", "sleep", "dance", "walk"]
#'problem': ["diarrhea", "glutony", "procrastination"]
#'gerund'[ "stabbing", "sweating", "exploding"]
#'theme': ["sadness","death","love"]
#}

choices['noun_place'] = ['New York', 'California', 'Florida','Ohio',"Massachusetts"]
choices['noun_char'] = ["James", "Mary", "John", "Patricia", "Robert"]
choices['pronoun'] = ["He", "She"]
choices['adj_bad'] = ["antisocial", "cocky", "devious", "evil", "greedy"]
choices['adj_good'] = ["loyal", "honest", "respectful", "responsible", "humble"]
choices['verb'] = ["cry", "eat", "sleep", "dance", "walk"]
choices['problem'] = ["diarrhea", "glutony", "procrastination"]
choices['gerund'] = [ "stabbing", "sweating", "exploding"]
choices['theme'] = ["sadness","death","love"]


story = """The story unfolds in <SETTING> . The text revolves around <CHARACTER> .
 <PRONOUN> is <BADTRAIT> but <GOODTRAIT> . <CHARACTER2> wanted to <VERB> .
 The problem is <PROBLEM> . <CHARACTER3> ovecome this by <GERUND> . Readers learn <MESSAGE> ."""

result_char = " "
 #result_pro = " "
def pronoun_find(value):
         #print(value)
         #statement below does not work the same as valid statements (?)
         #if value == "John" or "James" or "Robert":  
                 #select = pronoun[0]
         if value == "John" or value == "James" or value == "Robert":  
                 select = choices['pronoun'][0]
         else:
                 select = choices['pronoun'][1]
         return select
     
def madlibs(sentence):
     sentence = sentence.split()
     for element in sentence:
         if element == "<SETTING>":
             select = random.choice(choices['noun_place'])
             replacement = sentence.index(element)
             sentence[replacement] = select
             #print(sentence)
             #result = sentence
         elif element == "<CHARACTER>":
             select_name = random.choice(choices['noun_char'])
             replacement = sentence.index(element)
             sentence[replacement] = select_name
             result_char = select_name
             #print(sentence)           
             continue
         elif element == "<PRONOUN>":
             answer = pronoun_find(result_char) #call another function
             replacement = sentence.index(element)
             sentence[replacement] = answer
             continue
         elif element == "<BADTRAIT>":
             select = random.choice(choices['adj_bad'])
             replacement = sentence.index(element)
             sentence[replacement] = select
             #print(sentence)
             continue
         elif element == "<GOODTRAIT>":
             select = random.choice(choices['adj_good'])
             replacement = sentence.index(element)
             sentence[replacement] = select
             #print(sentence)
             continue
         elif element == "<CHARACTER2>":
             replacement = sentence.index(element)
             sentence[replacement] = result_char
             #print(sentence)
             continue
         elif element == "<VERB>":
             select = random.choice(choices['verb'])
             replacement = sentence.index(element)
             sentence[replacement] = select
             #print(sentence)
             continue
         elif element == "<PROBLEM>":
             select = random.choice(choices['problem'])
             replacement = sentence.index(element)
             sentence[replacement] = select
             #print(sentence)
             continue
         elif element == "<CHARACTER3>":
             replacement = sentence.index(element)
             sentence[replacement] = result_char
             #print(sentence)
             continue
         elif element == "<GERUND>":
             select = random.choice(choices['gerund'])
             replacement = sentence.index(element)
             sentence[replacement] = select
             #print(sentence)
             continue
         elif element == "<MESSAGE>":
             select = random.choice(choices['theme'])
             replacement = sentence.index(element)
             sentence[replacement] = select
             sentence = str(" ".join(sentence))
             print(sentence)
             return

 #test
madlibs(story)
         
        
    
