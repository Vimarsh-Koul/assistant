import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices') #getting details of current voice
engine.setProperty('voice', voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
  pass

def takecommand():
    # it takes commands from the user via microphone

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

    except:
        # print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query

if __name__=="__main__":
    speak("hi vimarsh! how may i help you") 
    while True: 
        query = takecommand().lower()
       #if wikipedia found in the speech then this if block is executed
        if 'wikipedia' in query:  
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia")
            print(results)
            # speak(results)
        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com/")    
        elif 'author' in query:
            webbrowser.open("https://github.com/Vimarsh-Koul")   

        elif 'problem with my code' in query:
            speak("I may just have the right thing for you")
            webbrowser.open("https://stackoverflow.com/")
            speak("here! good luck for your endeavours")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"well, the time is {strTime}")

        elif 'you may leave now' in query:
            speak("Thanks! always great talking to you")
            break                
        
        elif 'open code' in query:
            path = "C:\\Users\\vimar\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(path)

        # elif 'email' in query:
        #     try:
        #         speak("What should I say?")
        #         content = takeCommand()
        #         to = "vimarsh2001koul@gmail.com"    
        #         sendEmail(to, content)
        #         speak("Email has been sent!")
        #     except Exception as e:
        #         print(e)
        #         speak("Sorry!. I am not able to send this email")