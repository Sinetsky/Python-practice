import os
import pygame
import datetime
import random
from random import randint
import playsound
from gtts import gTTS
import speech_recognition as sr
from speech_recognition import Microphone
import webbrowser as wb

pygame.init()



ready = pygame.mixer.Sound('Я перезагрузился сэр.mp3')
greet = pygame.mixer.Sound('Поздравляю сэр.mp3')
hi = pygame.mixer.Sound('К вашим услугам сэр.mp3')

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

    if "приступаем к работе" in message:
        wb.open_new(url= "https://kwork.ru")
        ready.play()
    elif "пока" in message:
        finish()


def ex(message):
    message = message.lower()
    if "сколько времени" in message:
        now = datetime.datetime.now()
        say("Сейчас " + str(now.hour) + ":" + str(now.minute))


def que(message):
    message = message.lower()
    if "у меня получилось" in message:
       greet.play()

def coffee(message):
    message = message.lower()
    if "джарвис" in message:
        hi.play()






def finish():
    say("увидимся")
    exit()

_name_ = '_main_'

if _name_ == '_main_':
    print("Test")

    while True:
        command = listen()
        handle_message(command)
        que(command)
        ex(command)
        coffee(command)
        
