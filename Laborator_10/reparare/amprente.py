# -*- coding: utf-8 -*-
"""reparare/amprente.py - unealta reparata (cele 3 greseli corectate)."""
import os, hashlib

MAGIC = {b"\x89PNG": "PNG", b"%PDF": "PDF", b"PK\x03\x04": "ZIP"}


def tip(head):
    """Sarcina 5. Repara aceasta functie (are o greseala)."""
    for semnatura, nume in MAGIC.items():
        if head.startswith(semnatura):
            return nume
    return "necunoscut"

def amprenta_fisier(cale):
    """Sarcina 6. Repara aceasta functie (are doua greseli)."""
    with open(cale, "rb") as f:
        date = f.read()
    return {"nume": os.path.basename(cale),
            "tip": tip(date[:8]),
            "sha256": hashlib.sha256(date).hexdigest()[:16]}

def scaneaza(folder):
    """Sarcina 3. Amprenteaza toate fisierele dintr-un folder.

    Parcurge fisierele folderului in ordine si intoarce o lista de fise
    (cate o amprenta_fisier pentru fiecare fisier).

    scaneaza(".../probe") -> lista cu 4 fise
    """
    rez = []
    for nume in sorted(os.listdir(folder)):
        cale = os.path.join(folder, nume)
        if os.path.isfile(cale):
            rez.append(amprenta_fisier(cale))
    return rez
