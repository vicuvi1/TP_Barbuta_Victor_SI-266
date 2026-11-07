# -*- coding: utf-8 -*-
"""
===============================================================================

   LUCRAREA DE LABORATOR NR. 8  -  FUNCTII SI EXCEPTII
   Apararea: detectia unui atac brute force din auth.log

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

          python L8_TP_Nume_Prenume_SI-26x.py

   3. Iti apare un meniu. Incepe cu optiunea  c , "Cum se lucreaza".

   -----------------------------------------------------------------------

   CE AI DE FACUT

   Treci in scaunul apararii. Dintr-un jurnal auth.log de pe o masina
   atacata scrii o unealta care scoate esecurile de autentificare, le
   numara pe IP si decide ce adrese sunt un atac brute force.

   Partea A - scoate si numara esecurile   4 sarcini
   Partea B - detectorul de brute force    4 sarcini

   Fiecare sarcina valoreaza un punct. Nota = punctajul obtinut.

   Scrii codul in functiile pregatite mai jos, SALVEZI fisierul si apesi
   Enter in fereastra programului. Iti spune imediat ce e corect si ce nu.

   -----------------------------------------------------------------------

   JURNALUL

   La prima pornire, programul creeaza singur folderul  start/  cu fisierul
   auth.log. Nu ai nimic de descarcat.

   Jurnalul e de la o masina izolata, de laborator. Analiza de jurnale se
   face pe sisteme pe care ai dreptul sa le administrezi.

===============================================================================
"""
import argparse
import io
import json
import os
import re
import sys
from collections import Counter

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

VERSIUNE = "L8-v1"
DOSAR = os.path.dirname(os.path.abspath(sys.argv[0])) or os.getcwd()
START = os.path.join(DOSAR, "start")

# Un rand de esec arata asa:
#   Failed password for root from 203.0.113.9 port 51230 ssh2
#   Failed password for invalid user admin from 203.0.113.9 port 51240 ssh2
TIPAR = re.compile(r"Failed password for (?:invalid user )?(\S+) from (\S+) port")


# ===========================================================================
#
#    A I C I   S C R I I   T U
#
#    Fiecare functie are un  # TODO  si se termina cu  raise NotImplementedError
#    Stergi randul acela si scrii codul tau in locul lui.
#
# ===========================================================================

# ---------------------------------------------------------------------------
#  PARTEA A - scoate si numara esecurile
# ---------------------------------------------------------------------------

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

def suspecti(counts, prag=10):
    """Sarcina 5. Adresele cu cel putin prag esecuri, cele mai multe intai.

    counts e un Counter (sau dict) ip -> numar. Intoarce o lista de perechi
    (ip, numar) cu numar >= prag, sortata descrescator dupa numar.

    Parametrul prag are valoarea implicita 10. Daca prag e sub 1, opreste
    functia cu:  raise ValueError("prag invalid: <prag> (cel putin 1)")

    suspecti(Counter({"203.0.113.9": 13, "198.51.100.7": 2}))
        ->  [('203.0.113.9', 13)]
    suspecti(acelasi, prag=2)
        ->  [('203.0.113.9', 13), ('198.51.100.7', 2)]
    """
    if prag < 1:
        raise ValueError("prag invalid: %s (cel putin 1)" % prag)
    rezultat = [(ip, n) for ip, n in counts.items() if n >= prag]
    rezultat.sort(key=lambda p: p[1], reverse=True)
    return rezultat


def raport_json(cale, prag=10):
    """Sarcina 6. Raportul complet, ca dictionar gata de pus in JSON.

    Leaga parse-ul cu detectorul si intoarce un dictionar cu trei chei:
        {"esecuri": numarul total de esecuri,
         "pe_ip": dictionar simplu ip -> numar (foloseste dict(...)),
         "suspecti": lista de (ip, numar) de la suspecti(counts, prag)}

    Nu tipari; doar intoarce. Cu acest dictionar, main() scoate JSON-ul.
    """
    esecuri = citeste_esecuri(cale)
    counts = pe_ip(esecuri)
    return {"esecuri": len(esecuri),
            "pe_ip": dict(counts),
            "suspecti": suspecti(counts, prag)}


