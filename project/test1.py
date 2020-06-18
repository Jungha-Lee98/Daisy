sentence='How many customer rented a bike'
print(sentence)

words_list=[]

for words in sentence.split(' '):
    if words!= 'a':
        words_list.append(words)
print(words_list)

sqlquery=[]         

for loop in words_list:
    if loop == ('How' or 'Which'):
        sqlquery.append("SELECT ")

    elif loop == ('many'):
        sqlquery.append("count(*) ")
        sqlquery.append("from divvy_2015 ")

    elif loop == ('customer'):
        sqlquery.append('where usertype="customer" ')

         

print(''.join(sqlquery) + ';')