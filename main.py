import speech_recognition as sr
import pyttsx3

import datetime
import wikipedia
import webbrowser
import os



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)


engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour <= 12:

        a = ("Good Morning Sir!")
        print(a)
        speak("Good Morning Sir")

    elif hour >= 12 and hour <= 18:

        a = ("Good Afternoon Sir !")
        print(a)
        speak(" Good Afternoon Sir ")

    else:

        a = ("Good Evening Sir ")
        print(a)
        speak(" Good Evening Sir")

    print("  how are you?")
    speak("  how are you?")



def takeCommand():
    # it takes microphone from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone()  as source:

        print("Listening...")
        r.pause_threshold = 0.8
        audio = r.listen(source)




    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language ='en-IN')
        print(   { query } )

    except Exception as e:
        #print(e)
        speak("Say that again please..")
        return "None"

    return query





if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            print("searching wikipedia...")
            speak("searching wikipedia...")
            query = query.replace("wikipedia", " ")
            results = wikipedia.summary(query,sentences=3)
            print(results)
            speak("According to wikipedia")
            speak(results)
            speak("!anything else sir")

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak("!anything else sir")


        elif 'open google' in query:
            webbrowser.open("google.com")
            speak("!anything else sir")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
            speak("anything else sir")

        elif 'play music' in query:
            music_dir = 'E:\\MUSIC\\Jarvisplaymusic'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
            speak("!anything else sir")

        elif 'thank you' in query:
            print("welcome sir have a nice day")
            speak("welcome sir have a nice day")
            speak(wishMe)

            exit()

        elif 'how are you' in query:
            print("For computer software I'd say i'm feeling pretty good")
            speak("For computer software I did say i am feeling pretty good")
            speak("!anything else sir")

        elif 'made you' in query:
            speak("I was made by master Pranshu")

        elif 'born' in query:
            speak (" I am not born sir i am created on nineteenth of november through py charm")

        elif 'your name' in query:
            speak(" Jarvis sir. i am your Assistant sir. age old enough to use the internet but young enough to find anything. sorry for cracking a joke but its true")
            speak("!anything else sir")

        elif 'trillion in binary' in query:
            print(" 0b1110100011010100101001010001000000000000 ")
            speak("o b one one one o one o o o one one o one o one o o one o one o o 1 o one o o o one o o o o o o o o o o  ")
            speak("!anything else sir")

        elif 'open instagram' in query:
            webbrowser.open("instagram.com")
            speak("!anything else sir")

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")
            speak("!anything else sir")

        elif 'open twitter' in query:
            webbrowser.open("twitter.com")
            speak("!anything else sir")

        elif 'pranshu' in query:
            speak("!Pranshu is my master. he created me . he is so hard working and dedicated person")
            speak("!anything else sir")


         
















