# import SR,pyttsx,sqlite3
import speech_recognition as sr
import pyttsx3
import sqlite3

# import pyttsx engine and set speech rate 
engine = pyttsx3.init()
rate = engine.getProperty('rate')               
engine.setProperty('rate', 130)
 
# start conversation 
engine.say("Hi, I'm Daisy")
engine.runAndWait()
print("Hi, I'm Daisy")

# obtain audio from the microphone
r = sr.Recognizer()

# set Microphone instances
with sr.Microphone(device_index=1, chunk_size=1024, sample_rate=48000) as source:
    print("Please wait. Calibrating microphone...") 
    r.adjust_for_ambient_noise(source, duration=1) 
    r.energy_threshold = 500
    r.dynamic_energy_threshold = True
    r.dynamic_energy_adjustment_damping = 0.15
    r.dynamic_energy_adjustment_ratio = 1.5
    r.pause_threshold = 0.8
    
    # speak to user 'say something!'
    engine.say("Say something!")
    engine.runAndWait()
    print("Say something!")

    # get user's speech 
    audio = r.listen(source)

try:
    # recognize speech using Sphinx
    print("Sphinx thinks you said " + r.recognize_sphinx(audio))
    
    all_words_list=[] # all words list 
    words_list = [] # words list except articles and be_verb 

    # split sentence into words
    all_words_list = r.recognize_sphinx(audio).split(' ')
    print(all_words_list)

    # remove articles an be_verbs
    for words in all_words_list:
        if (words == 'the') or (words =='is') or (words == 'a') or (words == 'of') or (words == 'an'):
            continue
        else:
            words_list.append(words)
    print(words_list)

    # when use avg function it run
    def avg():
        for i in range(len(words_list)):
            if words_list[i]=='average':
                if words_list[i+1] == 'time':
                    return('avg(tripduration) ')
                elif words_list[i+1] == 'age':
                    return('avg(tripduration) ')
    

    sqlquery = [] # sql_sentence's words list

    # translate words into sql query
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
        
        elif loop == ('many'):
            sqlquery.append("count(*) ")

        elif loop == ('customer'):
            sqlquery.append('from divvy_2015 where usertype="Customer" ')
                
        elif loop == 'subscriber' or loop == 'subscribers':
            sqlquery.append('from divvy_2015 where usertype="Subscriber" ')
                
        elif loop == 'female' or (loop == 'females'):
            sqlquery.append('from divvy_2015 where gender="Female" ')
        
        
    strsqlquery = ''.join(sqlquery) + ';'
    print(strsqlquery)

    # connect database,sqlite3
    sqliteConnection = sqlite3.connect("C:\\Users\\USER\\divvy.db")
    cursor =sqliteConnection.cursor()
    print("Database created and Successfully Connected to SQLite")

    # execute sql query
    cursor.execute(strsqlquery)

    # cursor.fetchall(), print answer what user wants
    for row in cursor:
        print(row)
        print("\n")

    answer_list=[] # words list to use answer

    # remove question mark and print answer sentence
    for word in all_words_list:
        if (word == 'how') or (word =='many') or (word == 'what') or (word == 'where') or (word == 'which'):
            continue
        else:
            answer_list.append('{0} '.format(word))
    print(answer_list)
    
    # speak answer to user
    answer = ('{0}' +' '+ ''.join(answer_list)).format(row)
    print(answer)
    engine.say(answer)
    engine.runAndWait()

    # close cursor
    cursor.close()

except sr.UnknownValueError:
    print("Sphinx could not understand audio")
    engine.say("Sphinx could not understand audio.Could you tell me question again?")
    engine.runAndWait()

except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))
    engine.say("I can't understand your question. Could you tell me question again?")
    engine.runAndWait()

except sqlite3.Error as error:
    print("Error while connecting to sqlite", error)
    engine.say("I can't understand your question. Could you tell me question again?")
    engine.runAndWait()

finally:
    if (sqliteConnection):
        sqliteConnection.close()
        print("The SQLite connection is closed")