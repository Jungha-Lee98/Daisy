# word_list=['how', 'many', 'customer','rent', 'bicycles']
# word_list=['how', 'many', 'subscriber','rent', 'bicycles']
word_list=['how','many', 'females','rent', 'bicycles']


SQLResult = 1000

for word in word_list:
    print(word_list)
    print(word)
    if word == 'who'or word == 'what' or word =='where' or word =='when' or word =='how':
        word_list.remove(word)

    elif word == 'many':
        word_list.remove(word)


print (word_list)
'''
resultToSpeak = "SQLResult "
forloop
resultToSpeak.append(word_list[x] + " ")
# end forloop
engine.say(resultToSpeak)
'''