import pyttsx3

# initialising voice engine settings
engine = pyttsx3.init('sapi5')  # sapi
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
query = ''

"""Sets up and utilises text to speech engine"""


def speak(audio):
    """
    Audibly outputs audio to user
    :param audio: string to be spoken
    :type audio: str
    :return: null
    :rtype: null
    """
    engine.say(audio)
    engine.runAndWait()
