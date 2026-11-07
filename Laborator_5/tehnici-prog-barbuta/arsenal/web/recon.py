import os
import sys
import re
import json
import argparse

sys.path.insert(0, os.getcwd())

from arsenal.web.client import cere

IMPLICITE = ["admin", "login", "backup", "config", "test", "uploads", "phpmyadmin"]


def fingerprint(tinta):
    r = cere(tinta)
    return r.status_code, r.headers.get("Server"), r.headers.get("X-Powered-By")


def robots(tinta):
    r = cere(tinta + "/robots.txt")
    if r.status_code != 200:
        return []
    return [l for l in r.text.splitlines() if l.strip().startswith("Disallow:")]


def descopera(tinta, cuvinte):
    gasite = []
    for c in cuvinte:
        r = cere(tinta + "/" + c)
        if r.status_code == 200:
            gasite.append(c)
        elif r.status_code == 403:
            print("interzis (interesant):", c)
    return gasite


def linkuri(tinta):
    r = cere(tinta + "/")
    return sorted(set(re.findall(r'href="([^"]+)"', r.text)))


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("tinta")
    p.add_argument("--wordlist", default=None)
    a = p.parse_args()
    if a.wordlist:
        cuvinte = [l.strip() for l in open(a.wordlist) if l.strip()]
    else:
        cuvinte = IMPLICITE
    cod, server, powered = fingerprint(a.tinta)
    print("cod:", cod)
    print("Server:", server)
    print("X-Powered-By:", powered)
    disallow = robots(a.tinta)
    print("robots Disallow:", disallow)
    gasite = descopera(a.tinta, cuvinte)
    print("gasite:", gasite)
    print("linkuri:", linkuri(a.tinta))
    fisa = {"tinta": a.tinta, "server": server, "directoare": gasite}
    json.dump(fisa, open("arsenal/web/fisa.json", "w"), indent=2)
    print("fisa salvata:", fisa)
