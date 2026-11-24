# -*- coding: utf-8 -*-
"""
===============================================================================

   LUCRAREA DE LABORATOR NR. 10  -  with SI pytest
   Forensics: o unealta de incredere, cu resurse sigure si teste

   Universitatea Tehnica a Moldovei
   Facultatea Calculatoare, Informatica si Microelectronica
   Disciplina: Tehnici de programare        Anul I, grupele SI-265 / SI-266

===============================================================================

   CUM PORNESTI

   1. Deschide linia de comanda in folderul unde se afla acest fisier.
      In Windows: intra in folder, scrie  cmd  in bara de adresa si Enter.
      NU porni prin dublu-clic si nici din butonul Run al editorului: are
      nevoie de un terminal ca sa iti poata citi tastatura.

   2. Porneste programul:

          python L10_TP_Nume_Prenume_SI-26x.py

   3. Iti apare un meniu. Incepe cu optiunea  c , "Cum se lucreaza".

   -----------------------------------------------------------------------

   CE AI DE FACUT

   Transformi un script intr-o unealta de incredere. Scrii o unealta de
   forensics care citeste fisiere ridicate de pe o tinta: le afla tipul dupa
   primii octeti (magic bytes) si le calculeaza amprenta SHA-256, cu  with
   peste tot (fisierul se inchide singur).

   Partea A - unealta de forensics             4 sarcini
   Partea B - repari unealta stricata          2 sarcini
   Bonus    - un generator cu yield            1 sarcina (optional)

   Fiecare sarcina din A si B valoreaza un punct. Bonusul nu scade nota.

   Functiile au un  # TODO  si se termina cu  raise NotImplementedError.
   La reparare (Partea B) codul e deja scris, dar STRICAT: il repari.
   Scrii / repari, SALVEZI fisierul si apesi Enter in fereastra programului.

   -----------------------------------------------------------------------

   PROBELE

   La prima pornire, programul creeaza singur folderul  start/probe/  cu
   patru fisiere de examinat: imagine.png, raport.pdf, arhiva.zip, note.txt.
   Nu ai nimic de descarcat. Amprenta fiecaruia e fixa: daca fisierul se
   schimba cu un singur octet, amprenta se schimba complet.

===============================================================================
"""
import base64
import hashlib
import io
import os
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

VERSIUNE = "L10-v1"
DOSAR = os.path.dirname(os.path.abspath(sys.argv[0])) or os.getcwd()
START = os.path.join(DOSAR, "start")
PROBE = os.path.join(START, "probe")

# Multe fisiere incep cu o semnatura fixa (magic bytes): un PNG cu \x89PNG,
# un PDF cu %PDF, un ZIP cu PK\x03\x04.
MAGIC = {b"\x89PNG": "PNG", b"%PDF": "PDF", b"PK\x03\x04": "ZIP"}


# ===========================================================================
#
#    A I C I   S C R I I   T U
#
#    Partea A: scrii functiile (au # TODO si raise NotImplementedError).
#    Partea B: repari functiile STRICATE (tip_r, amprenta_r) - au greseli.
#    Bonus: scrii un generator.
#
# ===========================================================================

# ---------------------------------------------------------------------------
#  PARTEA A - unealta de forensics
# ---------------------------------------------------------------------------

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


# ---------------------------------------------------------------------------
#  PARTEA B - repari unealta stricata (3 greseli)
#
#  Functiile de mai jos sunt o copie STRICATA a uneltei. Au trei greseli,
#  marcate cu "greseala N". Le repari pe rand, pana cand sarcinile 5 si 6 trec.
#  NU schimba ce intorc (contractul), doar repara greselile.
# ---------------------------------------------------------------------------

def tip_r(head):
    """Sarcina 5. Repara aceasta functie (are o greseala)."""
    for semnatura, nume in MAGIC.items():
        if head.startswith(semnatura):
            return nume
    return "necunoscut"


def amprenta_r(cale):
    """Sarcina 6. Repara aceasta functie (are doua greseli)."""
    with open(cale, "rb") as f:
        date = f.read()
    return {"nume": os.path.basename(cale),
            "tip": tip_r(date[:8]),
            "sha256": hashlib.sha256(date).hexdigest()[:16]}


