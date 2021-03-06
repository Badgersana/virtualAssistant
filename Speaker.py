import pyttsx3

# initialising voice engine settings
engine = pyttsx3.init('sapi5')  # sapi
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
query = ''


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
