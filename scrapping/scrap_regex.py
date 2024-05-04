# Get data from html with regex
from urllib.request import urlopen
import re


def get_tag_content(tag: str, html: str) -> str:
    pattern = f"<{tag}.*?>[\\s\\S]*?</{tag}.?>"
    match_results = re.search(pattern, html, re.IGNORECASE)
    with_tags = match_results.group()
    return re.sub(f"<.*?{tag}.*?>", "", with_tags).strip()


def get_url_tag_content(url: str, tag: str) -> str:
    page = urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    return get_tag_content(tag, html)


if __name__ == "__main__":
    # url = "http://olympus.realpython.org/profiles/aphrodite"
    url = "http://olympus.realpython.org/profiles/poseidon"
    # url = "https://wikipedia.com/robots.txt"
    print(get_url_tag_content(url, "body"))
