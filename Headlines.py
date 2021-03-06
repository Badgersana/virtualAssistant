import requests
from bs4 import BeautifulSoup


commandsList = ['news', 'headlines']
url = "https://www.bbc.co.uk/news"

# gets html content of webpage @url
r1 = requests.get(url)
page = r1.content

soup = BeautifulSoup(page, 'html.parser')

def getHeadlines():
    # main headline
    hClasses = soup.find_all("h3", class_="gs-c-promo-heading__title gel-paragon-bold nw-o-link-split__text")
    # other headlines
    hClasses2 = soup.find_all("h3", class_="gs-c-promo-heading__title gel-pica-bold nw-o-link-split__text")

    output = 'Firstly: ' + hClasses[0].get_text() + '. Also: ' + hClasses2[0].get_text() + '. Lastly: ' \
             + hClasses2[0].get_text()

    return output
