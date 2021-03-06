import speech_recognition as sr
import Speaker


# listens for user input and passes audio to google speech api to translate into string
def command():
    # creates recognizer instance
    r = sr.Recognizer()
    # activates microphone
    with sr.Microphone() as source:
        print("Listening...")
        # waits for pause in input
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            # checks if input is recognizable
            print("Recognising...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
        except Exception as e:
            # will re-ask for request if not understood
            Speaker.speak("I did not understand, can you say that again please")
            command()
            return ""
        return query
