# all_words_list=['where','is','the', 'place','that','people' ,'use','the', 'most']
all_words_list=['what','is','the','average','time','of','bicycles','for','members']
# all_words_list=['what','is','the','average','age','of','female','users']
# all_words_list=['how', 'many', 'customer','rent', 'bicycles']
# all_words_list=['how', 'many', 'subscriber','rent', 'bicycles']
# all_words_list=['how', 'many', 'females','rent', 'bicycles']

words_list=[]

for words in all_words_list:
    if (words == 'the') or (words =='is') or (words == 'a') or (words == 'of'):
        continue
    else:
         words_list.append(words)
print(words_list)

a= 'St Dearborn'
b= 767
c= 40
d= 6000
e= 7000
f= 4000
# print(a,b,c,d,e,f)

answer_list=[]

for word in all_words_list:
    if (word == 'how') or (word =='many') or (word == 'what') or (word == 'where') or (word == 'which'):
        continue
    else:
         answer_list.append('{0} '.format(word))
print(answer_list)

# an='{0}'.format(b)

answer = ('{0}' +' '+ ''.join(answer_list)).format(b)

print(answer)
