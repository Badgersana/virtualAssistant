import Calculator
import FactFinder
import Headlines
import WeatherFinder
import Speaker
import Listener

NAME = 'Alpha'
commandsList = ['+', '-', 'x', '/', '÷', 'news', 'weather', 'week']
REPLY = 'yes Jacob?'

"""Acts as controller for virtual assistant"""

if __name__ == '__main__':
    running = True
    while running:
        output = ""
        initRequest = Listener.command()

        if NAME in initRequest:
            Speaker.speak(REPLY)
            request = Listener.command()

            # checks if any part of request is a subset of both commandsList and Calculator.commandsList
            if any(command in request for command in Calculator.commandsList):
                output = Calculator.start(request)

            elif any(command in request for command in Headlines.commandsList):
                output = Headlines.getHeadlines()

            elif any(command in request for command in WeatherFinder.commandsList):
                output = WeatherFinder.getWeather()

        print(output)  # temp
        Speaker.speak(output)