def e_brute_force(counts, ip, prag=10):
    """Sarcina 7. Spune daca o adresa e un atac brute force.

    Intoarce True daca adresa ip are cel putin prag esecuri in counts,
    altfel False. Foloseste counts.get(ip, 0), ca sa nu crape pentru o
    adresa care nu apare deloc.

    e_brute_force(Counter({"203.0.113.9": 13}), "203.0.113.9")  ->  True
    e_brute_force(acelasi, "198.51.100.7")                      ->  False
    e_brute_force(acelasi, "lipsa")                             ->  False
    """
    return counts.get(ip, 0) >= prag


def utilizatori_tintiti(esecuri, ip):
    """Sarcina 8. Ce utilizatori a incercat o anumita adresa.

    Primeste lista de esecuri si o adresa. Intoarce MULTIMEA numelor de
    utilizator incercate DE la acea adresa (fara dubluri).

    Pentru atacator iese o multime cu mai multe nume (root, admin, ...);
    multimea arunca singura repetarile.
    """
    return {e["user"] for e in esecuri if e["ip"] == ip}


#  @@ AICI SE TERMINA ZONA TA @@
# ===========================================================================

# Marcajul e lipit din doua bucati dinadins: altfel randul acesta ar contine
# el insusi textul cautat, iar taierea ar cadea in mijlocul lui.
MARCAJ_ZONA = "@@ AICI SE TERMINA " + "ZONA TA @@"

# Jurnalul de pe masina atacata. Un brute force dens de la 203.0.113.9 (13
# esecuri), doua esecuri de la 198.51.100.7, plus randuri care NU sunt
# esecuri si trebuie sarite.
AUTH_LOG = [
    "Nov  2 09:14:01 srv sshd[2011]: Server listening on 0.0.0.0 port 22.",
    "Nov  2 09:15:22 srv sshd[2044]: Accepted password for hacker from 10.0.0.5 port 49001 ssh2",
    "Nov  2 09:16:03 srv sshd[2051]: Failed password for root from 203.0.113.9 port 51230 ssh2",
    "Nov  2 09:16:04 srv sshd[2051]: Failed password for root from 203.0.113.9 port 51231 ssh2",
    "Nov  2 09:16:05 srv sshd[2051]: Failed password for root from 203.0.113.9 port 51232 ssh2",
    "Nov  2 09:16:06 srv sshd[2052]: Failed password for invalid user admin from 203.0.113.9 port 51240 ssh2",
    "Nov  2 09:16:07 srv sshd[2052]: Failed password for invalid user test from 203.0.113.9 port 51241 ssh2",
    "Nov  2 09:16:08 srv sshd[2052]: Failed password for invalid user oracle from 203.0.113.9 port 51242 ssh2",
    "Nov  2 09:16:09 srv sshd[2053]: Failed password for root from 203.0.113.9 port 51250 ssh2",
    "Nov  2 09:16:10 srv sshd[2053]: Failed password for root from 203.0.113.9 port 51251 ssh2",
    "Nov  2 09:16:11 srv CRON[2099]: pam_unix(cron:session): session opened for user root",
    "Nov  2 09:16:12 srv sshd[2054]: Failed password for invalid user pi from 203.0.113.9 port 51260 ssh2",
    "Nov  2 09:16:13 srv sshd[2054]: Failed password for invalid user git from 203.0.113.9 port 51261 ssh2",
    "Nov  2 09:16:14 srv sshd[2055]: Failed password for admin from 203.0.113.9 port 51270 ssh2",
    "Nov  2 09:16:15 srv sshd[2055]: Failed password for admin from 203.0.113.9 port 51271 ssh2",
    "Nov  2 09:16:16 srv sshd[2056]: Failed password for root from 203.0.113.9 port 51280 ssh2",
    "<linie stricata fara structura>",
    "Nov  2 09:18:40 srv sshd[2120]: Failed password for root from 198.51.100.7 port 40022 ssh2",
    "Nov  2 09:20:55 srv sshd[2140]: Failed password for invalid user ubuntu from 198.51.100.7 port 40100 ssh2",
    "Nov  2 09:21:10 srv sshd[2141]: Accepted password for hacker from 10.0.0.5 port 49050 ssh2",
    "Nov  2 09:22:00 srv sshd[2150]: Disconnected from 10.0.0.5 port 49050",
]


