# Laborator: functii, metode si importuri pe web
# Student: Barbuta Victor, SI-266
# Partea 5: modulul meu, cu functiile reutilizabile (exercitiile 44-50)

import json
import re
import socket
import ssl
import time
from datetime import datetime
from urllib.parse import urljoin, urlparse

import requests

BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10  # secunde
DEFAULT_HEADERS = {"User-Agent": "WebLab-Barbuta-Victor"}


def fetch(url: str, timeout: int = 10) -> requests.Response:
    """Descarca un URL si returneaza raspunsul."""
    return requests.get(url, headers=DEFAULT_HEADERS, timeout=timeout)


def get_status(url: str) -> int:
    """Returneaza codul de stare HTTP."""
    return fetch(url).status_code


def get_title(html: str) -> str:
    """Returneaza titlul unei pagini HTML sau un sir gol daca titlul lipseste."""
    start = html.find("<title>")
    end = html.find("</title>")
    if start == -1 or end == -1:
        return ""
    return html[start + len("<title>"):end].strip()


def check_paths(base: str, paths: list) -> dict:
    """Verifica o lista de cai."""
    result = {}
    for i, path in enumerate(paths):
        if i:
            time.sleep(1)
        try:
            result[path] = fetch(base.rstrip("/") + path).status_code
        except requests.RequestException:
            result[path] = None
    return result


def security_headers(url: str) -> dict:
    """Verifica antetele de securitate."""
    names = [
        "Strict-Transport-Security",
        "Content-Security-Policy",
        "X-Frame-Options",
        "X-Content-Type-Options",
        "Referrer-Policy",
    ]
    r = fetch(url)
    return {name: name in r.headers for name in names}


def score_headers(results: dict) -> str:
    """Calculeaza scorul antetelor."""
    return str(sum(results.values())) + "/" + str(len(results))


def fetch_robots(base: str):
    """Returneaza textul din robots.txt sau None daca fisierul lipseste.

    Unele site-uri raspund cu o pagina HTML in loc de 404; si atunci fisierul lipseste.
    """
    try:
        r = fetch(base.rstrip("/") + "/robots.txt")
        if r.status_code == 404:
            return None
        if "text/html" in r.headers.get("Content-Type", ""):
            return None
        return r.text
    except requests.RequestException:
        return None


def disallowed_paths(text) -> list:
    """Extrage caile Disallow."""
    if not text:
        return []
    result = []
    for line in text.splitlines():
        if line.lower().strip().startswith("disallow:"):
            value = line.split(":", 1)[1].strip()
            if value:
                result.append(value)
    return result


def extract_links(html: str) -> list:
    """Extrage linkurile din HTML."""
    links = re.findall(r'href="([^"]+)"', html)
    return list(dict.fromkeys(links))


def split_links(links: list, base: str):
    """Imparte linkurile in interne si externe."""
    domain = urlparse(base).netloc
    internal = []
    external = []
    for link in links:
        full = urljoin(base, link)
        if urlparse(full).netloc == domain:
            internal.append(full)
        else:
            external.append(full)
    return internal, external


def resolve(hostname: str):
    """Returneaza IP-ul domeniului."""
    try:
        return socket.gethostbyname(hostname)
    except socket.gaierror:
        return None


def cert_days_left(hostname: str):
    """Returneaza zilele ramase pentru certificat."""
    try:
        context = ssl.create_default_context()
        with socket.create_connection((hostname, 443), timeout=TIMEOUT) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as s:
                cert = s.getpeercert()
        expires = ssl.cert_time_to_seconds(cert["notAfter"])
        return int((expires - time.time()) / 86400)
    except (OSError, ssl.SSLError, KeyError):
        return None


def redirect_chain(url: str) -> list:
    """Returneaza redirectionarile pornind de la http://, in forma "301 -> adresa"."""
    host = urlparse(url).netloc
    try:
        r = fetch("http://" + host)
    except requests.RequestException:
        return []
    urls = [step.url for step in r.history] + [r.url]
    chain = []
    for i, step in enumerate(r.history):
        chain.append(str(step.status_code) + " -> " + urls[i + 1])
    return chain


def site_report(url: str, filename: str = "report.json") -> dict:
    """Genereaza raportul final si il salveaza in JSON."""
    r = fetch(url)
    r.raise_for_status()

    final_url = r.url
    host = urlparse(final_url).hostname
    links = extract_links(r.text)
    internal, external = split_links(links, final_url)

    time.sleep(1)
    headers = security_headers(final_url)
    time.sleep(1)
    robots = fetch_robots(final_url)
    time.sleep(1)
    redirects = redirect_chain(final_url)

    report = {
        "checked_at": datetime.now().isoformat(),
        "status_code": r.status_code,
        "final_url": final_url,
        "title": get_title(r.text),
        "ip_address": resolve(host),
        "redirect_chain": redirects,
        "security_score": score_headers(headers),
        "certificate_days_left": cert_days_left(host),
        "internal_links": len(internal),
        "external_links": len(external),
        "disallowed_paths": disallowed_paths(robots),
    }

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(report, file, indent=2, ensure_ascii=False)

    print("=== Raport site:", url, "===")
    print("Cod de stare:", report["status_code"])
    print("URL final:", report["final_url"])
    print("Titlu:", report["title"])
    print("Adresa IP:", report["ip_address"])
    print("Redirectionari:", ", ".join(redirects) or "niciuna")
    print("Scor securitate:", report["security_score"])
    print("Certificat:", report["certificate_days_left"], "de zile ramase")
    print("Legaturi:", report["internal_links"], "interne,", report["external_links"], "externe")
    print("Cai interzise:", ", ".join(report["disallowed_paths"]) or "niciuna")
    print("Salvat in", filename)

    return report


# Ex.46: cand rulez python webtools.py, Python pune in __name__ valoarea "__main__",
# deci autotestul porneste. Cand main.py face import webtools, __name__ este
# "webtools", conditia este falsa si autotestul nu mai ruleaza.
if __name__ == "__main__":
    print("Autotest:", get_status("https://cybercor.org"))
