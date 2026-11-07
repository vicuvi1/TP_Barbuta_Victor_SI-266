# -*- coding: utf-8 -*-
"""Laboratorul 8 - partea A. Scoate si numara esecurile din auth.log.
Generat din programul de laborator, cu codul scris de student."""
import re
from collections import Counter

TIPAR = re.compile(r"Failed password for (?:invalid user )?(\S+) from (\S+) port")


def esec(linie):
    """Sarcina 1. Scoate (user, ip) dintr-un rand de esec.

    Foloseste TIPAR, definit mai sus. Daca randul nu e un esec de
    autentificare, TIPAR.search intoarce None - atunci si tu intorci None.
    None nu e o eroare, e un semnal ca randul nu ne intereseaza.

    esec("x Failed password for root from 203.0.113.9 port 51230 ssh2")
        ->  ('root', '203.0.113.9')
    esec("<linie stricata>")  ->  None
    """
    m = TIPAR.search(linie)
    if m is None:
        return None
    return (m.group(1), m.group(2))

def citeste_esecuri(cale):
    """Sarcina 2. Lista de esecuri din fisier, robusta la randuri stricate.

    Parcurge fisierul si strange fisele {"user": ..., "ip": ...} intr-o
    lista. Randurile care nu sunt esecuri (esec intoarce None) se sar.

    Daca fisierul nu exista, prinde FileNotFoundError, scrie un mesaj si
    intoarce o lista goala - nu lasa programul sa crape.

    citeste_esecuri("start/auth.log")  ->  lista cu 15 dictionare
    """
    esecuri = []
    try:
        with open(cale, encoding="utf-8") as f:
            for linie in f:
                r = esec(linie)
                if r is not None:
                    esecuri.append({"user": r[0], "ip": r[1]})
    except FileNotFoundError:
        print("Fisierul nu exista:", cale)
        return []
    return esecuri

def pe_ip(esecuri):
    """Sarcina 3. Numara esecurile pe fiecare adresa IP.

    Primeste lista de la citeste_esecuri si intoarce un Counter al
    adreselor: cheia e IP-ul, valoarea de cate ori apare.

    Vezi Counter(e["ip"] for e in esecuri).
    """
    return Counter(e["ip"] for e in esecuri)

def rezumat(cale):
    """Sarcina 4. Leaga totul: citeste, numara, intoarce rezumatul.

    Intoarce un dictionar cu doua chei:
        {"esecuri": cate esecuri in total,
         "pe_ip": Counter-ul adreselor}

    Nu tipari nimic aici; doar intoarce. Afisarea o face programul.
    """
    esecuri = citeste_esecuri(cale)
    return {"esecuri": len(esecuri), "pe_ip": pe_ip(esecuri)}


# ---------------------------------------------------------------------------
#  PARTEA B - detectorul de brute force
# ---------------------------------------------------------------------------

def main():
    import sys
    cale = sys.argv[1] if len(sys.argv) > 1 else 'start/auth.log'
    esecuri = citeste_esecuri(cale)
    counts = pe_ip(esecuri)
    print('Esecuri de autentificare:', len(esecuri))
    for ip, n in counts.most_common():
        print('  %s: %d' % (ip, n))


if __name__ == '__main__':
    main()