# ---------------------------------------------------------------------------
#  BONUS (optional) - un generator cu yield
# ---------------------------------------------------------------------------

def amprente_lenes(folder):
    """Sarcina 7 (bonus). La fel ca scaneaza, dar produce fisele una cate una,
    cu yield, fara sa tina toata lista in memorie.

    Parcurge fisierele in ordine si, pentru fiecare fisier, face
        yield amprenta_fisier(cale)

    list(amprente_lenes(folder)) trebuie sa dea acelasi lucru ca scaneaza(folder).
    """
    for nume in sorted(os.listdir(folder)):
        cale = os.path.join(folder, nume)
        if os.path.isfile(cale):
            yield amprenta_fisier(cale)


#  @@ AICI SE TERMINA ZONA TA @@
# ===========================================================================

# Marcajul e lipit din doua bucati dinadins: altfel randul acesta ar contine
# el insusi textul cautat, iar taierea ar cadea in mijlocul lui.
MARCAJ_ZONA = "@@ AICI SE TERMINA " + "ZONA TA @@"

# Cele patru probe, minuscule si fictive, incepute cu magic bytes reale.
# Amprenta fiecareia e fixa; de aici valorile cunoscute din AMPRENTE.
PROBE_B64 = {
    "imagine.png": "iVBORw0KGgoAAAANSUhEUmRhdGUtZmljdGl2ZS1kZS1pbWFnaW5lLWFpY2k=",
    "raport.pdf": "JVBERi0xLjQKMSAwIG9iajw8Pj5lbmRvYmogdHJhaWxlciBmaWN0aXY=",
    "arhiva.zip": "UEsDBGNvbnRpbnV0LWZpY3Rpdi1kZS1hcmhpdmE=",
    "note.txt": "cGFyb2xhIGdhc2l0YTogaHVudGVyMgpjb250OiBhbmEK",
}

AMPRENTE = {"imagine.png": "ea3a9848da7e6c1d", "raport.pdf": "9023842e09242e5d",
            "arhiva.zip": "e026715077436f53", "note.txt": "27f8884260c60ec9"}
TIPURI = {"imagine.png": "PNG", "raport.pdf": "PDF",
          "arhiva.zip": "ZIP", "note.txt": "necunoscut"}


def pregateste_probele(unde=PROBE):
    """Scrie folderul probe/ cu cele patru fisiere la prima pornire."""
    nou = False
    if not os.path.isdir(unde):
        os.makedirs(unde)
        nou = True
    for nume, b64 in PROBE_B64.items():
        cale = os.path.join(unde, nume)
        if not os.path.exists(cale):
            open(cale, "wb").write(base64.b64decode(b64))
            nou = True
    return nou


# ---------------------------------------------------------------------------
#  Reincarcarea codului scris de student
# ---------------------------------------------------------------------------
def reincarca_codul():
    """Reciteste de pe disc zona in care scrii tu si actualizeaza functiile.
    Intoarce (reusit, mesaj_de_eroare)."""
    try:
        cale = os.path.abspath(sys.argv[0])
        sursa = io.open(cale, encoding="utf-8").read()
    except Exception as e:
        return False, "Nu pot reciti fisierul de pe disc: " + str(e)
    taietura = sursa.find(MARCAJ_ZONA)
    if taietura == -1:
        return False, "Nu gasesc randul de separare din fisier."
    zona = sursa[:taietura]
    spatiu = {}
    try:
        exec(compile(zona, cale, "exec"), spatiu)
    except IndentationError as e:
        return False, ("Indentare gresita la randul " + str(e.lineno) + "."
                       + chr(10) + "Codul dintr-o functie se scrie cu 4 spatii "
                       "mai la dreapta decat def.")
    except SyntaxError as e:
        return False, ("Greseala de scriere la randul " + str(e.lineno) +
                       ":" + chr(10) + str(e.msg) + chr(10) +
                       "Verifica ghilimelele, parantezele si cele doua puncte.")
    except Exception as e:
        return False, ("Codul tau a dat eroare cand a fost incarcat:" +
                       chr(10) + type(e).__name__ + ": " + str(e))
    g = globals()
    for n, v in spatiu.items():
        if not n.startswith("__"):
            g[n] = v
    return True, ""


