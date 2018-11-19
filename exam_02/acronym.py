#1 - Acronymn
list = ["laugh out loud","read the fine manual", "in my humble opinion", "too much information"]
new_list = []
result = ""

def make_acronym(w):
    for words in range(len(list)):
        words = words.split()
        single_word = w.split()
        if w in words[:1]:
            select_letter = [w[0] for word in list]
            combine_letters = select_letter.join("")
            add_letters = new_list.append()
            return combine_letters(add_letters)
         elif w in words[:2]:
            select_letter = [w[0] for word in list]
            combine_letters = select_letter.join("")
            add_letters = new_list.append()
            return combine_letters(add_letters)
        elif w in words[:3]:
            select_letter = [w[0] for word in list]
            combine_letters = select_letter.join("")
            add_letters = new_list.append()
            return combine_letters(add_letters)
        elif w in words[:4]:
            select_letter = [w[0] for word in list]
            combine_letters = select_letter.join("")
            add_letters = new_list.append()
            return combine_letters(add_letters)
        else:
            return result
        
print(make_acronym)
            

        