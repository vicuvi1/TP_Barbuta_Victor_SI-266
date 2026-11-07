# Laborator: functii, metode si importuri pe web
# Student: Barbuta Victor, SI-266
# Partea 3: propriile functii (exercitiile 21-34)

import time
import requests

BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10  # secunde


def fetch(url: str, timeout: int = 10) -> requests.Response:
    """Descarca un URL si returneaza raspunsul."""
    return requests.get(url, timeout=timeout)


def get_status(url: str) -> int:
    """Returneaza codul de stare."""
    return requests.get(url, timeout=TIMEOUT).status_code


def get_title(html: str) -> str:
    """Returneaza titlul unei pagini HTML sau un sir gol daca titlul lipseste."""
    start = html.find("<title>")
    end = html.find("</title>")
    if start == -1 or end == -1:
        return ""
    return html[start + len("<title>"):end].strip()


def page_exists(url: str) -> bool:
    """Returneaza True daca pagina poate fi accesata."""
    try:
        r = requests.get(url, timeout=TIMEOUT)
        r.raise_for_status()
        return True
    except requests.RequestException:
        return False


def check_paths(base: str, paths: list) -> dict:
    """Returneaza statusul pentru fiecare cale."""
    result = {}
    for i, path in enumerate(paths):
        if i:
            time.sleep(1)
        try:
            result[path] = requests.get(base.rstrip("/") + path, timeout=TIMEOUT).status_code
        except requests.RequestException:
            result[path] = None
    return result


def get_header(url: str, name: str, default: str = "lipseste") -> str:
    """Returneaza un antet HTTP."""
    try:
        r = requests.get(url, timeout=TIMEOUT)
        return r.headers.get(name, default)
    except requests.RequestException:
        return default


def security_headers(url: str) -> dict:
    """Verifica cele cinci antete de securitate."""
    names = [
        "Strict-Transport-Security",
        "Content-Security-Policy",
        "X-Frame-Options",
        "X-Content-Type-Options",
        "Referrer-Policy",
    ]
    r = requests.get(url, timeout=TIMEOUT)
    return {name: name in r.headers for name in names}


def score_headers(results: dict) -> str:
    """Returneaza scorul antetelor."""
    return str(sum(results.values())) + "/" + str(len(results))


def fetch_robots(base: str):
    """Returneaza textul din robots.txt sau None daca fisierul lipseste.

    Unele site-uri raspund cu o pagina HTML in loc de 404; si atunci fisierul lipseste.
    """
    try:
        r = requests.get(base.rstrip("/") + "/robots.txt", timeout=TIMEOUT)
        if r.status_code == 404:
            return None
        if "text/html" in r.headers.get("Content-Type", ""):
            return None
        return r.text
    except requests.RequestException:
        return None


def disallowed_paths(robots_text) -> list:
    """Extrage valorile Disallow din robots.txt."""
    if robots_text is None:
        return []
    result = []
    for line in robots_text.splitlines():
        if line.lower().strip().startswith("disallow:"):
            value = line.split(":", 1)[1].strip()
            if value:
                result.append(value)
    return result


def response_times(*urls: str) -> dict:
    """Masora timpul pentru mai multe URL-uri."""
    result = {}
    for i, url in enumerate(urls):
        if i:
            time.sleep(1)
        try:
            start = time.perf_counter()
            requests.get(url, timeout=TIMEOUT)
            result[url] = time.perf_counter() - start
        except requests.RequestException:
            result[url] = None
    return result


def log(message: str, **details) -> None:
    """Afiseaza mesajul si detaliile."""
    text = message
    for key, value in details.items():
        text += " | " + key + "=" + str(value)
    print(text)


def main():
    """Apeleaza functiile din exercitiile 21-34."""
    print("Ex.21")
    r = fetch(BASE_URL)
    print(r.status_code)

    print("\nEx.22")
    time.sleep(1)
    for i, path in enumerate(["/", "/robots.txt", "/sitemap.xml"]):
        if i:
            time.sleep(1)
        print(path, get_status(BASE_URL + path))

    print("\nEx.23")
    time.sleep(1)
    print(fetch(BASE_URL).status_code)
    time.sleep(1)
    print(fetch(BASE_URL, timeout=3).status_code)

    print("\nEx.24-25")
    print(get_title(r.text))
    help(get_title)

    print("\nEx.26")
    # Adnotarile de tip nu ma opresc: Python nu le verifica la rulare.
    # Apelul porneste, iar eroarea vine abia din requests, fiindca 123 nu este un URL.
    try:
        print(get_status(123))
    except Exception as e:
        print("eroare:", e)

    print("\nEx.27")
    time.sleep(1)
    print(page_exists(BASE_URL))
    time.sleep(1)
    print(page_exists("https://this-domain-does-not-exist.invalid"))

    print("\nEx.28")
    time.sleep(1)
    print(check_paths(BASE_URL, ["/", "/robots.txt", "/sitemap.xml"]))

    print("\nEx.29")
    time.sleep(1)
    print(get_header(BASE_URL, name="Server"))

    print("\nEx.30-31")
    time.sleep(1)
    h = security_headers(BASE_URL)
    print(h)
    print(score_headers(h))

    print("\nEx.32")
    time.sleep(1)
    print(disallowed_paths(fetch_robots(BASE_URL)))

    print("\nEx.33")
    time.sleep(1)
    print(response_times(BASE_URL, BASE_URL + "/robots.txt"))

    print("\nEx.34")
    log("verificat", url=BASE_URL, status=200)

    # Verificati-va: print() doar arata valoarea pe ecran, iar functia nu da nimic inapoi.
    # return trimite valoarea catre cel care a apelat functia, deci o pot salva
    # intr-o variabila sau o pot da altei functii.


if __name__ == "__main__":
    main()
