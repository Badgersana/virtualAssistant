import speech_recognition as sr

"""Controls output to user - currently only contains audio output, intend on adding windows notifications"""


def command():
    """
    Listens for and interprets command of user.
    :return: query
    :rtype: str
    """
    # creates recognizer instance
    r = sr.Recognizer()
    # activates microphone
    with sr.Microphone() as source:
        print("Listening...")
        # waits for pause in input
        r.pause_threshold = 1
        audio = r.listen(source)

        # Exception only appears if users command is not recognised
        try:
            # checks if input is recognizable
            print("Recognising...")
            query = r.recognize_google(audio, language='en-in')
            print("User said: " + query)

        except Exception as e:
            query = "Not understood"
            return query

        return query
