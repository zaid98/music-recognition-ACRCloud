# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 17:03:22 2019

@author: zaid
"""

import speech_recognition as sr
r = sr.Recognizer()
'''music = sr.AudioFile('audio_speech.wav')

with music as source:
   audio = r.record(source)

print((r.recognize_google(audio,language="es-GB")))
'''
with sr.Microphone() as source:
    print("Speak Anything :")
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("You said : {}".format(text))
    except:
        print("Sorry could not recognize what you said")