def _scurt(v, maxim=60):
    t = repr(v)
    return t if len(t) <= maxim else t[:maxim - 3] + "..."


# ---------------------------------------------------------------------------
#  Verificatorii fiecarei sarcini
# ---------------------------------------------------------------------------
def v_tip():
    f = globals()["tip"]
    cazuri = [(b"\x89PNG\r\n", "PNG"), (b"%PDF-1.4", "PDF"),
              (b"PK\x03\x04abcd", "ZIP"), (b"text oarecare", "necunoscut")]
    for head, astept in cazuri:
        got = f(head)
        if got != astept:
            return False, ("tip(%r) ar trebui sa dea %r, a dat %r." %
                           (head, astept, got))
    return True, "Corect."


def v_amprenta():
    f = globals()["amprenta_fisier"]
    r = f(os.path.join(PROBE, "imagine.png"))
    if not isinstance(r, dict):
        return False, "amprenta_fisier trebuie sa intoarca un dictionar."
    for ch in ("nume", "tip", "sha256"):
        if ch not in r:
            return False, "Lipseste cheia '%s' din fisa." % ch
    if r["nume"] != "imagine.png":
        return False, "nume ar trebui sa fie 'imagine.png', e %r." % r.get("nume")
    if r["tip"] != "PNG":
        return False, "tip ar trebui sa fie 'PNG', e %r." % r.get("tip")
    if r["sha256"] != AMPRENTE["imagine.png"]:
        return False, ("sha256 ar trebui sa fie %r (primele 16 caractere), e %r."
                       % (AMPRENTE["imagine.png"], r.get("sha256")))
    return True, "Corect."


def v_scaneaza():
    f = globals()["scaneaza"]
    rez = f(PROBE)
    if not isinstance(rez, list) or len(rez) != 4:
        return False, "scaneaza(probe) ar trebui sa dea o lista cu 4 fise."
    tipuri = {x.get("tip") for x in rez if isinstance(x, dict)}
    if tipuri != {"PNG", "PDF", "ZIP", "necunoscut"}:
        return False, "Tipurile gasite nu sunt cele asteptate: " + _scurt(tipuri)
    return True, "Corect."


def v_formateaza():
    f = globals()["formateaza"]
    fisa = {"nume": "imagine.png", "tip": "PNG", "sha256": "ea3a9848da7e6c1d"}
    astept = "imagine.png    PNG         ea3a9848da7e6c1d"
    got = f(fisa)
    if got != astept:
        return False, ("Randul nu e cel asteptat." + chr(10) +
                       "   asteptat: %r" % astept + chr(10) +
                       "   primit:   %r" % got)
    return True, "Corect."


def v_tip_r():
    f = globals()["tip_r"]
    for head, astept in [(b"\x89PNG", "PNG"), (b"%PDF-1.4", "PDF"),
                         (b"PK\x03\x04", "ZIP"), (b"text", "necunoscut")]:
        got = f(head)
        if got != astept:
            return False, ("Inca e stricata: tip_r(%r) da %r, trebuie %r."
                           % (head, got, astept) + chr(10) +
                           "   Greseala 1: return \"necunoscut\" e in bucla; "
                           "mut-l DUPA bucla.")
    return True, "Reparata."


def v_amprenta_r():
    f = globals()["amprenta_r"]
    try:
        r = f(os.path.join(PROBE, "imagine.png"))
    except Exception as e:
        return False, ("Inca e stricata: arunca " + type(e).__name__ +
                       " cand citeste un PNG." + chr(10) +
                       "   Greseala 2: deschide fisierul in binar, cu open(cale, \"rb\").")
    if r.get("sha256") != AMPRENTE["imagine.png"]:
        return False, ("Amprenta e %r, trebuie %r." %
                       (r.get("sha256"), AMPRENTE["imagine.png"]) + chr(10) +
                       "   Greseala 3: ia primele 16 caractere din hexdigest(), nu 8.")
    return True, "Reparata."


