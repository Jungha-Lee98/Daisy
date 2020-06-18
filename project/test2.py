# this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr
import pyttsx3

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
    r.energy_threshold = 500
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
        if loop == ('How' or 'Which'):
            sqlquery.append("SELECT ")

        elif loop == ('many'):
            sqlquery.append("count(*) ")
            sqlquery.append("from divvy_2015 ")

        elif loop == ('people'):
            sqlquery.append('where usertype="customer" ')

         

    print(''.join(sqlquery) + ';')
    

    engine.say(r.recognize_sphinx(audio))
    engine.runAndWait()
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))