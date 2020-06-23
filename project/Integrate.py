# this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr
import pyttsx3
import sqlite3

engine = pyttsx3.init()
rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
engine.setProperty('rate', 100) 

# obtain audio from the microphone
r = sr.Recognizer()
# r.energy_threshold = 200
# r.dynami  c_energy_threshold = True 
with sr.Microphone(device_index=1, sample_rate=48000, chunk_size=1024) as source:
    print("Please wait. Calibrating microphone...")
    # r.energy_threshold = 5000   
    # listen for 5 seconds and create the ambient noise energy level   
    r.adjust_for_ambient_noise(source, duration=1) 
    r.energy_threshold = 1000
    r.dynamic_energy_threshold = True
    r.dynamic_energy_adjustment_damping = 0.15
    r.dynamic_energy_adjustment_ratio = 2
    r.pause_threshold = 0.8  
    # r.dynamic_energy_threshold = True  
    print("Say something!")
    audio = r.listen(source)

# recognize speech using Sphinx
try:
    print("Sphinx thinks you said " + r.recognize_sphinx(audio))
    
    all_words_list=[]
    words_list = []

    all_words_list = r.recognize_sphinx(audio).split(' ')
    print(all_words_list)

    for words in all_words_list:
        if words!= 'a':
            words_list.append(words)
    print(words_list)

# word_list=['where', 'place','that','people' 'use','the', 'most']
# word_list=['what','is','the','average','time','of','bicycles','for','members']
# word_list=['what','average','age',"female",'users']
# word_list=['how', 'many', 'customer','rent', 'bicycles']
# word_list=['how', 'many', 'subscriber','rent', 'bicycles']
# word_list=['how', 'many', 'females','rent', 'bicycles']

    sqlquery = []

    def avg():
        for i in range(len(words_list)):
            if words_list[i]=='average':
                if words_list[i+1] == 'time':
                    return('avg(tripduration) ')
                elif words_list[i+1] == 'age':
                    return('avg(tripduration) ')

    for loop in words_list:

        if loop == 'what' or loop =='which' or loop =='where' or loop == "where's" or loop == 'how':
            sqlquery.append("select ")

        elif loop == ('place' or 'station'):
            sqlquery.append("from_station_name ")
            sqlquery.append("from divvy_2015 group by from_station_name ")


        elif loop == 'average':
            sqlquery.append(avg()) 

        elif loop == 'each':
            sqlquery.append('from divvy_2015 ')
            sqlquery.append('group by ')

        elif loop == 'members' or loop == 'member':
            sqlquery.append("from divvy_2015 where usertype='Subscriber' ")
        
        elif loop == 'most' or (loop == 'almost'):
            sqlquery.append("order by count(*) desc ")
            sqlquery.append("limit 1 ")
            # sqlquery.insert(1,"count(*), ")
        
        elif loop == ('many'):
            sqlquery.append("count(*) ")

        elif loop == ('customer'):
            sqlquery.append('from divvy_2015 where usertype="Customer" ')
                
        elif loop == ('subscriber'):
            sqlquery.append('from divvy_2015 where usertype="Subscriber" ')
                
        elif loop == 'female' or (loop == 'females'):
            sqlquery.append('from divvy_2015 where gender="Female"')
            

    print(''.join(sqlquery) + ';')




    sqliteConnection = sqlite3.connect("C:\\Users\\이정하\\Documents\\Divvy_Trips_2015-Q1Q2\\Divvy.db")
    cursor =sqliteConnection.cursor()
    print("Database created and Successfully Connected to SQLite")
    sqlite_select_Query = "select sqlite_version();"
    cursor.execute(sqlite_select_Query)
    record = cursor.fetchall()
    print("SQLite Database Version is: ", record)

    sqlite_Q1 = ''.join(sqlquery) + ';'
    cursor.execute(sqlite_Q1)
    print("Success")

    for row in cursor:
        print(row)
        print("\n")

    answer_list=[]

    for word in all_words_list:
        if (word == 'how') or (word =='many') or (word == 'what') or (word == 'where') or (word == 'which'):
            continue
        else:
            answer_list.append('{0} '.format(word))
    print(answer_list)

    answer = ('{0}' +' '+ ''.join(answer_list)).format(row)

    print(answer)

    engine.say(answer)
    engine.runAndWait()

    cursor.close()

    #engine.say(r.recognize_sphinx(audio))
    #engine.runAndWait()
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))

except sqlite3.Error as error:
    print("Error while connecting to sqlite", error)

finally:
    if (sqliteConnection):
        sqliteConnection.close()
        print("The SQLite connection is closed")