def v_lenes():
    f = globals()["amprente_lenes"]
    sc = globals()["scaneaza"]
    got = list(f(PROBE))
    if got != sc(PROBE):
        return False, "list(amprente_lenes(probe)) trebuie sa dea la fel ca scaneaza(probe)."
    import inspect
    if "yield" not in inspect.getsource(f):
        return False, "Foloseste yield (altfel nu e generator)."
    return True, "Corect."


def verifica_sarcina(s):
    """Intoarce (reusit, mesaj)."""
    if globals().get(s["cheie_functie"]) is None:
        return False, "Nu gasesc " + s["cheie_functie"] + " in fisier."
    try:
        return s["verificator"]()
    except NotImplementedError:
        return False, ("Inca e stricata." if s["parte"] == "B"
                       else "Sarcina nu este inca rezolvata.")
    except Exception as e:
        return False, ("Codul tau a dat eroare:" + chr(10) + "         "
                       + type(e).__name__ + ": " + str(e))


def stare_completa(reincarca=True):
    if reincarca:
        ok, mesaj = reincarca_codul()
        if not ok:
            return None, mesaj
    out = []
    for s in SARCINI:
        reusit, mesaj = verifica_sarcina(s)
        out.append((s, reusit, mesaj))
    return out, ""


def punctaj(stare):
    return sum(1 for s, reusit, _ in stare if reusit and not s.get("bonus"))


def punctaj_bonus(stare):
    return sum(1 for s, reusit, _ in stare if reusit and s.get("bonus"))


# ---------------------------------------------------------------------------
#  Sarcinile
# ---------------------------------------------------------------------------
SARCINI = [
    {"nr": 1, "parte": "A", "cheie_functie": "tip",
     "titlu": "Tipul dupa magic bytes",
     "indiciu": "bucla peste MAGIC; return \"necunoscut\" DUPA bucla.",
     "verificator": v_tip},
    {"nr": 2, "parte": "A", "cheie_functie": "amprenta_fisier",
     "titlu": "Amprenta unui fisier (cu with)",
     "indiciu": "intoarce dict cu nume, tip(date[:8]), sha256 primele 16 caractere.",
     "verificator": v_amprenta},
    {"nr": 3, "parte": "A", "cheie_functie": "scaneaza",
     "titlu": "Scanezi tot folderul",
     "indiciu": "rez.append(amprenta_fisier(cale)).",
     "verificator": v_scaneaza},
    {"nr": 4, "parte": "A", "cheie_functie": "formateaza",
     "titlu": "Un rand frumos pentru tiparit",
     "indiciu": "f\"{fisa['nume']:14} {fisa['tip']:11} {fisa['sha256']}\".",
     "verificator": v_formateaza},

    {"nr": 5, "parte": "B", "cheie_functie": "tip_r",
     "titlu": "Repari tip_r (greseala 1)",
     "indiciu": "muta return \"necunoscut\" dupa bucla (scoate-l din if/bucla).",
     "verificator": v_tip_r},
    {"nr": 6, "parte": "B", "cheie_functie": "amprenta_r",
     "titlu": "Repari amprenta_r (greselile 2 si 3)",
     "indiciu": "open(cale, \"rb\") si hexdigest()[:16].",
     "verificator": v_amprenta_r},

    {"nr": 7, "parte": "Bonus", "cheie_functie": "amprente_lenes", "bonus": True,
     "titlu": "Generator cu yield (optional)",
     "indiciu": "yield amprenta_fisier(cale) in loc de append.",
     "verificator": v_lenes},
]
NR_CORE = sum(1 for s in SARCINI if not s.get("bonus"))


# ---------------------------------------------------------------------------
#  Ce se vede pe ecran
# ---------------------------------------------------------------------------
LAT = 74


def linie(ch="-"):
    print(ch * LAT)


def titlu(text, ch="="):
    print()
    linie(ch)
    print("  " + text)
    linie(ch)


def bara(cate, din, latime=34):
    plin = int(round(latime * cate / float(din))) if din else 0
    return "[" + "#" * plin + "." * (latime - plin) + "]"


def nota_din(p):
    return max(1, round(10 * p / float(NR_CORE))) if p else 0