def pregateste_jurnalul():
    """Scrie folderul start/ cu auth.log la prima pornire."""
    nou = False
    if not os.path.isdir(START):
        os.makedirs(START)
        nou = True
    cale = os.path.join(START, "auth.log")
    if not os.path.exists(cale):
        io.open(cale, "w", encoding="utf-8").write("\n".join(AUTH_LOG) + "\n")
        nou = True
    return nou


LOG = os.path.join(START, "auth.log")


# ---------------------------------------------------------------------------
#  Rezultatele asteptate, scoase din jurnal
# ---------------------------------------------------------------------------
_ESECURI = [{"user": u, "ip": ip} for (u, ip) in [
    ("root", "203.0.113.9"), ("root", "203.0.113.9"), ("root", "203.0.113.9"),
    ("admin", "203.0.113.9"), ("test", "203.0.113.9"), ("oracle", "203.0.113.9"),
    ("root", "203.0.113.9"), ("root", "203.0.113.9"), ("pi", "203.0.113.9"),
    ("git", "203.0.113.9"), ("admin", "203.0.113.9"), ("admin", "203.0.113.9"),
    ("root", "203.0.113.9"),
    ("root", "198.51.100.7"), ("ubuntu", "198.51.100.7"),
]]
_PE_IP = Counter({"203.0.113.9": 13, "198.51.100.7": 2})
_REZUMAT = {"esecuri": 15, "pe_ip": _PE_IP}
_RAPORT = {"esecuri": 15, "pe_ip": {"203.0.113.9": 13, "198.51.100.7": 2},
           "suspecti": [("203.0.113.9", 13)]}
_C = Counter({"203.0.113.9": 13, "198.51.100.7": 2})


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
                       + chr(10) + "Codul dintr-o functie se scrie cu 4 "
                       "spatii mai la dreapta decat def.")
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


def _scurt(v, maxim=58):
    t = repr(v)
    return t if len(t) <= maxim else t[:maxim - 3] + "..."


def _egale(a, b):
    """Compara rezultatul cu cel asteptat, fara sa accepte alt tip gresit."""
    if isinstance(b, bool):
        return isinstance(a, bool) and a == b
    if isinstance(b, set):
        return isinstance(a, set) and a == b
    if isinstance(b, dict):      # Counter e tot dict; comparam pe valori
        return isinstance(a, dict) and a == b
    if isinstance(b, list):
        return isinstance(a, list) and a == b
    if isinstance(b, tuple):
        return isinstance(a, tuple) and a == b
    return a == b


def verifica_sarcina(s):
    """Intoarce (reusit, mesaj)."""
    fn = globals().get(s["functie"])
    if fn is None:
        return False, "Functia " + s["functie"] + " nu exista in fisier."
    # sarcina de validare: cod care TREBUIE sa ridice o exceptie
    for args, exc in s.get("ridica", []):
        try:
            fn(*args)
            return False, ("Pentru " + s["functie"] + "(" +
                           ", ".join(_scurt(a, 24) for a in args) + ")" +
                           chr(10) + "         trebuia sa opresti cu " +
                           exc.__name__ + ", dar nu ai facut-o.")
        except NotImplementedError:
            return False, "Sarcina nu este inca rezolvata."
        except exc:
            pass
        except Exception as e:
            return False, ("Ai ridicat " + type(e).__name__ + ", dar se astepta "
                           + exc.__name__ + ".")
    for args, asteptat in s.get("teste", []):
        try:
            obtinut = fn(*args)
        except NotImplementedError:
            return False, "Sarcina nu este inca rezolvata."
        except Exception as e:
            return False, ("Codul tau a dat eroare la " + s["functie"] + "(" +
                           ", ".join(_scurt(a, 24) for a in args) + ")" +
                           chr(10) + "         " + type(e).__name__ + ": " + str(e))
        if not _egale(obtinut, asteptat):
            return False, ("Pentru " + s["functie"] + "(" +
                           ", ".join(_scurt(a, 24) for a in args) + ")" +
                           chr(10) + "         asteptam: " + _scurt(asteptat) +
                           chr(10) + "         am primit: " + _scurt(obtinut))
    return True, "Corect."


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
    return sum(1 for _, reusit, _ in stare if reusit)


