import speech_recognition as sr
import pyttsx3

# Function to recognize speech
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio)
        print(f"You said: {query}")
        return query.lower()
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that. Could you please repeat?")
        return ""
    except sr.RequestError:
        print("Sorry, I couldn't request results at the moment.")
        return ""

# Function to speak
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Function to execute commands
def execute_command(command):
    if "hello" in command:
        speak("Hello! How can I help you?")
    elif "what is your name" in command:
        speak("I am your custom voice assistant.")
    elif "exit" in command:
        speak("Goodbye!")
        exit()
    else:
        speak("Sorry, I didn't understand that command.")

# Main function
def main():
    speak("Initializing voice assistant...")
    while True:
        command = recognize_speech()
        execute_command(command)

if __name__ == "__main__":
    main()
