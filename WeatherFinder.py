import requests

commandsList = ['weather']

"""Contains logic for accessing location based weather information via accuWeather API"""

def getWeather():
    """
    Accesses Accuweather API - Finds appropriate information as set out in returned JSON dictionary
    Formats the text so it can be output to the user in main.py
    :return: output
    :rtype: str
    """
    tempHigh = ""
    tempLow = ""
    weatherType = ""

    api_key = "ibIC9KVfkUp8pttH1gFjJ9wnLxhdmwZW"
    response = requests.get(
        "http://dataservice.accuweather.com/forecasts/v1/daily/1day/323620?apikey=ibIC9KVfkUp8pttH1gFjJ9wnLxhdmwZW&language=en-us&details=false&metric=true HTTP/1.1")
    jsonResponse = response.json()

    tempHigh = jsonResponse['DailyForecasts'][0].get('Temperature').get('Maximum').get('Value')
    tempLow = jsonResponse['DailyForecasts'][0].get('Temperature').get('Minimum').get('Value')
    weatherType = jsonResponse['DailyForecasts'][0].get('Day').get('IconPhrase')

    output = "The weather is: " + weatherType + " in Welwyn Garden City." \
                                                " With a high of: " + tempHigh + "and a low of: " + tempLow

    return output
