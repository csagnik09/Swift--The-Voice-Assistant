import pyttsx3
import os
import time
import speech_recognition as sr
import playsound
from gtts import gTTS



def chime_ac():
    playsound.playsound('/Users/sagnikchakraborty/SwiftBeta/audio/Swift_Activate.mp3')


def chime_dac():
    playsound.playsound('/Users/sagnikchakraborty/SwiftBeta/audio/Swift_Deactivate.mp3')


def play(file_path):
    playsound.playsound(file_path)


def cttxt(innum):
    number = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    nty = ["", "", "Twenty", "Thirty", "Fourty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninty"]
    tens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen",
            "Nineteen"]
    n = int(innum)
    if n > 99999:
        print("Cant solve for more than 5 digits")
    else:
        d = [0, 0, 0, 0, 0]
        i = 0
        while n > 0:
            d[i] = n % 10
            i += 1
            n = n // 10
        num = ""
        if d[4] != 0:
            if d[4] == 1:
                num += tens[d[3]] + " Thousand "
            else:
                num += nty[d[4]] + " " + number[d[3]] + " Thousand "
        else:
            if d[3] != 0:
                num += number[d[3]] + " Thousand "
        if d[2] != 0:
            num += number[d[2]] + " Hundred "
        if d[1] != 0:
            if d[1] == 1:
                num += tens[d[0]]
            else:
                num += nty[d[1]] + " " + number[d[0]]
        else:
            if d[0] != 0:
                num += number[d[0]]
        return num


def input():
    count = 0
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please Talk")
        chime_ac()
        audio_text = r.listen(source)
        chime_dac()
        try:
            print("You: " + r.recognize_google(audio_text))
        except:
            count = +1
            if count <= 3:
                talk("Sorry, I did not get that")
                talk("Please Try Again")
                input()
    return r.recognize_google(audio_text).lower()


def swift_ker():
    r = sr.Recognizer()
    while True:
        with sr.Microphone() as source:
            audio_text = r.listen(source)
            try:
                print("You: " + r.recognize_google(audio_text))
            except:
                print("No Input Trying Again..")
        return r.recognize_google(audio_text).lower()


def talk(statement):
    tts = gTTS(text=statement, lang="en")
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)




