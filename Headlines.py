import requests
from bs4 import BeautifulSoup
# to extend - give the user the ability to select a headline and provide the link to the article
commandsList = ['news', 'headlines']

"""Contains all logic for retrieving headlines"""

url = "https://www.bbc.co.uk/news"

# gets html content of webpage @url and stores it in page
r1 = requests.get(url)
page = r1.content

soup = BeautifulSoup(page, 'html.parser')

# finds all elements of webpage and stores them in respective lists, formats output so it can be spoken by speaker class
def getHeadlines():
    """
    Stores main headline in mainHL and other headlines in otherHL. Formats the text so it can be output to the user in
    main.py
    :return: output
    :rtype: str
    """
    # main headline
    mainHL = soup.find_all("h3", class_="gs-c-promo-heading__title gel-paragon-bold nw-o-link-split__text")
    # other headlines
    otherHL = soup.find_all("h3", class_="gs-c-promo-heading__title gel-pica-bold nw-o-link-split__text")

    output = 'Firstly: ' + mainHL[0].get_text() + '. Also: ' + otherHL[0].get_text() + '. Lastly: ' \
             + otherHL[1].get_text()

    return output
