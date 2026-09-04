import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

engine = pyttsx3.init()

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print("You:", command)
        return command.lower()
    except:
        speak("Sorry, I could not understand.")
        return ""

speak("Hello! How can I help you?")

while True:
    command = listen()

    if "hello" in command:
        speak("Hello! Nice to meet you.")

    elif "time" in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        speak("The time is " + time)

    elif "youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "exit" in command or "stop" in command:
        speak("Goodbye!")
        break

    else:
        speak("I don't know that command.")