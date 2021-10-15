import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import phonenumbers
from phonenumbers import geocoder, carrier, timezone




engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id) #voices[0] for male voice


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good Morning !")
    elif hour>=12 and hour<17:
        speak("Good Afternoon !")
    else:
        speak("Good Evening !")
    speak("i am voice assistant. please tell me how may I help you !!")


def takecommand():
     # to take microphn input from 
     

     r=sr.Recognizer()
     with sr.Microphone() as source:
         print("Listening....")
         r.pause_threshold= 1
         audio = r.listen(source)
     try:
         print("Recognizing...")
         query = r.recognize_google(audio, language= 'en-in')
         print(f"User said: {query}\n")
    
     except Exception as e:


         # print(e)
        speak("kindly repeat what you said")
        print("kindly repeat what you said")
        return "None"
     return query



if __name__=="__main__":
    wishMe()
    while True:
        query = takecommand().lower()
        if 'wikipedia' in query:
            speak('Searchig Wikipedia....')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)    #Plain text summary of the page.

            speak("According to wikipedia ")
            speak(results)
        elif 'open youtube'   in query:
            webbrowser.open("youtube.com")
        elif 'open stack overflow'   in query:
            webbrowser.open("https://stackoverflow.com/")
        
        elif 'open google'   in query:
            webbrowser.open("google.com")

        elif "what's the time"   in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")  #current time btane ke leye now use kra hai
            speak(f"the time is {strTime}")

        elif 'open vs code' in query  :
            codepath = "C:\\Users\\Palak Sharma\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
        elif "play music" in query:
            speak("which music you would like to listen")
            webbrowser.open("https://gaana.com/")
        elif "quit" in query:
            speak("have a nice day!")
            print("quit")
            exit()
        elif "open my files" in query:
            codepath="C:\\Users\\Palak Sharma"
            os.startfile(codepath)
        
        elif "tell me something about yourself" in query:
            speak("hello, I am voice assistant , i am a prototype of advance version on alexa, siri, hello google!. i  may assist you in certain task and help you in every way possible to make your work easier. i am still evolving with the help of my mentor Palak Sharma. you may give certain feedback and help me serve you better. Have a nice day! ")

        elif "show my location" in query:
            speak("enter your phonenumber")
            number=phonenumbers.parse(input("Enter number with code(+91) "), None)
            result=geocoder.description_for_number(number,'en')
            speak(result)
            print(result)
            result2=carrier.name_for_number(number, 'en')
            speak(result2)
            print(result2)
            result3=timezone.time_zones_for_number(number) 
            speak(result3)
            print(result3)
                             

