import datetime
import random
from random import randint
import playsound
from gtts import gTTS
import speech_recognition as sr
from speech_recognition import Microphone



mic = sr.Microphone(device_index=0)


def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Какие будут указания: ")
        audio = r.listen(source)

    try:
       return r.recognize_google(audio, language="ru")
    except sr.UnknownValueError:
        return 'Error'
    except sr.RequestError:
       return 'error'

def say(text):
    voice = gTTS(text, lang="ru")
    Unique_filename = "audio_" + str(random.randint(0, 100000)) + ".mp3"
    voice.save(Unique_filename)

    playsound.playsound(Unique_filename)
    print("Ассистент:", text)




def handle_message(message):
    message = message.lower()

    if "привет" in message:
        say("Приветствую, какие будут указания?")
    elif "пока" in message:
        finish()


def ex(message):
    message = message.lower()
    if "сколько времени" in message:
        now = datetime.datetime.now()
        say("Сейчас " + str(now.hour) + ":" + str(now.minute))


def Yname(message):
    message = message.lower()
    if "как тебя зовут" in message:
        say("меня зовут гюнтер")

def Abl(message):
    message = message.lower()
    if "что ты умеешь" in message:
        say("чему меня научат то я и сумею")

def coffee(message):
    message = message.lower()
    if "свари мне кофе" in message:
        say("когда меня научат ходить я хотя бы встану")






def finish():
    say("увидимся")
    exit()

_name_ = '_main_'

if _name_ == '_main_':
    print("Test")

    while True:
        command = listen()
        handle_message(command)
        Yname(command)
        Abl(command)
        ex(command)
        coffee(command)