# ---------------------------------------------------------------------------
#  Sarcinile
# ---------------------------------------------------------------------------
_EX_OK = "Nov 2 Failed password for root from 203.0.113.9 port 51230 ssh2"
_EX_INV = "x Failed password for invalid user admin from 203.0.113.9 port 9 ssh2"

SARCINI = [
 {"nr": 1, "parte": "A", "functie": "esec", "titlu": "Fisa dintr-un rand",
  "indiciu": "TIPAR.search intoarce None daca randul nu se potriveste; atunci intorci None.",
  "teste": [((_EX_OK,), ("root", "203.0.113.9")),
            ((_EX_INV,), ("admin", "203.0.113.9")),
            (("<linie stricata>",), None),
            (("",), None)]},
 {"nr": 2, "parte": "A", "functie": "citeste_esecuri",
  "titlu": "Lista de esecuri, robusta",
  "indiciu": "Sari peste randul unde esec intoarce None. Prinde FileNotFoundError.",
  "teste": [((LOG,), _ESECURI),
            ((os.path.join(START, "nu_exista.log"),), [])]},
 {"nr": 3, "parte": "A", "functie": "pe_ip",
  "titlu": "Numararea pe IP",
  "indiciu": "Counter(e['ip'] for e in esecuri).",
  "teste": [((_ESECURI,), _PE_IP),
            (([],), Counter())]},
 {"nr": 4, "parte": "A", "functie": "rezumat",
  "titlu": "Rezumatul, ca dictionar",
  "indiciu": "Intoarce {'esecuri': len(...), 'pe_ip': pe_ip(...)}. Nu tipari.",
  "teste": [((LOG,), _REZUMAT)]},

 {"nr": 5, "parte": "B", "functie": "suspecti",
  "titlu": "Pragul si validarea",
  "indiciu": "Perechile (ip, n) cu n >= prag, sortate descrescator dupa n.",
  "teste": [((_C,), [("203.0.113.9", 13)]),
            ((_C, 2), [("203.0.113.9", 13), ("198.51.100.7", 2)]),
            ((_C, 100), [])],
  "ridica": [(({}, 0), ValueError), (({}, -5), ValueError)]},
 {"nr": 6, "parte": "B", "functie": "raport_json",
  "titlu": "Raportul complet",
  "indiciu": "Trei chei: esecuri, pe_ip (dict simplu), suspecti. Foloseste dict(...).",
  "teste": [((LOG,), _RAPORT)]},
 {"nr": 7, "parte": "B", "functie": "e_brute_force",
  "titlu": "E atac brute force?",
  "indiciu": "counts.get(ip, 0) >= prag. Nu crapa pentru o adresa care lipseste.",
  "teste": [((_C, "203.0.113.9"), True),
            ((_C, "198.51.100.7"), False),
            ((_C, "lipsa"), False),
            ((_C, "198.51.100.7", 2), True)]},
 {"nr": 8, "parte": "B", "functie": "utilizatori_tintiti",
  "titlu": "Ce utilizatori a incercat",
  "indiciu": "Multimea e['user'] pentru esecurile cu e['ip'] == ip.",
  "teste": [((_ESECURI, "203.0.113.9"),
             {"admin", "git", "oracle", "pi", "root", "test"}),
            ((_ESECURI, "198.51.100.7"), {"root", "ubuntu"})]},
]


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


