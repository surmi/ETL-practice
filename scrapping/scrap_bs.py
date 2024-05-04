# Scrap with BeautifulSoup
from bs4 import BeautifulSoup
from urllib.request import urlopen


if __name__ == "__main__":
    url = "http://olympus.realpython.org/profiles/dionysus"
    page = urlopen(url)
    html = page.read().decode('utf-8')
    soup = BeautifulSoup(html, "html.parser")
    # soup object contains now parsed html
    # use square bracket notation or (in some cases) tag names as soup object properties
