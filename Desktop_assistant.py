# Before using below code , pls ensure to install all required Python libraries
# pip install pyttsx3
# pip install SpeechRecognition
# pip install wikipedia
# conda install --yes pyaudio




from time import sleep
import pyttsx3
import pyaudio
import datetime
import wikipedia
import os
import smtplib
import webbrowser
import speech_recognition as sr
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('Voice',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    

def sendmail(to,msg):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('useremail@gmail.com', '')
    server.sendmail('useremail@gmail.com', to, content)
    server.close()
   
    
def wish_me():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning sir")
    elif hour>=12 and hour<18:
        speak("Good Afternoon sir")
    else:
        speak("good night sir")
    speak("I am an AI bot,made to help you")   
def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 2
        audio = r.listen(source)
        print("Listening completed")
        
        

    try:
        print("Recognizing...")    
        query = r.recognize(audio)
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)    
        print("Say that again please...")  
        return "None"
    return query  
if __name__=='__main__':
    speak("Hi User,")
    wish_me()
    while True:
        query=takeCommand().lower() 
        if 'wikipedia' in query:
            speak("Searching wikipedia")
            query=query.replace('wikipedia','')
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'youtube' in query:
            from selenium import webdriver
            driver=webdriver.Chrome(executable_path=r'C:\Users\Downloads\chromedriver.exe')
            driver.get('https://youtube.com')
        elif 'google' in query:
            webbrowser.open('google.com')
        elif 'mailjj' in query:
            webbrowser.open('outlook.com')
        elif 'outlook' in query:
            filep=r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Outlook'
            os.startfile(filep)
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")   
        elif 'song' in query:
            from selenium import webdriver
            driver=webdriver.Chrome(executable_path=r'C:\Users\euakumn\Downloads\chromedriver.exe')
            driver.get("https://gaana.com/playlist/gaana-dj-hindi-top-50-1")
            sleep(40)
            play_btn=driver.find_element_by_xpath('//*[@id="p-list-play_all"]/span')
            play_btn.click()
        elif 'excel' in query:
            filep=r'C:\Program Files (x86)\Microsoft Office\root\Office16\EXCEL.EXE'
            os.startfile(filep)
        elif 'stop' or 'exit' in query:
            break
        elif 'write-email' in query:
            try:
                speak("Please provide email and msg")
                msg=takeCommand()
                to='recipient_name@gmail.com'
                sendmail(to,msg)
                speak("Email sent")
         
            except Exception as e:
                print(e)
                speak("Pls try again,mail could not be sent")
                