def harta(stare):
    """Ancheta pe masina atacata, care se completeaza pe masura ce rezolvi.

    Fiecare rand e un pas al apararii. Cat timp sarcina care il produce nu e
    rezolvata, randul sta in ceata. Cand o rezolvi, se aprinde cu datele
    adevarate: chiar rezultatul codului tau."""
    gata = set(s["nr"] for s, reusit, _ in stare if reusit)

    def are(*nrs):
        return all(n in gata for n in nrs)

    def rand(eticheta, deblocat, text, cheie):
        tinta = text if deblocat else "in ceata ... (rezolva %s)" % cheie
        marcaj = " +" if deblocat else "  "
        print("  %s %-12s %s" % (marcaj, eticheta, tinta[:52]))

    atac = _PE_IP.most_common(1)[0]          # ('203.0.113.9', 13)
    useri = sorted({e["user"] for e in _ESECURI if e["ip"] == atac[0]})

    titlu("MASINA ATACATA  -  ancheta din auth.log", "-")
    print()
    rand("un rand:", are(1), "stiu sa scot (user, ip) dintr-un esec", "sarcina 1")
    rand("esecuri:", are(2), "%d esecuri scoase din jurnal" % len(_ESECURI),
         "sarcina 2")
    rand("pe adresa:", are(3), "%s" % ", ".join("%s=%d" % (ip, n)
         for ip, n in _PE_IP.most_common()), "sarcina 3")
    rand("rezumat:", are(4), "%d esecuri de la %d adrese" %
         (_REZUMAT["esecuri"], len(_PE_IP)), "sarcina 4")
    print()
    rand("SUSPECT:", are(5), "prag 10 -> %s (%d incercari)" % atac, "sarcina 5")
    rand("raport:", are(6), "JSON gata de trimis", "sarcina 6")
    rand("VERDICT:", are(7), "%s  ->  BRUTE FORCE" % atac[0], "sarcina 7")
    rand("ce a vrut:", are(8), "a incercat conturile: %s" % ", ".join(useri),
         "sarcina 8")
    print()
    if are(*range(1, 9)):
        print("  >>> Atacul e documentat. Adresa %s e dovedita. <<<" % atac[0])
    else:
        print("  Rezolva sarcinile ca sa risipesti ceata de pe masina.")


def arata_progres(stare):
    titlu("LABORATORUL 8  -  FUNCTII SI EXCEPTII", "=")
    p = punctaj(stare)
    print()
    print("  " + bara(p, len(SARCINI)) + "   %d din %d sarcini" % (p, len(SARCINI)))
    harta(stare)
    print()
    parte = None
    for s, reusit, mesaj in stare:
        if s["parte"] != parte:
            parte = s["parte"]
            print("  PARTEA %s" % parte)
        semn = "[x]" if reusit else "[ ]"
        print("   %s %2d. %-30s %s" % (semn, s["nr"], s["titlu"],
                                       "" if reusit else mesaj.split(chr(10))[0][:30]))
    print()
    print("  Nota ta acum: %d" % max(1, min(10, p)))


def arata_sarcina(s, reusit, mesaj):
    titlu("SARCINA %d  (partea %s)  -  %s" % (s["nr"], s["parte"], s["titlu"]))
    print()
    fn = globals().get(s["functie"])
    doc = (fn.__doc__ or "") if fn else ""
    for r in doc.strip().split(chr(10)):
        print("   " + r.strip())
    print()
    if reusit:
        print("   REZOLVATA.")
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

   2. Deschide fisierul  L8_TP_Nume_Prenume_SI-26x.py  intr-un editor.

   3. Cauta functia sarcinii la care lucrezi. Fiecare are un  # TODO
      si se termina cu  raise NotImplementedError.
      Stergi randul acela si scrii codul tau.

   4. SALVEZI fisierul.

   5. Vii inapoi in aceasta fereastra si apesi Enter. Programul reciteste
      fisierul si iti spune imediat daca merge.

   Jurnalul e in folderul  start/auth.log , creat la prima pornire. Il poti
   deschide si citi oricand: e un simplu fisier text.