def harta(stare):
    """Ancheta de forensics, care se completeaza pe masura ce rezolvi.
    Fiecare rand e un pas al analizei, aprins cu date adevarate cand rezolvi
    sarcina care il produce."""
    gata = set(s["nr"] for s, reusit, _ in stare if reusit)

    def are(*nrs):
        return all(n in gata for n in nrs)

    def rand(eticheta, deblocat, text, cheie):
        tinta = text if deblocat else "in ceata ... (rezolva %s)" % cheie
        marcaj = " +" if deblocat else "  "
        print("  %s %-12s %s" % (marcaj, eticheta, tinta[:52]))

    titlu("PROBELE RIDICATE DE PE TINTA", "-")
    print()
    rand("tip:", are(1), "stiu tipul dupa primii octeti (magic bytes)", "sarcina 1")
    rand("amprenta:", are(2), "imagine.png -> PNG, %s" % AMPRENTE["imagine.png"],
         "sarcina 2")
    rand("scanare:", are(3), "4 probe amprentate", "sarcina 3")
    rand("raport:", are(4), "un rand aliniat pentru fiecare proba", "sarcina 4")
    print()
    rand("reparat 1:", are(5), "unealta stricata: tipul iese corect", "sarcina 5")
    rand("reparat 2:", are(6), "unealta stricata: amprenta iese corect", "sarcina 6")
    if any(s.get("bonus") for s, _, _ in stare):
        rand("bonus:", are(7), "generator lenes, fisa cu fisa (yield)", "sarcina 7")
    print()
    if are(1, 2, 3, 4, 5, 6):
        print("  >>> Unealta e de incredere: cu with peste tot si teste care pot pica. <<<")
    else:
        print("  Rezolva sarcinile ca sa risipesti ceata de pe probe.")


def arata_progres(stare):
    titlu("LABORATORUL 10  -  with SI pytest", "=")
    p = punctaj(stare)
    b = punctaj_bonus(stare)
    print()
    print("  " + bara(p, NR_CORE) + "   %d din %d sarcini%s" %
          (p, NR_CORE, ("  (+bonus)" if b else "")))
    harta(stare)
    print()
    parte = None
    for s, reusit, mesaj in stare:
        if s["parte"] != parte:
            parte = s["parte"]
            print("  PARTEA %s" % parte if parte != "Bonus" else "  BONUS")
        semn = "[x]" if reusit else "[ ]"
        print("   %s %2d. %-34s %s" % (semn, s["nr"], s["titlu"],
                                       "" if reusit else mesaj.split(chr(10))[0][:26]))
    print()
    print("  Nota ta acum (din 10): %d" % nota_din(p))


def arata_sarcina(s, reusit, mesaj):
    eticheta = "SARCINA %d  (%s)  -  %s" % (s["nr"], s["parte"], s["titlu"])
    titlu(eticheta)
    print()
    tinta = globals().get(s["cheie_functie"])
    doc = (getattr(tinta, "__doc__", None) or "") if tinta else ""
    for r in doc.strip().split(chr(10)):
        print("   " + r.strip())
    print()
    if reusit:
        print("   REZOLVATA." if s["parte"] != "B" else "   REPARATA.")
    else:
        print("   Inca nu merge:")
        for r in mesaj.split(chr(10)):
            print("      " + r)
        print()
        print("   Indiciu: " + s["indiciu"])


def _tine_fereastra_deschisa():
    if os.name == "nt" and sys.stdout.isatty():
        try:
            os.system("pause")
        except Exception:
            pass


def iesire_fara_terminal():
    print()
    print("   " + "!" * 66)
    print("   Programul s-a inchis fiindca NU a fost pornit dintr-un terminal")
    print("   si nu poate citi tastatura (de obicei, cand dai dublu-clic sau")
    print("   il pornesti din butonul Run al editorului).")
    print()
    print("   Porneste-l asa:")
    print("     1. Intra in folderul unde se afla acest fisier.")
    print("     2. Scrie  cmd  in bara de adresa a ferestrei si apasa Enter.")
    print("     3. In fereastra neagra scrie:")
    print()
    print("          python " + os.path.basename(sys.argv[0]))
    print("   " + "!" * 66)
    _tine_fereastra_deschisa()
    raise SystemExit


