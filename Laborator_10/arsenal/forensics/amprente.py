# -*- coding: utf-8 -*-
"""arsenal/forensics/amprente.py - unealta de forensics (tip, amprenta, scanare)."""
import os, hashlib

MAGIC = {b"\x89PNG": "PNG", b"%PDF": "PDF", b"PK\x03\x04": "ZIP"}


def tip(head):
    """Sarcina 1. Tipul fisierului dupa primii octeti (magic bytes).

    Pentru fiecare (semnatura, nume) din MAGIC: daca head.startswith(semnatura)
    intoarce nume. DUPA bucla, daca nimic nu s-a potrivit, intoarce "necunoscut".

    tip(b"\\x89PNG\\r\\n") -> "PNG"      tip(b"%PDF-1.4") -> "PDF"
    tip(b"text")          -> "necunoscut"

    ATENTIE: return "necunoscut" trebuie sa fie DUPA bucla, nu inauntru.
    Daca e in bucla, functia verifica doar prima semnatura si apoi renunta.
    """
    for semnatura, nume in MAGIC.items():
        if head.startswith(semnatura):
            return nume
    return "necunoscut"

def amprenta_fisier(cale):
    """Sarcina 2. Fisa unui fisier, citit in binar cu with.

    Deschide fisierul in mod binar ("rb") cu with, citeste octetii, si intoarce
    un dictionar:
        {"nume": numele fisierului (os.path.basename),
         "tip": tip(primii 8 octeti),
         "sha256": hashlib.sha256(octeti).hexdigest() - PRIMELE 16 caractere}

    amprenta_fisier(".../imagine.png")
        -> {'nume': 'imagine.png', 'tip': 'PNG', 'sha256': 'ea3a9848da7e6c1d'}

    Deschizi cu "rb" fiindca un PNG e octeti, nu text. Si cu with, ca fisierul
    sa se inchida singur.
    """
    with open(cale, "rb") as f:      # "rb" = binar; with = inchide singur
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

def formateaza(fisa):
    """Sarcina 4. Un rand frumos pentru un fisier, gata de tiparit.

    Intoarce un sir cu numele (latime 14), tipul (latime 11) si amprenta,
    despartite prin cate un spatiu. Foloseste f-string cu latimi:

        f"{nume:14} {tip:11} {sha256}"

    formateaza({'nume':'imagine.png','tip':'PNG','sha256':'ea3a9848da7e6c1d'})
        -> "imagine.png    PNG         ea3a9848da7e6c1d"
    """
    return f"{fisa['nume']:14} {fisa['tip']:11} {fisa['sha256']}"

def main():
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument('folder')
    a = p.parse_args()
    for fisa in scaneaza(a.folder):
        print(formateaza(fisa))


if __name__ == '__main__':
    main()
