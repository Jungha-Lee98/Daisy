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
    word_list = []
    word_list = r.recognize_sphinx(audio).split(' ')

    speek_list = []

    for words in word_list:
        if words!= 'a':
            speek_list.append(words)
    print(speek_list)

    sqlquery=[]         

    for loop in speek_list:
        if loop == ('how' or 'which'):
            sqlquery.append("SELECT ")

        elif loop == ('many'):
            sqlquery.append("count(*) ")
            sqlquery.append("from divvy_2015 ")

        elif loop == ('customer'):
            sqlquery.append('where usertype="Customer" ')
        
        elif loop == ('people'):
            sqlquery.append('where usertype="Subscriber" ')
        
        elif loop == ('female'):
            sqlquery.append('where gender="Female"')
        

         

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

    engine.say("I think {0} left".format(row))
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

