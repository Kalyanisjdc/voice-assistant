import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# initialize speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio)
            command = command.lower()
            print("You said:", command)
            return command
        except:
            print("Sorry, I did not understand.")
            return ""

print("Voice Assistant Started")
speak("Hello, I am your voice assistant")

while True:

    command = listen()

    if "hello" in command:
        speak("Hello, how can I help you?")

    elif "time" in command:
        time = datetime.datetime.now().strftime("%H:%M")
        speak("The time is " + time)

    elif "date" in command:
        date = datetime.datetime.now().strftime("%d %B %Y")
        speak("Today's date is " + date)

    elif "search" in command:
        speak("What should I search?")
        query = listen()
        webbrowser.open("https://www.google.com/search?q=" + query)

    elif "bye" in command:
        speak("Goodbye")
        break

    else:
        speak("Please say the command again")
