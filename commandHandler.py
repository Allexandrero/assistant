import random
import time
import logging

import playsound
import speech_recognition as sr
from gtts import gTTS

import database as db


logging.basicConfig(filename='log.log', encoding='utf-8', level=logging.INFO)


def make_log(log, argument = None):

    if log == 'database':
        logging.info(f'[{str(time.ctime())}]: accessing Database...')
    
    if log == 'message':
        logging.info(f'[{str(time.ctime())}]: {argument} saved successfully')


def listen_command():
    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Скажите команду: ")
        audio = r.listen(source)

    # recognize speech using Google Speech Recognition
    try:
        our_speech = r.recognize_google(audio, language="ru")
        print("You said: " + our_speech)
        return our_speech

    except sr.UnknownValueError:
        return "[ERROR]: Unknown Value "

    except sr.RequestError as e:
        return f"[ERROR]: Couldn't request results from GSR Service; {e} "


def do_this_command(message):
    message = message.lower()

    print(database_command('GET'))

    if "привет" in message:
        say_message("привет!")
    elif "пока" in message:
        say_message("пока! было весело!")
        exit()
    else:
        say_message("Я вас не понял. Можете повторить?")


def say_message(message):
    log = 'message'
    
    voice = gTTS(message, lang="ru")
    file_voice_name = '_audio_' + str(time.time()) + '_' + str(random.randint(0, 100000)) + '.mp3'
    voice.save('Audio\\' + file_voice_name)
    make_log(log, file_voice_name)

    playsound.playsound('Audio\\' + file_voice_name)
    print("Голосовой ассистент отвечает: " + message)


def database_command(command):

    log = 'database'

    if command == 'GET': 
        make_log(log)
        return db.request_GET()
    
    elif command == 'POST':
        make_log(log)
        return db.request_POST()
    
    elif command == 'UPDATE':
        make_log(log)
        return db.request_UPDATE()
    
    elif command == 'DELETE':
        make_log(log)
        return db.request_DELETE()    
