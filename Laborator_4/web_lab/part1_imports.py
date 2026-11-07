# Laborator: functii, metode si importuri pe web
# Student: Barbuta Victor, SI-266
# Partea 1: importuri (exercitiile 1-8)

import time
import urllib.error
import urllib.request

BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10  # secunde


def main():
    """Ruleaza exercitiile 1-8."""
    import requests

    print("Ex.1 - versiune requests:", requests.__version__)
    # requests este o biblioteca externa: nu vine cu Python, de aceea am instalat-o cu pip.
    # urllib face parte din biblioteca standard, deci exista deja dupa instalarea Python.

    print("\nEx.2")
    r = requests.get(BASE_URL, timeout=TIMEOUT)
    print("requests.get:", r.status_code)
    time.sleep(1)

    from requests import get
    r = get(BASE_URL, timeout=TIMEOUT)
    print("get:", r.status_code)
    # import requests: se vede mereu din ce modul vine functia (requests.get).
    # from requests import get: scriu mai putin, doar get(...).

    print("\nEx.3")
    import requests as rq
    time.sleep(1)
    r = rq.get(BASE_URL, timeout=TIMEOUT)
    print("rq.get:", r.status_code)
    # Un alias ajuta cand numele modulului este lung sau aliasul este cunoscut de toti.
    # Un alias scurt si neobisnuit, ca rq, face codul mai greu de citit pentru altcineva.

    print("\nEx.4")
    time.sleep(1)
    # Site-ul raspunde cu 403 la User-Agent-ul implicit al urllib (Python-urllib),
    # de aceea trimit cererea cu un User-Agent propriu.
    cerere = urllib.request.Request(BASE_URL, headers={"User-Agent": "WebLab-Barbuta-Victor"})
    try:
        with urllib.request.urlopen(cerere, timeout=TIMEOUT) as r2:
            text = r2.read().decode("utf-8", errors="ignore")
            print("status:", r2.status)
            print(text[:200])
    except urllib.error.HTTPError as eroare:
        print("Serverul a refuzat cererea urllib:", eroare.code, eroare.reason)

    print("\nEx.5")
    print(dir(requests))
    # get este o functie, Session este o clasa, adapters este un modul.

    print("\nEx.6")
    help(requests.get)
    # help arata ca get primeste **kwargs, adica argumentele functiei request.
    # Printre ele este timeout, timpul maxim de asteptare in secunde.
    time.sleep(1)
    print(requests.get(BASE_URL, timeout=TIMEOUT).status_code)

    print("\nEx.7")
    time.sleep(1)
    start = time.perf_counter()
    r = requests.get(BASE_URL, timeout=TIMEOUT)
    stop = time.perf_counter()
    print("perf_counter:", stop - start)
    print("response.elapsed:", r.elapsed.total_seconds())
    # perf_counter masoara toata cererea, inclusiv descarcarea corpului.
    # response.elapsed se opreste cand sosesc antetele, de aceea este putin mai mic.

    print("\nEx.8")
    try:
        import bs4
        print("bs4 este instalat")
    except ImportError:
        print("Instalati modulul cu: pip install beautifulsoup4")

    # Verificati-va: un modul este un singur fisier .py, un pachet este un director
    # cu mai multe module, iar o biblioteca este o colectie de pachete si module
    # instalata impreuna, cum este requests.


if __name__ == "__main__":
    main()
