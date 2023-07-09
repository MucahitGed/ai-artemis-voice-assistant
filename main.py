import subprocess
import wolframalpha
import pyttsx3
import tkinter
import json
import random
import operator
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os 
import winshell
import pyjokes
import feedparser
import smtplib
import ctypes
import time
import requests
import shutil
from twilio.rest import Client
from clint.textui import progress
from ecapture import ecapture as ec
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen
import subprocess
import samsungctl

#setting voice engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice' , voices[1].id)
newRateVoice = 160
engine.setProperty('rate' , newRateVoice)

#setting talking and responding
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def demands():
    hour = int(datetime.datetime.now().hour)
    if hour > 6 and hour<12:
        speak("Good Morning Sir")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir")
    else:
        speak("Good Evening Sir")            
    
    artemis = ("Artemis")
    speak(f"I am your assistant {artemis}")

def commandAss():
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Listening")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing")
        query = r.recognize_google(audio , language="en-in")
        print(f"User Said {query}\n")
    except Exception as e:           
        print(e)
        print("I couldn`t get what you said")
        return "None"
    
    return query     
    
def master():
    speak("How should i call you sir")
    
    masterName = commandAss()
    
    # if masterName.lower() not in ["mike" , "victoria"]:
    #     speak("User not authorized")
    #     exit()
    # else:
    
    speak("Welcome Mister")
    speak(masterName)
    columns = shutil.get_terminal_size().columns
    print("#####################".center(columns))
    print("Welcome Mr.", masterName.center(columns))
    print("#####################".center(columns))
    speak(f"How can i Help you {masterName}")
    
    # if not masterName == "Mike" or "Victoria":
    #     speak("User not authorized")
    #     exit()


def sendEmail(to , content):
    server = smtplib.SMTP('smtp.gmail.com' , 587)
    server.ehlo()
    server.starttls()
    
    #Enable low security in gmail
    server.login("your email id" , "your email password")
    server.sendmail("your email id", to , content)
    server.close()

#comlicated order functions
def turn_on_tv():
    config = {
        "name" : "Golcuk Televizyon" ,
        "description" : "Golcuk Televizyon Description",
        "id" : "my_tv_id" ,
        "host" : "my_tv_ip_adress",
        "method" : "websocket",
        "timeout" : 0
    }
    try:
        with samsungctl.Remote(config) as remote:
            remote.control("KEY_POWERON")
            speak("Tv turned on")
    except Exception as e:
        print("Error wiht" , str(e))
        speak("Sorry I couldnt turned on tv")        

def turn_off_tv():
    config = {
        "name" : "Golcuk Televizyon" ,
        "description" : "Golcuk Televizyon Description",
        "id" : "my_tv_id" ,
        "host" : "my_tv_ip_adress",
        "method" : "websocket",
        "timeout" : 0
    }
    try:
        with samsungctl.Remote(config) as remote:
            remote.control("KEY_POWEROFF")
            speak("Tv turned on")
    except Exception as e:
        print("Error wiht" , str(e))
        speak("Sorry I couldnt turned off tv")        

#orders starts here

if __name__ == "__main__":
    clear = lambda: os.system("cls")
    # This Function will clean any
    # command before execution of this python file
    clear()
    demands()
    master()
    
    while True:
        query = commandAss().lower()
        # All the commands said by user will be
        # stored here in 'query' and will be
        # converted to lower case for easily
        # recognition of command
        
        if "wikipedia" in query:
            speak("Searching Wikipedia")
            query = query.replace("wikipedia" , "")
            results = wikipedia.summary(query , sentences=3)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif "open youtube" in query:
            speak("Opening youtube")
            webbrowser.open("youtube.com")
        elif "open google" in query:
            speak("Opening google")
            webbrowser.open("google.com") 
        elif "open instagram" in query:
            speak("Opening instagram")
            webbrowser.open("instagram.com")
        elif "open facebook" in query:
            speak("Opening facebook")
            webbrowser.open("facebook.com")            
        elif "open stackoverflow" in query:    
            speak("Here you go to Stack Over flow.Happy coding")
            webbrowser.open("stackoverflow.com")  
        elif "play music" in query or "open spotify" in query or "turn on music" in query:
            speak("Here turning on music")    
            spotify = "C:\Program Files\WindowsApps\SpotifyAB.SpotifyMusic_1.213.661.0_x86__zpdnekdrzrea0\Spotify.exe"
            subprocess.call(['cmd', '/c', 'spotify'] , shell=True)
        elif "time" in query or "what is the time now" in query:
            strTime = time.strftime("%m-%d-%Y %T:%M%p")
            speak(f"Sir, the time is {strTime}") 
        elif "what do you think about victoria" in query:
            speak("I think she should give you blowjob tonight")
        elif "what do you think about brother" in query:
            speak("Onu seviyorum")   
        elif "what are you" in query or "who are you" in query:
            speak("I am AI assistant design by imamkoylu yazilimci")
        elif "who made you" in query or "who created you" in query:
            speak("I am designed by Mucahit Gedik")  
        # elif f"{query}" in query or "open village" in query:
            # game = rf'C:\Users\mucah\Desktop\GameList\{query}.exe'
            # subprocess.call(['cmd', '/c', 'game'] , shell=True)
            # print(query)
            # print("worked")
            # speak(f"Here I {query} for you.Enjoy your game")                           
        elif "turn on the TV" in query:
            turn_on_tv()
        elif "turn off the TV" in query:
            turn_off_tv()    
        elif "sleep" in query or "close" in query or "exit" in query:
            speak("It was pleasure to serve you")
            exit()    
            