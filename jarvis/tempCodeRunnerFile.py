import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good Morning !")
    elif hour>=12 and hour<18:
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
         query = r.recognize_google(audio, languagr= 'en-in')
         print(f"User said: {query}\n")
    
     except Exception as e:

        #print(e)

         print("kindly repeat what you said")
         return "None"
     return query



if __name__=="__main__":
    wishMe()
    while True:

        query = takecommand().lower()