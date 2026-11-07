# Laborator: functii, metode si importuri pe web
# Student: Barbuta Victor, SI-266
# Partea 4: alte module din biblioteca standard (exercitiile 35-43)

import hashlib
import json
import re
import socket
import ssl
import time
from html.parser import HTMLParser
from urllib.parse import urljoin, urlparse

import requests

BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10  # secunde


def parse_url(url):
    """Descompune un URL."""
    p = urlparse(url)
    return p.scheme, p.netloc, p.path, p.query, p.fragment


def make_urls(base, links):
    """Transforma linkuri relative in URL-uri complete."""
    return [urljoin(base, link) for link in links]


def extract_links(html):
    """Extrage href-urile fara duplicate."""
    links = re.findall(r'href="([^"]+)"', html)
    return list(dict.fromkeys(links))


def split_links(links, domain):
    """Imparte linkurile in interne si externe."""
    internal = []
    external = []
    base = "https://" + domain
    for link in links:
        full = urljoin(base, link)
        if urlparse(full).netloc == domain:
            internal.append(full)
        else:
            external.append(full)
    return internal, external


class ImageFinder(HTMLParser):
    """Gaseste valorile src din tagurile img."""

    def __init__(self):
        """Creeaza lista de imagini."""
        super().__init__()
        self.images = []

    def handle_starttag(self, tag, attrs):
        """Este apelata automat cand parserul gaseste un tag."""
        if tag.lower() == "img":
            src = dict(attrs).get("src")
            if src:
                self.images.append(src)


def page_fingerprint(url):
    """Calculeaza SHA-256 pentru continutul paginii."""
    r = requests.get(url, timeout=TIMEOUT)
    return hashlib.sha256(r.content).hexdigest()


def save_headers(url, filename="headers.json"):
    """Salveaza antetele in JSON si le citeste inapoi."""
    r = requests.get(url, timeout=TIMEOUT)
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(dict(r.headers), file, indent=2)
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)


def resolve(hostname):
    """Returneaza adresa IP."""
    return socket.gethostbyname(hostname)


def cert_days_left(hostname):
    """Returneaza cate zile mai sunt pana la expirarea certificatului."""
    context = ssl.create_default_context()
    with socket.create_connection((hostname, 443), timeout=TIMEOUT) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as s:
            cert = s.getpeercert()
    expires = ssl.cert_time_to_seconds(cert["notAfter"])
    return int((expires - time.time()) / 86400)


def main():
    """Apeleaza functiile din exercitiile 35-43."""
    print("Ex.35")
    p = parse_url("https://cybercor.org/path?x=1#top")
    print("scheme:", p[0])
    print("netloc:", p[1])
    print("path:", p[2])
    print("query:", p[3])
    print("fragment:", p[4])

    print("\nEx.36")
    print(make_urls(BASE_URL, ["/about", "contact.html", "../index.html"]))

    print("\nEx.37-38")
    r = requests.get(BASE_URL, timeout=TIMEOUT)
    links = extract_links(r.text)
    print("linkuri:", links)
    internal, external = split_links(links, urlparse(r.url).netloc)
    print("interne:", len(internal))
    print("externe:", len(external))

    print("\nEx.39")
    test_html = """
    <img src="/logo.png" alt="Logo">
    <IMG SRC="poza.jpg">
    <img alt="fara src">
    <img src="https://cdn.example.com/banner.webp" />
    <a href="/despre">link</a>
    """
    finder = ImageFinder()
    finder.feed(test_html)
    print(finder.images)
    assert finder.images == ["/logo.png", "poza.jpg", "https://cdn.example.com/banner.webp"]
    print("Testul a trecut")

    finder = ImageFinder()
    finder.feed(r.text)
    print(len(finder.images), "imagini gasite")
    for src in finder.images:
        print(src)
    print("<img in sursa:", r.text.lower().count("<img"))

    print("\nEx.40")
    time.sleep(1)
    f1 = page_fingerprint(BASE_URL)
    time.sleep(1)
    f2 = page_fingerprint(BASE_URL)
    print(f1)
    print(f2)
    print("identice:", f1 == f2)
    # Amprentele ar fi diferite daca se schimba macar un octet din pagina intre cele
    # doua cereri, de exemplu o data afisata, un token sau continut generat dinamic.

    print("\nEx.41")
    time.sleep(1)
    data = save_headers(BASE_URL)
    print(data.get("Content-Type", "lipseste"))

    print("\nEx.42")
    print(resolve("cybercor.org"))

    print("\nEx.43")
    print(cert_days_left("cybercor.org"))

    # Verificati-va: handle_starttag() este apelata de HTMLParser, din interiorul
    # metodei feed(), de fiecare data cand gaseste un tag de deschidere.


if __name__ == "__main__":
    main()
