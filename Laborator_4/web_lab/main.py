# Laborator: functii, metode si importuri pe web
# Student: Barbuta Victor, SI-266
# Partea 5: programul care importa modulul webtools (exercitiile 44-50)

import argparse
import csv
import time
from datetime import datetime

import requests

import webtools
from webtools import DEFAULT_HEADERS, check_paths, get_title, security_headers, site_report

# Ex.45: daca main.py ar avea si o functie proprie numita get_title, definitia de aici
# ar inlocui numele importat, fiindca vine dupa import. Apelul get_title(...) ar folosi
# functia din main.py, iar cea din modul ar ramane disponibila doar ca webtools.get_title.

BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10  # secunde


def save_csv_report(url: str, filename: str = "report.csv") -> None:
    """Salveaza rezultatul functiei check_paths in report.csv."""
    result = check_paths(url, ["/", "/robots.txt", "/sitemap.xml"])
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["path", "status", "checked_at"])
        for path, status in result.items():
            writer.writerow([path, status, datetime.now().isoformat()])


def main() -> None:
    """Citeste URL-ul din linia de comanda si ruleaza proiectul final."""
    parser = argparse.ArgumentParser(description="Raport despre un site web")
    parser.add_argument("url", help="adresa site-ului, de exemplu https://cybercor.org")
    args = parser.parse_args()

    print("DEFAULT_HEADERS:", DEFAULT_HEADERS)

    try:
        response = webtools.fetch(args.url)
        print("Titlu (webtools.get_title):", webtools.get_title(response.text))
        print("Titlu (get_title):", get_title(response.text))

        time.sleep(1)
        print("Antete de securitate:", security_headers(args.url))

        time.sleep(1)
        save_csv_report(args.url)
        print("Salvat in report.csv")

        time.sleep(1)
        site_report(args.url)
    except requests.RequestException as error:
        print("Site-ul nu a putut fi verificat:", error)


if __name__ == "__main__":
    main()
