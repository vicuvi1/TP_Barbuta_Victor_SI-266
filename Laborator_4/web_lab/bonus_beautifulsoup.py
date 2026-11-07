# Laborator: functii, metode si importuri pe web
# Student: Barbuta Victor, SI-266
# Bonus: get_title si extract_links rescrise cu BeautifulSoup

import requests
from bs4 import BeautifulSoup

import webtools

BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10  # secunde


def get_title_bs4(html: str) -> str:
    """Returneaza titlul paginii cu BeautifulSoup sau un sir gol."""
    soup = BeautifulSoup(html, "html.parser")
    if soup.title is None:
        return ""
    return soup.title.get_text(strip=True)


def extract_links_bs4(html: str) -> list:
    """Returneaza legaturile din tagurile <a>, fara duplicate."""
    soup = BeautifulSoup(html, "html.parser")
    links = []
    for tag in soup.find_all("a", href=True):
        if tag["href"] not in links:
            links.append(tag["href"])
    return links


def main() -> None:
    """Compara variantele cu BeautifulSoup cu cele din webtools."""
    test_html = """
    <html><head><TITLE lang="ro"> Pagina de test </TITLE></head><body>
    <a href='/despre'>ghilimele simple</a>
    <A HREF="/contact">tag cu majuscule</A>
    <link href="/style.css" rel="stylesheet">
    </body></html>
    """
    print("Titlu, varianta mea:", repr(webtools.get_title(test_html)))
    print("Titlu, BeautifulSoup:", repr(get_title_bs4(test_html)))
    print("Legaturi, varianta mea:", webtools.extract_links(test_html))
    print("Legaturi, BeautifulSoup:", extract_links_bs4(test_html))

    response = requests.get(BASE_URL, timeout=TIMEOUT)
    print("Titlul site-ului:", get_title_bs4(response.text))
    print("Legaturi (find + re):", len(webtools.extract_links(response.text)))
    print("Legaturi (BeautifulSoup):", len(extract_links_bs4(response.text)))

    # Comparatie: cu BeautifulSoup functiile sunt mai scurte si nu mai caut eu pozitii in text.
    # Sunt si mai sigure: titlul este gasit chiar daca tagul are majuscule sau atribute,
    # iar legaturile sunt luate doar din tagurile <a>, inclusiv cele cu ghilimele simple.
    # Varianta cu re ia orice href (si din <link>) si rateaza href-urile cu ghilimele simple.


if __name__ == "__main__":
    main()