def asteapta():
    try:
        input()
    except EOFError:
        iesire_fara_terminal()
    except KeyboardInterrupt:
        raise SystemExit


def instructiuni():
    titlu("CUM SE LUCREAZA")
    print("""
   1. Lasa acest program pornit, intr-un terminal (cmd).

   2. Deschide fisierul  L10_TP_Nume_Prenume_SI-26x.py  intr-un editor.

   3. PARTEA A: completezi functiile tip, amprenta_fisier, scaneaza,
      formateaza. Fiecare are un  # TODO  si se termina cu
      raise NotImplementedError.

   4. PARTEA B: functiile tip_r si amprenta_r sunt o copie STRICATA a uneltei.
      Au trei greseli (marcate cu "greseala N"). Le repari pana cand sarcinile
      5 si 6 trec. NU le schimba contractul, doar repara greselile.

   5. SALVEZI fisierul.

   6. Vii inapoi in aceasta fereastra si apesi Enter. Programul reciteste
      fisierul si iti spune imediat ce merge si ce nu.

   Probele sunt in  start/probe/ , create la prima pornire. Amprenta fiecareia
   e fixa: daca fisierul se schimba cu un octet, amprenta se schimba complet.
""")


# ---------------------------------------------------------------------------
#  Predarea: scrie fisierele cerute in fisa
# ---------------------------------------------------------------------------
def _extrage(zona, nume):
    """Scoate sursa functiei `nume` din zona studentului."""
    linii = zona.split(chr(10))
    out, luam = [], False
    for ln in linii:
        cap = ln.startswith("def " + nume + "(") or ln.startswith("def " + nume + " ")
        if cap:
            luam = True
            out.append(ln)
            continue
        if luam:
            if ln.strip() == "" or ln[:1] in (" ", "\t"):
                out.append(ln)
            else:
                break
    while out and out[-1].strip() == "":
        out.pop()
    return chr(10).join(out)


ANTET_AMPRENTE = (
    "# -*- coding: utf-8 -*-" + chr(10) +
    '"""arsenal/forensics/amprente.py - unealta de forensics (tip, amprenta, scanare)."""'
    + chr(10) + "import os, hashlib" + chr(10) + chr(10) +
    r'MAGIC = {b"\x89PNG": "PNG", b"%PDF": "PDF", b"PK\x03\x04": "ZIP"}' +
    chr(10) + chr(10) + chr(10))

MAIN_AMPRENTE = (chr(10) + chr(10) +
    "def main():" + chr(10) +
    "    import argparse" + chr(10) +
    "    p = argparse.ArgumentParser()" + chr(10) +
    "    p.add_argument('folder')" + chr(10) +
    "    a = p.parse_args()" + chr(10) +
    "    for fisa in scaneaza(a.folder):" + chr(10) +
    "        print(formateaza(fisa))" + chr(10) +
    chr(10) + chr(10) + "if __name__ == '__main__':" + chr(10) + "    main()" + chr(10))

TEST_AMPRENTE = (
    "# -*- coding: utf-8 -*-" + chr(10) +
    '"""Trei teste care dovedesc ca unealta merge (ruleaza din radacina depozitului:'
    + chr(10) + '   python -m pytest -q arsenal/forensics/test_amprente.py)."""' + chr(10) +
    "import os" + chr(10) +
    "from arsenal.forensics.amprente import tip, amprenta_fisier, scaneaza" + chr(10) +
    'PROBE = os.path.join(os.path.dirname(__file__), "probe")' + chr(10) + chr(10) + chr(10) +
    "def test_tip_din_magic():" + chr(10) +
    '    assert tip(b"\\x89PNG") == "PNG"' + chr(10) +
    '    assert tip(b"text") == "necunoscut"' + chr(10) + chr(10) + chr(10) +
    "def test_amprenta_png():" + chr(10) +
    '    r = amprenta_fisier(os.path.join(PROBE, "imagine.png"))' + chr(10) +
    '    assert r["sha256"] == "ea3a9848da7e6c1d"' + chr(10) + chr(10) + chr(10) +
    "def test_scaneaza_toate():" + chr(10) +
    "    assert len(scaneaza(PROBE)) == 4" + chr(10))

