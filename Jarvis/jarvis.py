import pyttsx3
import webbrowser
import smtplib
import random
import speech_recognition as sr
import wikipedia
import time
import datetime
import pyjokes
import os
import os.path
import sys
import wolframalpha
import PyPDF2
import requests
from requests import get
import json
from tkinter.filedialog import *

try:
    app = wolframalpha.Client("7AEVY2-YPGJA675YX")
except Exception:
    print("Some Features are not working ")    

engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    print('Computer: ' + audio)
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    currentH = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")
    if currentH >= 0 and currentH < 12:
        speak(f'Good Morning! Pushkar! its {tt} now ')

    elif currentH >= 12 and currentH < 16:
        speak(f'Good Afternoon! Pushkar! its {tt} now')

    else:
        speak(f'Good Evening! Pushkar! its {tt} now')
    speak("I am your Jarvis Sir. Please tell me how can I help you")



def takecommand():
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        print("Listening...")
        r.pause_threshold =  1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f'User: {query}')
        
    except Exception as e :
        print('Please say it again')
        return "none"
    query = query.lower()
    return query
        

def TaskExecution():
    greetMe()
    while True:
        query = takecommand()
        

        if 'wikipedia' in query:  #if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak('okay')
            webbrowser.open('www.youtube.com')

        elif 'open code' in query:
            speak('okay')
            codePath = "C:\\Users\\chandramohan\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open zoom' in query:
            speak('okay')
            codePath = "C:\\Users\\chandramohan\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe"
            os.startfile(codePath)
            
        elif 'open browser' in query:
            speak('Okay')
            codePath = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
            os.startfile(codePath)
                
        elif 'thanks' in query:
            speak('okay')
            speak('Bye Pushkar, have a good day.')
            sys.exit()
            
        elif 'read' in query:
            book = askopenfilename()
            pdfReader = PyPDF2.PdfFileReader(book)
            pages = pdfReader.numPages
            print(pages)
            speaker = pyttsx3.init()
            for num in range(2,range):
                page = pdfReader.getPage(num)
                text  = page.extractText()
                speaker.say(text)
                speaker.runAndWait()

        elif 'where i am' in query or 'where are we' in query:
            speak("Wait Pushkar let me check")
            try:
                ipAdd = requests.get('https://api.ipify.org').text
                print(ipAdd)
                url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
                geo_requests = requests.get(url)
                geo_data = geo_requests.json()
                city = geo_data['city']
                state = geo_data['state']
                country = geo_data['country']
                speak(f'We are in {city} city of state  {state} in country of {country}')
            except Exception as e:
                speak("Sorry Pushkar, Due to network issue i am not able to find where we are.")
                pass
        
        elif 'sleep' in query:
            speak("Okay Pushkar, I am going to sleep. Feel free to contact me again")
            break

        elif 'joke' in query:
            speak('Okay')
            print(pyjokes.get_joke())
            speak(pyjokes.get_joke())

        elif 'shut down' in query:
            speak("Shutting Down your system")
            speak("Bye Pushkar have a good day")
            os.system("shutdown -s")
            sys.exit()    

        elif 'news' in query:
            speak("Please wait pushkar, fetching the latest news")
            main_url = 'http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=d780d06a88814956b6560ac4ab3bd183'
            main_page = requests.get(main_url).json()
            articles = main_page["articles"]
            head = []
            day = ["first","second","third","fourth","fifth","sixth","seventh","eighth","ninth","tenth"]
            for ar in articles:
                head.append(ar["title"])
            for i in range (len(day)):
                speak(f"today's {day[i]} news is: {head[i]}")
            
            
        elif 'temperature' in query:
            try:
                res = app.query(query)
                print(next(res.results).text)
                speak(next(res.results).text) 
            except:
                print("Internet connection error")
        speak('Next Command! Pushkar!')                
            
         

if __name__ == "__main__":
    while True:
        permission = takecommand()
        if 'ok' in permission:
            TaskExecution()
        elif 'goodbye' in permission:
            sys.exit()

             

        
            
            
            
            
            
            
            
           
        

        
           
        


           
                                    
        
            

        
                
                    
                
        
            
        
        