""")


# ---------------------------------------------------------------------------
#  Predarea: scrie fisierele cerute in fisa
# ---------------------------------------------------------------------------
def _extrage(zona, nume):
    """Scoate sursa functiei cu numele dat din zona studentului."""
    randuri = zona.split(chr(10))
    inceput = None
    for i, r in enumerate(randuri):
        if r.startswith("def " + nume + "("):
            inceput = i
            break
    if inceput is None:
        return "# functia " + nume + " lipseste"
    out = [randuri[inceput]]
    for r in randuri[inceput + 1:]:
        if r.startswith("def ") or (r and not r[0].isspace() and not r.startswith("#")):
            break
        out.append(r)
    while out and not out[-1].strip():
        out.pop()
    return chr(10).join(out)


PARSE_A = ["esec", "citeste_esecuri", "pe_ip", "rezumat"]
DET_B = ["suspecti", "raport_json", "e_brute_force", "utilizatori_tintiti"]

ANTET_PARSE = (
    "# -*- coding: utf-8 -*-" + chr(10) +
    '"""Laboratorul 8 - partea A. Scoate si numara esecurile din auth.log.' +
    chr(10) + 'Generat din programul de laborator, cu codul scris de student."""' +
    chr(10) + "import re" + chr(10) + "from collections import Counter" +
    chr(10) + chr(10) +
    'TIPAR = re.compile(r"Failed password for (?:invalid user )?'
    r'(\S+) from (\S+) port")' + chr(10) + chr(10) + chr(10))

MAIN_PARSE = (chr(10) + chr(10) +
    "def main():" + chr(10) +
    "    import sys" + chr(10) +
    "    cale = sys.argv[1] if len(sys.argv) > 1 else 'start/auth.log'" + chr(10) +
    "    esecuri = citeste_esecuri(cale)" + chr(10) +
    "    counts = pe_ip(esecuri)" + chr(10) +
    "    print('Esecuri de autentificare:', len(esecuri))" + chr(10) +
    "    for ip, n in counts.most_common():" + chr(10) +
    "        print('  %s: %d' % (ip, n))" + chr(10) + chr(10) + chr(10) +
    "if __name__ == '__main__':" + chr(10) + "    main()" + chr(10))

ANTET_DET = (
    "# -*- coding: utf-8 -*-" + chr(10) +
    '"""Laboratorul 8 - partea B. Detectorul de brute force."""' + chr(10) +
    "import argparse, json" + chr(10) +
    "from collections import Counter" + chr(10) +
    "from arsenal.aparare.parse_auth import citeste_esecuri, pe_ip" +
    chr(10) + chr(10) + chr(10))

MAIN_DET = (chr(10) + chr(10) +
    "def main():" + chr(10) +
    "    p = argparse.ArgumentParser()" + chr(10) +
    "    p.add_argument('log')" + chr(10) +
    "    p.add_argument('--prag', type=int, default=10)" + chr(10) +
    "    p.add_argument('--json', action='store_true')" + chr(10) +
    "    a = p.parse_args()" + chr(10) +
    "    esecuri = citeste_esecuri(a.log)" + chr(10) +
    "    counts = pe_ip(esecuri)" + chr(10) +
    "    sus = suspecti(counts, a.prag)" + chr(10) +
    "    if a.json:" + chr(10) +
    "        print(json.dumps({'esecuri': len(esecuri)," + chr(10) +
    "                          'pe_ip': dict(counts)," + chr(10) +
    "                          'suspecti': sus}, indent=2))" + chr(10) +
    "        return" + chr(10) +
    "    print('Esecuri de autentificare:', len(esecuri))" + chr(10) +
    "    for ip, n in counts.most_common():" + chr(10) +
    "        print('  %s: %d' % (ip, n))" + chr(10) +
    "    print('Suspecti (prag %d):' % a.prag)" + chr(10) +
    "    for ip, n in sus:" + chr(10) +
    "        print('  %s  (%d incercari)  BRUTE FORCE' % (ip, n))" + chr(10) +
    chr(10) + chr(10) + "if __name__ == '__main__':" + chr(10) + "    main()" + chr(10))

