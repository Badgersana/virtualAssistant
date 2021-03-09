import requests


commandsList = ['weather', 'week']

"""Contains logic for accessing location based weather information via accuWeather API"""


def getWeather():
    """
    Accesses Accuweather API - Finds appropriate information as set out in returned JSON dictionary
    Formats the text so it can be output to the user in main.py
    :return: output
    :rtype: str
    """

    # api_key = "ibIC9KVfkUp8pttH1gFjJ9wnLxhdmwZW"
    # location_key = 323620
    url = "http://dataservice.accuweather.com/forecasts/v1/daily/1day/323620?apikey=ibIC9KVfkUp8pttH1gFjJ9wnLxhdmwZW&metric=true HTTP/1.1"

    # retrieves data from api
    response = requests.get(url)

    # formats data into a dictionary
    jsonResponse = response.json()

    # retrieves necessary information from jsonResponse
    tempHigh = jsonResponse['DailyForecasts'][0].get('Temperature').get('Maximum').get('Value')
    tempLow = jsonResponse['DailyForecasts'][0].get('Temperature').get('Minimum').get('Value')
    weatherType = jsonResponse['DailyForecasts'][0].get('Day').get('IconPhrase')

    tempHigh = parseTemp(tempHigh)
    tempLow = parseTemp(tempLow)

    output = "The weather is: " + weatherType + " in Welwyn Garden City." \
                                                     " With a high of: " + tempHigh\
                                                        + " and a low of: " + tempLow

    return output


def changeInt(answer):
    """
    Checks if answer is a whole number represented as a float e.g 19 > 19.0. Removes .0 after check - allows the program
    to keep answer as string instead of changing type
    :param answer: result from performed operation
    :type answer: str
    :return: answer
    :rtype: str
    """
    if answer[-2:] == ".0":
        answer = answer[:-2]

    return answer


def parseTemp(temp):
    """
    Changes temperature value from float to int if necessary, and then converts from farenheit to celcius
    :param temp: temperature returned from json dictionary
    :type temp: float
    :return: temp
    :rtype: str
    """
    temp = (temp - 32) * 5 / 9
    temp = round(temp, 1)
    temp = changeInt(str(temp))

    return temp
