# Laborator: functii, metode si importuri pe web
# Student: Barbuta Victor, SI-266
# Partea 2: metode si atribute (exercitiile 9-20)

import time
import requests

BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10  # secunde


def main():
    """Ruleaza exercitiile 9-20."""
    response = requests.get(BASE_URL, timeout=TIMEOUT)

    print("Ex.9")
    print(response.status_code)  # atribut
    print(response.ok)           # atribut
    print(response.url)          # atribut
    print(response.encoding)     # atribut

    print("\nEx.10")
    try:
        response.raise_for_status()
        print("Pagina principala a raspuns fara eroare")
        time.sleep(1)
        bad = requests.get(BASE_URL + "/this-page-does-not-exist", timeout=TIMEOUT)
        bad.raise_for_status()
        # cybercor.org raspunde cu 200 si pentru adrese care nu exista,
        # de aceea aici HTTPError nu apare; la un cod 404 ar rula blocul except.
        print("Serverul a raspuns cu", bad.status_code, "si pentru o pagina inexistenta")
    except requests.HTTPError:
        print("Pagina nu exista sau a aparut o eroare HTTP")

    print("\nEx.11")
    for name, value in response.headers.items():
        print(name + ":", value)

    print("\nEx.12")
    print("Server:", response.headers.get("Server", "lipseste"))
    print("Content-Type:", response.headers.get("Content-Type", "lipseste"))
    print("content-type:", response.headers.get("content-type", "lipseste"))
    # Observ ca primesc aceeasi valoare: response.headers nu tine cont de litere mari sau mici.

    print("\nEx.13")
    print(response.text.lower().count("cyber"))
    # lower() returneaza tot un sir de caractere, deci pot apela count() direct pe rezultat.

    print("\nEx.14")
    html = response.text
    start = html.find("<title>") + len("<title>")
    end = html.find("</title>")
    print(html[start:end].strip())

    print("\nEx.15")
    lines = html.splitlines()
    print("linii:", len(lines))
    if lines:
        print("cea mai lunga:", len(max(lines, key=len)))

    print("\nEx.16")
    if response.url.startswith("https://"):
        print("Conexiune securizata")
    else:
        print("Conexiune nesecurizata")

    print("\nEx.17")
    time.sleep(1)
    redir = requests.get("http://cybercor.org", timeout=TIMEOUT)
    for item in redir.history:
        print(item.status_code, item.url)
    print("final:", redir.url)

    print("\nEx.18")
    time.sleep(1)
    head = requests.head(BASE_URL, timeout=TIMEOUT)
    time.sleep(1)
    get = requests.get(BASE_URL, timeout=TIMEOUT)
    print("HEAD:", len(head.content))
    print("GET:", len(get.content))
    # HEAD cere doar antetele, deci corpul are lungimea 0.
    # GET aduce si corpul paginii, de aceea lungimea este mare.

    print("\nEx.19")
    if response.cookies:
        for cookie in response.cookies:
            print(cookie.name, cookie.secure)
    else:
        print("Niciun cookie setat")

    print("\nEx.20")
    session = requests.Session()
    session.headers.update({"User-Agent": "WebLab-Barbuta-Victor"})
    time.sleep(1)
    r = session.get(ECHO_URL + "/headers", timeout=TIMEOUT)
    print("User-Agent trimis:", r.json()["headers"].get("User-Agent"))
    session.close()

    # Verificati-va: response.text este un atribut, adica o valoare deja pregatita.
    # response.json() este o metoda: face o actiune (transforma textul JSON in
    # dictionar), de aceea se apeleaza cu paranteze.


if __name__ == "__main__":
    main()
