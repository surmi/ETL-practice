# scrapping from webpages with interactive features (MechanicalSoup)
import mechanicalsoup
from urllib.request import urlopen


def reading_after_login():
    url = "http://olympus.realpython.org/login"
    browser = mechanicalsoup.Browser()

    login_page = browser.get(url)
    login_html = login_page.soup

    form = login_html.select("form")[0]
    form.select("input")[0]["value"] = "zeus"
    form.select("input")[1]["value"] = "ThunderDude"

    profiles_page = browser.submit(form, login_page.url)
    links = profiles_page.soup.select("a")
    base_url = "http://olympus.realpython.org"
    for link in links:
        address = base_url + link["href"]
        text = link.text
        print(f"{text}: {address}")


def reading_dice():
    url = "http://olympus.realpython.org/dice"
    browser = mechanicalsoup.Browser()

    dice_page = browser.get(url)
    dice_html = dice_page.soup
    tag = dice_html.select("#result")[0]
    dice_result = tag.text
    print(dice_result)


if __name__ == "__main__":
    # reading_after_login()
    reading_dice()