CODA_TEST = (
    "# -*- coding: utf-8 -*-" + chr(10) +
    '"""Doua teste care prind regresia."""' + chr(10) +
    "from collections import Counter" + chr(10) +
    "from arsenal.aparare.detector import suspecti" + chr(10) + chr(10) + chr(10) +
    "def test_pragul_taie():" + chr(10) +
    "    c = Counter({'a': 13, 'b': 2})" + chr(10) +
    "    assert suspecti(c, 10) == [('a', 13)]" + chr(10) + chr(10) + chr(10) +
    "def test_prag_invalid():" + chr(10) +
    "    import pytest" + chr(10) +
    "    with pytest.raises(ValueError):" + chr(10) +
    "        suspecti({}, 0)" + chr(10))


def pregateste_predarea(stare):
    nerezolvate = [s["nr"] for s, reusit, _ in stare if not reusit]
    sursa = io.open(os.path.abspath(sys.argv[0]), encoding="utf-8").read()
    zona = sursa[:sursa.find(MARCAJ_ZONA)]

    LUCRARE = os.path.join(DOSAR, "Laborator_8")
    dest = os.path.join(LUCRARE, "arsenal", "aparare")
    os.makedirs(dest, exist_ok=True)
    io.open(os.path.join(LUCRARE, "arsenal", "__init__.py"), "w",
            encoding="utf-8").write("")
    io.open(os.path.join(dest, "__init__.py"), "w", encoding="utf-8").write("")
    io.open(os.path.join(LUCRARE, ".gitignore"), "w", encoding="utf-8").write(
        "__pycache__/" + chr(10) + "*.pyc" + chr(10) + "venv/" + chr(10) +
        ".venv/" + chr(10))

    parse_src = ANTET_PARSE + (chr(10) + chr(10)).join(
        _extrage(zona, n) for n in PARSE_A) + MAIN_PARSE
    det_src = ANTET_DET + (chr(10) + chr(10)).join(
        _extrage(zona, n) for n in DET_B) + MAIN_DET
    io.open(os.path.join(dest, "parse_auth.py"), "w", encoding="utf-8").write(parse_src)
    io.open(os.path.join(dest, "detector.py"), "w", encoding="utf-8").write(det_src)
    io.open(os.path.join(dest, "test_detector.py"), "w", encoding="utf-8").write(CODA_TEST)

    sdest = os.path.join(dest, "start")
    os.makedirs(sdest, exist_ok=True)
    io.open(os.path.join(sdest, "auth.log"), "w", encoding="utf-8").write(
        chr(10).join(AUTH_LOG) + chr(10))

    titlu("PREDAREA E PREGATITA")
    print()
    print("   Am scris, in folderul lucrarii:")
    print()
    print("      Laborator_8/arsenal/aparare/parse_auth.py      partea A")
    print("      Laborator_8/arsenal/aparare/detector.py        partea B")
    print("      Laborator_8/arsenal/aparare/test_detector.py   testele")
    print("      Laborator_8/arsenal/aparare/start/auth.log     jurnalul")
    print()
    if nerezolvate:
        linie("!")
        print("  ATENTIE. Mai ai de rezolvat sarcinile: " +
              ", ".join(str(x) for x in nerezolvate))
        print("  Pana le termini, comenzile de mai jos se opresc cu eroare la")
        print("  prima functie nescrisa. Asa trebuie, nu e o defectiune.")
        linie("!")
        print()
    print("   Verifica-l asa:")
    print()
    print("      cd Laborator_8")
    print("      python -m arsenal.aparare.detector arsenal/aparare/start/auth.log")
    print()
    print("   Apoi urca totul in depozitul tau:")
    print()
    print("      git add Laborator_8")
    print('      git commit -m "Laboratorul 8: functii si exceptii"')
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
    if pregateste_jurnalul():
        print()
        print("   Am creat folderul  start/  cu jurnalul auth.log.")

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
        # orice altceva, inclusiv Enter, reia bucla si reverifica


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