ANTET_REPARARE = (
    "# -*- coding: utf-8 -*-" + chr(10) +
    '"""reparare/amprente.py - unealta reparata (cele 3 greseli corectate)."""' + chr(10) +
    "import os, hashlib" + chr(10) + chr(10) +
    r'MAGIC = {b"\x89PNG": "PNG", b"%PDF": "PDF", b"PK\x03\x04": "ZIP"}' +
    chr(10) + chr(10) + chr(10))

TEST_REPARARE = (
    "# -*- coding: utf-8 -*-" + chr(10) +
    "# Teste pentru Lucrarea B. NU le modifica: descriu cum TREBUIE sa se poarte unealta." + chr(10) +
    "# Ruleaza cu: python -m pytest -q   (din folderul reparare/)" + chr(10) +
    "import os" + chr(10) +
    "from amprente import tip, amprenta_fisier, scaneaza" + chr(10) +
    'PROBE = os.path.join(os.path.dirname(__file__), "probe")' + chr(10) + chr(10) + chr(10) +
    "def test_tip_din_magic():" + chr(10) +
    '    assert tip(b"\\x89PNG\\r\\n") == "PNG"' + chr(10) +
    '    assert tip(b"%PDF-1.4") == "PDF"' + chr(10) +
    '    assert tip(b"text oarecare") == "necunoscut"' + chr(10) + chr(10) + chr(10) +
    "def test_amprenta_png():" + chr(10) +
    '    r = amprenta_fisier(os.path.join(PROBE, "imagine.png"))' + chr(10) +
    '    assert r["tip"] == "PNG"' + chr(10) +
    '    assert r["sha256"] == "ea3a9848da7e6c1d"' + chr(10) + chr(10) + chr(10) +
    "def test_scaneaza_toate():" + chr(10) +
    "    rez = scaneaza(PROBE)" + chr(10) +
    "    assert len(rez) == 4" + chr(10) +
    '    assert {f["tip"] for f in rez} == {"PNG", "PDF", "ZIP", "necunoscut"}' + chr(10))


def _scrie_probe(dest):
    os.makedirs(dest, exist_ok=True)
    for nume, b64 in PROBE_B64.items():
        open(os.path.join(dest, nume), "wb").write(base64.b64decode(b64))


