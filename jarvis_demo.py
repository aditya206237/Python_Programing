import os
import speech_recognition as sr
import pyttsx3
import webbrowser

# Initialize the recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio).lower()
            print(f"You said: {command}")
            return command
        except sr.UnknownValueError:
            speak("Sorry, I didn't understand that.")
        except sr.RequestError as e:
            speak("Couldn't process your request. Check your internet connection.")
        return None

def execute_command(command):
    if "open edge" in command:
        speak("Opening the web browser.")
        webbrowser.open("https://www.microsoftedge.com")
    elif "play music" in command:
        speak("Playing music from your system.")
        music_dir = "C:\\Your\\Music\\Directory"  # Replace with your music folder
        songs = os.listdir(music_dir)
        if songs:
            os.startfile(os.path.join(music_dir, songs[0]))
        else:
            speak("No music files found in the specified directory.")
    elif "shut down" in command:
        speak("Shutting down your system.")
        os.system("shutdown /s /t 5")
    elif "restart" in command:
        speak("Restarting your system.")
        os.system("shutdown /r /t 15")
    elif "abort" in command:
        speak("Aborting the system shutdown.")
        os.system("shutdown /a")
    elif "Open youtube" in command:
        speak("Opening Youtube")
        webbrowser.open("https://www.youtube.com")
    else:
        speak("Sorry, I can't handle that command yet.")

# Main loop
speak("Hello, I am your assistant. How can I help you today?")
while True:
    command = listen()
    if command:
        if "exit" in command or "quit" in command:
            speak("Goodbye!")
            break
        execute_command(command)