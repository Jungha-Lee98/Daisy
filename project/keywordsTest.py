import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()
engine = pyttsx3.init()

# set Microphone instances
with sr.Microphone(device_index=1, chunk_size=1024, sample_rate=48000) as source:
    print("Please wait. Calibrating microphone...") 
    r.adjust_for_ambient_noise(source, duration=1) 
    r.energy_threshold = 1000
    r.dynamic_energy_threshold = True
    r.dynamic_energy_adjustment_damping = 0.15
    r.dynamic_energy_adjustment_ratio = 1.5
    r.pause_threshold = 0.8

# get user's speech 
    audio1 = r.listen(source)
    daisy = "hey daisy"

    print("Sphinx thinks you said " + r.recognize_sphinx(audio1, keyword_entries= [(daisy,0.8)]))
    
    # speak to user 'say something!'
    engine.say("how can I help you?")
    engine.runAndWait()
    print("how can I help you?")
    print("\n")