def pregateste_predarea(stare):
    nerez_a = [s["nr"] for s, reusit, _ in stare
               if not reusit and s["parte"] in ("A", "B")]
    sursa = io.open(os.path.abspath(sys.argv[0]), encoding="utf-8").read()
    zona = sursa[:sursa.find(MARCAJ_ZONA)]

    LUCRARE = os.path.join(DOSAR, "Laborator_10")
    # --- Lucrarea A: arsenal/forensics/ ---
    fdir = os.path.join(LUCRARE, "arsenal", "forensics")
    os.makedirs(fdir, exist_ok=True)
    open(os.path.join(LUCRARE, "arsenal", "__init__.py"), "w", encoding="utf-8").write("")
    open(os.path.join(fdir, "__init__.py"), "w", encoding="utf-8").write("")
    corp_a = (chr(10) + chr(10)).join(_extrage(zona, n) for n in
              ("tip", "amprenta_fisier", "scaneaza", "formateaza"))
    io.open(os.path.join(fdir, "amprente.py"), "w", encoding="utf-8").write(
        ANTET_AMPRENTE + corp_a + MAIN_AMPRENTE)
    io.open(os.path.join(fdir, "test_amprente.py"), "w", encoding="utf-8").write(TEST_AMPRENTE)
    _scrie_probe(os.path.join(fdir, "probe"))

    # --- Lucrarea B: reparare/ (tip_r->tip, amprenta_r->amprenta_fisier) ---
    rdir = os.path.join(LUCRARE, "reparare")
    os.makedirs(rdir, exist_ok=True)
    corp_r = (chr(10) + chr(10)).join(_extrage(zona, n) for n in
              ("tip_r", "amprenta_r", "scaneaza"))
    corp_r = corp_r.replace("amprenta_r", "amprenta_fisier").replace("tip_r", "tip")
    io.open(os.path.join(rdir, "amprente.py"), "w", encoding="utf-8").write(
        ANTET_REPARARE + corp_r + chr(10))
    io.open(os.path.join(rdir, "test_amprente.py"), "w", encoding="utf-8").write(TEST_REPARARE)
    _scrie_probe(os.path.join(rdir, "probe"))

    open(os.path.join(LUCRARE, ".gitignore"), "w", encoding="utf-8").write(
        "__pycache__/" + chr(10) + "*.pyc" + chr(10) + ".pytest_cache/" + chr(10) +
        "venv/" + chr(10) + ".venv/" + chr(10))

    titlu("PREDAREA E PREGATITA")
    print()
    print("   Am scris, in folderul lucrarii:")
    print()
    print("      Laborator_10/arsenal/forensics/amprente.py       unealta (Lucrarea A)")
    print("      Laborator_10/arsenal/forensics/test_amprente.py  cele 3 teste")
    print("      Laborator_10/arsenal/forensics/probe/            probele")
    print("      Laborator_10/reparare/amprente.py                unealta reparata (B)")
    print("      Laborator_10/reparare/test_amprente.py           testele reparare")
    print("      Laborator_10/reparare/probe/                     probele reparare")
    print()
    if nerez_a:
        linie("!")
        print("  ATENTIE. Mai ai de rezolvat/reparat sarcinile: " +
              ", ".join(str(x) for x in nerez_a))
        print("  Pana le termini, pytest va avea teste picate. Asa trebuie.")
        linie("!")
        print()
    print("   Verifica-l asa (din folderul Laborator_10):")
    print()
    print("      python -m arsenal.forensics.amprente arsenal/forensics/probe")
    print("      python -m pytest -q arsenal/forensics/test_amprente.py")
    print("      cd reparare && python -m pytest -q")
    print()
    print("   Apoi urca totul in depozitul tau:")
    print()
    print("      git add Laborator_10")
    print('      git commit -m "Laboratorul 10: forensics cu with, teste si reparare"')
    print("      git push")


# ---------------------------------------------------------------------------
#  Meniul
# ---------------------------------------------------------------------------
def deschide_sarcina(stare, numar):
    s, reusit, mesaj = stare[numar - 1]
    arata_sarcina(s, reusit, mesaj)
    print()
    print("   Apasa Enter dupa ce salvezi fisierul, ca sa reverific.")
    asteapta()


def main():
    if pregateste_probele():
        print()
        print("   Am creat folderul  start/probe/  cu cele patru probe.")

    while True:
        stare, eroare = stare_completa()
        if stare is None:
            titlu("CODUL TAU NU POATE FI CITIT", "!")
            print()
            for r in eroare.split(chr(10)):
                print("   " + r)
            print()
            print("   Repara si apasa Enter.")
            asteapta()
            continue

        arata_progres(stare)
        print()
        print("   Scrie numarul unei sarcini (1-%d) ca sa o vezi." % len(SARCINI))
        print()
        print("   Enter  reverifica tot")
        print("   p      pregateste predarea")
        print("   c      cum se lucreaza")
        print("   i      iesi")
        print()
        print("   Alege: ", end="")
        try:
            op = input().strip().lower()
        except EOFError:
            iesire_fara_terminal()
        except KeyboardInterrupt:
            break

        if op.isdigit():
            numar = int(op)
            if 1 <= numar <= len(SARCINI):
                deschide_sarcina(stare, numar)
            else:
                print()
                print("   Sarcinile sunt numerotate de la 1 la %d." % len(SARCINI))
                print("   Apasa Enter.")
                asteapta()
        elif op == "p":
            pregateste_predarea(stare)
            print()
            print("   Apasa Enter.")
            asteapta()
        elif op == "c":
            instructiuni()
            print("   Apasa Enter.")
            asteapta()
        elif op == "i":
            break


if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        pass
    except KeyboardInterrupt:
        print()
        print("   Intrerupt. Codul tau ramane salvat in fisier.")
    except Exception as _e:
        print()
        print("   A aparut o eroare neasteptata in program:")
        print("   " + type(_e).__name__ + ": " + str(_e))
        _tine_fereastra_deschisa()
