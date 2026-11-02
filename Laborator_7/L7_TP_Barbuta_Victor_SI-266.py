# -*- coding: utf-8 -*-
"""
===============================================================================

   LUCRAREA DE LABORATOR NR. 7  -  COLECTII
   Liste, tupluri, multimi, dictionare   ·   Privesc pe Linux

   Universitatea Tehnica a Moldovei
   Facultatea Calculatoare, Informatica si Microelectronica
   Disciplina: Tehnici de programare        Anul I, grupele SI-265 / SI-266

===============================================================================

   CUM PORNESTI

   1. Deschide linia de comanda in folderul unde se afla acest fisier.
      In Windows: intra in folder, scrie  cmd  in bara de adresa si Enter.

   2. Porneste programul:

          python L7_TP_Nume_Prenume_SI-26x.py

   3. Iti apare un meniu. Incepe cu optiunea 4, "Cum se lucreaza".

   -----------------------------------------------------------------------

   CE AI DE FACUT

   Construiesti o unealta de enumerare spre root: citeste ce a adunat un
   atacator de pe o masina Linux si aseaza constatarile in colectii.

   Partea A - aduna si grupeaza        7 sarcini
   Partea B - ce e nou fata de curat   4 sarcini

   Fiecare sarcina valoreaza un punct. Nota = punctajul obtinut.

   Scrii codul in functiile pregatite mai jos, SALVEZI fisierul si apesi
   Enter in fereastra programului. Iti spune imediat ce e corect si ce nu.

   -----------------------------------------------------------------------

   CAPTURILE DE PE MASINA

   La prima pornire, programul creeaza singur folderul  start/  cu patru
   fisiere. Nu ai nimic de descarcat.

      suid.txt       fisiere cu bit SUID      (find / -perm -4000 -type f)
      sudo.txt       ce poate rula contul     (sudo -l)
      crontab.txt    sarcini programate       (cat /etc/crontab)
      baza_suid.txt  aceleasi SUID pe o instalare curata, de referinta

   Pe o masina reala, comenzile acelea scot sute de randuri. Au fost
   capturate o data, ca sa lucrezi pe date stabile.

===============================================================================
"""
import io
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

VERSIUNE = "L7-v1"
DOSAR = os.path.dirname(os.path.abspath(sys.argv[0])) or os.getcwd()
START = os.path.join(DOSAR, "start")

# Binare care, daca au bit SUID, deschid drum spre root.
# Lista scurtata din proiectul GTFOBins.
GTFO = {"find", "vim.basic", "vim", "nmap", "cp", "bash",
        "less", "awk", "python3", "perl"}


# ===========================================================================
#
#    A I C I   S C R I I   T U
#
#    Fiecare functie are un  # TODO  si se termina cu  raise NotImplementedError
#    Stergi randul acela si scrii codul tau in locul lui.
#
# ===========================================================================

# ---------------------------------------------------------------------------
#  PARTEA A - aduna si grupeaza
# ---------------------------------------------------------------------------

def citeste_linii(cale):
    """Sarcina 1. Citeste un fisier si intoarce LISTA randurilor folositoare.

    Fiecare rand se curata de spatiile de la capete. Se arunca randurile
    goale si cele care incep cu diez, fiindca sunt comentarii.

    citeste_linii("start/suid.txt")  ->  lista cu 14 randuri
    """
    linii = []
    with open(cale, encoding="utf-8") as fis:
        for rand in fis:
            rand = rand.strip()
            if rand and not rand.startswith("#"):
                linii.append(rand)
    return linii


def nume(cale):
    """Sarcina 2. Intoarce numele fisierului dintr-o cale.

    Numele decide daca binarul e periculos, nu toata calea.

    nume("/usr/bin/find")  ->  "find"
    """
    return cale.rsplit("/", 1)[-1]


def suid_constatari(cale):
    """Sarcina 3. Din fisierul SUID face o LISTA DE DICTIONARE.

    Fiecare cale UNICA, in ordine sortata, devine o fisa cu trei campuri:
        {"cale": ..., "nume": ..., "risc": "mare" sau "normal"}
    Riscul e "mare" daca numele se afla in multimea GTFO, altfel "normal".

    Atentie: in captura o cale apare de doua ori. Fisa ei apare o data.
    """
    constatari = []
    for c in sorted(set(citeste_linii(cale))):
        n = nume(c)
        risc = "mare" if n in GTFO else "normal"
        constatari.append({"cale": c, "nume": n, "risc": risc})
    return constatari


def sudo_constatari(cale):
    """Sarcina 4. Din fisierul sudo face o lista de dictionare.

    Un rand are forma  utilizator : drept
    Il despachetezi intr-un tuplu de doua valori, taind la PRIMUL separator:
        user, drept = rand.split(" : ", 1)

    Fiecare rand devine:
        {"user": ..., "drept": ..., "risc": "mare" sau "normal"}
    Riscul e "mare" daca in drept apare NOPASSWD, fiindca atunci comanda
    se ruleaza fara sa se ceara parola.
    """
    constatari = []
    for rand in citeste_linii(cale):
        user, drept = rand.split(" : ", 1)
        risc = "mare" if "NOPASSWD" in drept else "normal"
        constatari.append({"user": user, "drept": drept, "risc": risc})
    return constatari


def cron_constatari(cale):
    """Sarcina 5. Din crontab face o lista de dictionare.

    Un rand de crontab are cinci campuri de timp, apoi utilizatorul si
    comanda. Desparti randul in campuri cu split(), iar:
        campul 5 (al saselea) este utilizatorul
        tot ce urmeaza, lipit la loc cu spatii, este comanda

    Fiecare rand devine:  {"user": ..., "comanda": ...}
    """
    constatari = []
    for rand in citeste_linii(cale):
        campuri = rand.split()
        constatari.append({"user": campuri[5], "comanda": " ".join(campuri[6:])})
    return constatari


def enumereaza(dosar):
    """Sarcina 6. Aduna toate constatarile intr-un singur DICTIONAR.

    Primeste calea folderului cu capturi si intoarce un dictionar cu o
    cheie pe categorie, iar valoarea este lista de constatari:

        {"suid": [...], "sudo": [...], "cron": [...]}

    Pentru a lipi calea unui fisier de folder, foloseste os.path.join.
    """
    return {
        "suid": suid_constatari(os.path.join(dosar, "suid.txt")),
        "sudo": sudo_constatari(os.path.join(dosar, "sudo.txt")),
        "cron": cron_constatari(os.path.join(dosar, "crontab.txt")),
    }


def utilizatori_implicati(raport):
    """Sarcina 7. Intoarce MULTIMEA utilizatorilor care apar in raport.

    Sunt utilizatorii din constatarile sudo REUNITI cu cei din cron.
    Reuniunea a doua multimi se face cu operatorul  |  si arunca dublurile.

    Primeste dictionarul intors de enumereaza.
    """
    useri_sudo = {c["user"] for c in raport["sudo"]}
    useri_cron = {c["user"] for c in raport["cron"]}
    return useri_sudo | useri_cron


# ---------------------------------------------------------------------------
#  PARTEA B - ce e nou fata de un sistem curat
# ---------------------------------------------------------------------------

def cai(fisier):
    """Sarcina 8. Intoarce MULTIMEA cailor dintr-un fisier.

    Foloseste citeste_linii, pe care ai scris-o deja la sarcina 1.
    O multime arunca singura dublurile, de aceea aici iese 13, nu 14.
    """
    return set(citeste_linii(fisier))


def suid_noi(acum, baza):
    """Sarcina 9. Ce e in acum, dar nu si in baza.

    Amandoua sunt multimi de cai. Rezultatul este tot o multime: fisierele
    SUID aparute fata de sistemul curat.

    Se face cu UN SINGUR operator, nu cu doua bucle una in alta.
    """
    return acum - baza


def risc_pe_nume(multime_cai):
    """Sarcina 10. Fisa nume -> risc, ca DICTIONAR.

    Pentru fiecare cale din multimea primita, cheia este numele fisierului,
    iar valoarea este "mare" daca numele se afla in GTFO, altfel "normal".

    Se scrie pe un singur rand, cu dict comprehension.
    """
    return {nume(c): ("mare" if nume(c) in GTFO else "normal") for c in multime_cai}


def periculoase_noi(noi):
    """Sarcina 11. Lista cailor noi care sunt periculoase, sortata.

    Din multimea primita pastrezi doar caile al caror nume e in GTFO si le
    intorci ca lista, in ordine sortata.
    """
    return [c for c in sorted(noi) if nume(c) in GTFO]


# ===========================================================================
#
#   Sub randul urmator incepe programul care te verifica.
#   Nu e nevoie sa intelegi codul de mai jos si nu il modifica.
#
# ===========================================================================
#  @@ AICI SE TERMINA ZONA TA @@
# ===========================================================================

# Marcajul e lipit din doua bucati dinadins: altfel randul acesta ar contine
# el insusi textul cautat, iar taierea ar cadea in mijlocul lui.
MARCAJ_ZONA = "@@ AICI SE TERMINA " + "ZONA TA @@"

CAPTURI = {
    "suid.txt": [
        "/usr/bin/passwd", "/usr/bin/sudo", "/usr/bin/chsh", "/usr/bin/chfn",
        "/usr/bin/newgrp", "/usr/bin/gpasswd", "/bin/mount", "/bin/umount",
        "/bin/su", "/usr/bin/find", "/usr/bin/vim.basic", "/usr/bin/nmap",
        "/bin/cp", "/usr/bin/passwd",
    ],
    "baza_suid.txt": [
        "/usr/bin/passwd", "/usr/bin/sudo", "/usr/bin/chsh", "/usr/bin/chfn",
        "/usr/bin/newgrp", "/usr/bin/gpasswd", "/bin/mount", "/bin/umount",
        "/bin/su",
    ],
    "sudo.txt": [
        "ana : (ALL) NOPASSWD: /usr/bin/vim.basic",
        "ana : (ALL) /usr/bin/apt",
        "www-data : (root) NOPASSWD: /usr/bin/find",
    ],
    "crontab.txt": [
        "# /etc/crontab",
        "17 *\t* * *\troot\tcd / && run-parts --report /etc/cron.hourly",
        "*/5 *\t* * *\troot\t/opt/backup/run.sh",
        "30 2\t* * *\twww-data\t/home/www-data/clean.sh",
    ],
}


def pregateste_capturile():
    """Scrie folderul start/ la prima pornire, ca sa nu descarci nimic."""
    nou = False
    if not os.path.isdir(START):
        os.makedirs(START)
        nou = True
    for fisier, randuri in CAPTURI.items():
        cale = os.path.join(START, fisier)
        if not os.path.exists(cale):
            io.open(cale, "w", encoding="utf-8").write("\n".join(randuri) + "\n")
            nou = True
    return nou


def f(fisier):
    """Calea unei capturi, scurt."""
    return os.path.join(START, fisier)


# ---------------------------------------------------------------------------
#  Reincarcarea codului scris de student
# ---------------------------------------------------------------------------
def reincarca_codul():
    """Reciteste de pe disc zona in care scrii tu si actualizeaza functiile.

    Datorita ei poti lasa programul pornit, sa editezi fisierul in alta
    fereastra, sa salvezi si sa apesi Enter: se verifica noul cod.
    Intoarce (reusit, mesaj_de_eroare).
    """
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
    """Compara rezultatul cu cel asteptat, fara sa accepte alt tip."""
    if isinstance(b, set):
        return isinstance(a, set) and a == b
    if isinstance(b, dict):
        return isinstance(a, dict) and a == b
    if isinstance(b, list):
        return isinstance(a, list) and a == b
    return a == b


def verifica_sarcina(s):
    """Intoarce (reusit, mesaj)."""
    fn = globals().get(s["functie"])
    if fn is None:
        return False, "Functia " + s["functie"] + " nu exista in fisier."
    for argumente, asteptat in s["teste"]:
        try:
            obtinut = fn(*argumente)
        except NotImplementedError:
            return False, "Sarcina nu este inca rezolvata."
        except Exception as e:
            return False, ("Codul tau a dat eroare la " + s["functie"] + "(" +
                           ", ".join(_scurt(a, 28) for a in argumente) + ")" +
                           chr(10) + "         " + type(e).__name__ + ": " + str(e))
        if not _egale(obtinut, asteptat):
            return False, ("Pentru " + s["functie"] + "(" +
                           ", ".join(_scurt(a, 28) for a in argumente) + ")" +
                           chr(10) + "         asteptam: " + _scurt(asteptat) +
                           chr(10) + "         am primit: " + _scurt(obtinut))
    return True, "Corect."


def stare_completa(reincarca=True):
    """Intoarce lista (sarcina, reusit, mesaj) pentru toate sarcinile."""
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
#  Rezultatele asteptate, scoase din capturi
# ---------------------------------------------------------------------------
_SUID_LINII = list(CAPTURI["suid.txt"])
_CRON_LINII = [x for x in CAPTURI["crontab.txt"] if not x.startswith("#")]
_CAI_ACUM = set(CAPTURI["suid.txt"])
_CAI_BAZA = set(CAPTURI["baza_suid.txt"])
_NOI = _CAI_ACUM - _CAI_BAZA

_SUID = [{"cale": "/bin/cp", "nume": "cp", "risc": "mare"},
         {"cale": "/bin/mount", "nume": "mount", "risc": "normal"},
         {"cale": "/bin/su", "nume": "su", "risc": "normal"},
         {"cale": "/bin/umount", "nume": "umount", "risc": "normal"},
         {"cale": "/usr/bin/chfn", "nume": "chfn", "risc": "normal"},
         {"cale": "/usr/bin/chsh", "nume": "chsh", "risc": "normal"},
         {"cale": "/usr/bin/find", "nume": "find", "risc": "mare"},
         {"cale": "/usr/bin/gpasswd", "nume": "gpasswd", "risc": "normal"},
         {"cale": "/usr/bin/newgrp", "nume": "newgrp", "risc": "normal"},
         {"cale": "/usr/bin/nmap", "nume": "nmap", "risc": "mare"},
         {"cale": "/usr/bin/passwd", "nume": "passwd", "risc": "normal"},
         {"cale": "/usr/bin/sudo", "nume": "sudo", "risc": "normal"},
         {"cale": "/usr/bin/vim.basic", "nume": "vim.basic", "risc": "mare"}]

_SUDO = [{"user": "ana", "drept": "(ALL) NOPASSWD: /usr/bin/vim.basic",
          "risc": "mare"},
         {"user": "ana", "drept": "(ALL) /usr/bin/apt", "risc": "normal"},
         {"user": "www-data", "drept": "(root) NOPASSWD: /usr/bin/find",
          "risc": "mare"}]

_CRON = [{"user": "root",
          "comanda": "cd / && run-parts --report /etc/cron.hourly"},
         {"user": "root", "comanda": "/opt/backup/run.sh"},
         {"user": "www-data", "comanda": "/home/www-data/clean.sh"}]

_RAPORT = {"suid": _SUID, "sudo": _SUDO, "cron": _CRON}
_RISC_NOI = {"cp": "mare", "find": "mare", "nmap": "mare", "vim.basic": "mare"}
_PERIC = ["/bin/cp", "/usr/bin/find", "/usr/bin/nmap", "/usr/bin/vim.basic"]


SARCINI = [
    {"nr": 1, "parte": "A", "functie": "citeste_linii",
     "titlu": "Lista randurilor folositoare",
     "indiciu": "Un rand gol dupa .strip() nu se pastreaza. Comentariile incep cu diez.",
     "teste": [((f("suid.txt"),), _SUID_LINII),
               ((f("crontab.txt"),), _CRON_LINII)]},
    {"nr": 2, "parte": "A", "functie": "nume",
     "titlu": "Numele fisierului dintr-o cale",
     "indiciu": "rsplit(\"/\", 1) taie o singura data, de la dreapta.",
     "teste": [(("/usr/bin/find",), "find"), (("/bin/cp",), "cp"),
               (("/usr/bin/vim.basic",), "vim.basic"),
               (("fara_slash",), "fara_slash")]},
    {"nr": 3, "parte": "A", "functie": "suid_constatari",
     "titlu": "Lista de dictionare, fara dubluri",
     "indiciu": "set() arunca dublurile, sorted() le pune in ordine. Abia apoi faci dictionarele.",
     "teste": [((f("suid.txt"),), _SUID)]},
    {"nr": 4, "parte": "A", "functie": "sudo_constatari",
     "titlu": "Despachetarea in tuplu",
     "indiciu": "user, drept = rand.split(\" : \", 1) despacheteaza un tuplu de doua valori.",
     "teste": [((f("sudo.txt"),), _SUDO)]},
    {"nr": 5, "parte": "A", "functie": "cron_constatari",
     "titlu": "Campurile unui rand de crontab",
     "indiciu": "split() fara argument desparte la orice spatiu si tab. Userul e campul cu indicele 5.",
     "teste": [((f("crontab.txt"),), _CRON)]},
    {"nr": 6, "parte": "A", "functie": "enumereaza",
     "titlu": "Dictionarul cu toate categoriile",
     "indiciu": "os.path.join(dosar, \"suid.txt\") lipeste calea corect pe orice sistem.",
     "teste": [((START,), _RAPORT)]},
    {"nr": 7, "parte": "A", "functie": "utilizatori_implicati",
     "titlu": "Reuniunea a doua multimi",
     "indiciu": "Operatorul | reuneste doua multimi si arunca dublurile.",
     "teste": [((_RAPORT,), {"ana", "root", "www-data"})]},

    {"nr": 8, "parte": "B", "functie": "cai",
     "titlu": "De la fisier la multime",
     "indiciu": "set(citeste_linii(fisier)). Iese 13, nu 14: o cale se repeta.",
     "teste": [((f("suid.txt"),), _CAI_ACUM), ((f("baza_suid.txt"),), _CAI_BAZA)]},
    {"nr": 9, "parte": "B", "functie": "suid_noi",
     "titlu": "Diferenta de multimi",
     "indiciu": "Un singur operator: acum - baza.",
     "teste": [((_CAI_ACUM, _CAI_BAZA), _NOI),
               (({"a", "b", "c"}, {"a", "b"}), {"c"})]},
    {"nr": 10, "parte": "B", "functie": "risc_pe_nume",
     "titlu": "Dictionar prin comprehension",
     "indiciu": "{nume(c): (\"mare\" if nume(c) in GTFO else \"normal\") for c in cai}",
     "teste": [((_NOI,), _RISC_NOI)]},
    {"nr": 11, "parte": "B", "functie": "periculoase_noi",
     "titlu": "Filtrul final",
     "indiciu": "sorted() intai, apoi pastrezi doar caile al caror nume e in GTFO.",
     "teste": [((_NOI,), _PERIC), ((set(),), [])]},
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
    """Harta masinii tinta, care se completeaza pe masura ce rezolvi.

    Fiecare rand e o constatare din raport. Cat timp sarcina care o produce
    nu e rezolvata, randul sta in ceata (puncte). Cand o rezolvi, se aprinde
    cu datele adevarate: chiar rezultatul codului tau. Harta nu e un joc pe
    deasupra lucrarii - este raportul tau, vazut dintr-o privire.
    """
    gata = set(s["nr"] for s, reusit, _ in stare if reusit)

    def are(*nrs):
        return all(n in gata for n in nrs)

    def rand(eticheta, deblocat, text, cheie):
        tinta = text if deblocat else "in ceata ... (rezolva %s)" % cheie
        marcaj = " +" if deblocat else "  "
        print("  %s %-11s %s" % (marcaj, eticheta, tinta[:54]))

    # datele adevarate, luate din constatarile corecte
    peric = [c["nume"] for c in _SUID if c["risc"] == "mare"]
    sudo_np = sorted({c["user"] for c in _SUDO if c["risc"] == "mare"})
    cron_useri = sorted({c["user"] for c in _CRON})
    toti_useri = sorted({c["user"] for c in _SUDO} | {c["user"] for c in _CRON})
    noi = sorted(_NOI)
    nume_peric = [c.rsplit("/", 1)[-1] for c in _PERIC]

    titlu("MASINA TINTA  -  enumerare spre root", "-")
    print()
    rand("capturi:", are(1), "suid, sudo, crontab - %d randuri citite" %
         len(CAPTURI["suid.txt"]), "sarcina 1")
    rand("nume:", are(2), "numele binarelor, desprinse din cai", "sarcina 2")
    rand("SUID:", are(3), "%d fisiere, %d PERICULOASE: %s" %
         (len(_SUID), len(peric), " ".join(peric)), "sarcina 3")
    rand("sudo:", are(4), "NOPASSWD la: %s" % ", ".join(sudo_np), "sarcina 4")
    rand("cron:", are(5), "ruleaza ca: %s" % ", ".join(cron_useri), "sarcina 5")
    rand("conturi:", are(6, 7), "implicati pe masina: %s" %
         ", ".join(toti_useri), "sarcinile 6-7")
    print()
    rand("ce-i NOU:", are(8, 9), "%d SUID puse de atacator: %s" %
         (len(noi), " ".join(n.rsplit("/", 1)[-1] for n in noi)),
         "sarcinile 8-9")
    rand("DRUM ROOT:", are(10, 11), "%s  ->  toate dau root" %
         " ".join(nume_peric), "sarcinile 10-11")
    print()
    if are(*range(1, 12)):
        print("  >>> Masina e cartografiata. Drumul spre root e limpede. <<<")
    else:
        print("  Rezolva sarcinile ca sa risipesti ceata de pe masina.")


def arata_progres(stare):
    titlu("LABORATORUL 7  -  COLECTII", "=")
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
        print("   %s %2d. %-34s %s" % (semn, s["nr"], s["titlu"],
                                       "" if reusit else mesaj.split(chr(10))[0][:28]))
    print()
    print("  Nota ta acum: %d" % max(1, min(10, p)))


def arata_sarcina(s, reusit, mesaj):
    titlu("SARCINA %d  (partea %s)  -  %s" % (s["nr"], s["parte"], s["titlu"]))
    print()
    doc = (globals().get(s["functie"]).__doc__ or "") if globals().get(s["functie"]) else ""
    for rand in doc.strip().split(chr(10)):
        print("   " + rand.strip())
    print()
    if reusit:
        print("   REZOLVATA.")
    else:
        print("   Inca nu merge:")
        for rand in mesaj.split(chr(10)):
            print("      " + rand)
        print()
        print("   Indiciu: " + s["indiciu"])


def _tine_fereastra_deschisa():
    """Pe Windows, cand e o fereastra dar nu se poate citi tastatura."""
    if os.name == "nt" and sys.stdout.isatty():
        try:
            os.system("pause")
        except Exception:
            pass


def iesire_fara_terminal():
    """Spune limpede ca programul are nevoie de un terminal si nu dispare."""
    print()
    print("   " + "!" * 66)
    print("   Programul s-a inchis fiindca NU a fost pornit dintr-un terminal")
    print("   si nu poate citi tastatura (de obicei, cand dai dublu-clic).")
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
    except (EOFError, KeyboardInterrupt):
        raise SystemExit


def instructiuni():
    titlu("CUM SE LUCREAZA")
    print("""
   1. Lasa acest program pornit.

   2. Deschide fisierul  L7_TP_Nume_Prenume_SI-26x.py  intr-un editor
      (Notepad merge, dar VS Code e mai comod).

   3. Cauta functia sarcinii la care lucrezi. Fiecare are un  # TODO
      si se termina cu  raise NotImplementedError.
      Stergi randul acela si scrii codul tau.

   4. SALVEZI fisierul.

   5. Vii inapoi in aceasta fereastra si apesi Enter. Programul reciteste
      fisierul de pe disc si iti spune imediat daca merge.

   Nu inchizi si nu repornesti programul dupa fiecare schimbare.

   Capturile de pe masina sunt in folderul  start/ , creat la prima
   pornire. Le poti deschide si citi oricand: sunt simple fisiere text.
""")


# ---------------------------------------------------------------------------
#  Predarea: scrie fisierele cerute in fisa
# ---------------------------------------------------------------------------
def pregateste_predarea(stare):
    """Scrie codul tau in structura ceruta de fisa lucrarii."""
    p = punctaj(stare)
    if p < len(SARCINI):
        print()
        print("   Mai ai %d sarcini nerezolvate. Le poti preda si asa, dar"
              % (len(SARCINI) - p))
        print("   fisierele vor contine functii care inca dau eroare.")
        print()
        print("   Continui? (da/nu): ", end="")
        try:
            if not input().strip().lower().startswith("d"):
                return
        except (EOFError, KeyboardInterrupt):
            return

    sursa = io.open(os.path.abspath(sys.argv[0]), encoding="utf-8").read()
    zona = sursa[:sursa.find(MARCAJ_ZONA)]
    corp = zona[zona.find("#  PARTEA A"):]

    # Totul intra in Laborator_7/, ca sa se vada dintr-o privire in depozit.
    # Inauntru pastram arsenal/privesc, fiindca fisa cere rularea cu
    # python -m arsenal.privesc.enum, iar diferenta.py importa de acolo.
    LUCRARE = os.path.join(DOSAR, "Laborator_7")
    dest = os.path.join(LUCRARE, "arsenal", "privesc")
    os.makedirs(dest, exist_ok=True)
    for sub in ("", ):
        pass
    # arsenal/ si arsenal/privesc trebuie sa fie pachete, ca sa mearga -m
    io.open(os.path.join(LUCRARE, "arsenal", "__init__.py"), "w",
            encoding="utf-8").write("")
    # Python lasa in urma foldere __pycache__. Nu au ce cauta in depozit.
    io.open(os.path.join(LUCRARE, ".gitignore"), "w", encoding="utf-8").write(
        "__pycache__/" + chr(10) + "*.pyc" + chr(10) +
        "venv/" + chr(10) + ".venv/" + chr(10))
    io.open(os.path.join(dest, "__init__.py"), "w", encoding="utf-8").write("")

    antet = ('# -*- coding: utf-8 -*-' + chr(10) +
             '"""Laboratorul 7 - enumerare spre root. Generat din programul'
             + chr(10) + 'de laborator, cu codul scris de student."""' + chr(10) +
             "import argparse, io, json, os" + chr(10) + chr(10) +
             'GTFO = ' + repr(GTFO) + chr(10) + chr(10))

    io.open(os.path.join(dest, "enum.py"), "w", encoding="utf-8").write(
        antet + corp + chr(10) + CODA_ENUM)
    io.open(os.path.join(dest, "diferenta.py"), "w", encoding="utf-8").write(
        CODA_DIFERENTA)
    io.open(os.path.join(dest, "test_diferenta.py"), "w", encoding="utf-8").write(
        CODA_TEST)

    # raportul, generat cu codul studentului
    try:
        raport = globals()["enumereaza"](START)
        io.open(os.path.join(dest, "enum.json"), "w", encoding="utf-8").write(
            json.dumps(raport, indent=2, ensure_ascii=False))
        gata_json = True
    except Exception:
        gata_json = False

    # capturile merg si ele, ca lucrarea sa poata fi rulata de asistent
    sdest = os.path.join(dest, "start")
    os.makedirs(sdest, exist_ok=True)
    for fisier, randuri in CAPTURI.items():
        io.open(os.path.join(sdest, fisier), "w", encoding="utf-8").write(
            chr(10).join(randuri) + chr(10))

    titlu("PREDAREA E PREGATITA")
    print()
    print("   Am scris, in folderul lucrarii:")
    print()
    print("      Laborator_7/arsenal/privesc/enum.py            codul tau")
    print("      Laborator_7/arsenal/privesc/diferenta.py       partea B")
    print("      Laborator_7/arsenal/privesc/test_diferenta.py  testul")
    print("      Laborator_7/arsenal/privesc/enum.json          %s" %
          ("raportul generat" if gata_json else "NU s-a putut genera"))
    print("      Laborator_7/arsenal/privesc/start/             capturile")
    print()

    nerezolvate = [s["nr"] for s, reusit, _ in stare if not reusit]
    if nerezolvate:
        linie("!")
        print("  ATENTIE. Mai ai de rezolvat sarcinile: " +
              ", ".join(str(x) for x in nerezolvate))
        print()
        print("  Pana le termini, comanda de verificare de mai jos NU va")
        print("  merge: se opreste cu NotImplementedError la prima functie")
        print("  nescrisa. Asa trebuie sa fie, nu e o defectiune.")
        print()
        print("  Poti urca lucrarea si asa, dar asistentul va vedea ca e")
        print("  neterminata. Mai bine te intorci la sarcini.")
        linie("!")
        print()

    print("   Verifica-l o data cu:")
    print()
    print("      cd Laborator_7")
    print("      python -m arsenal.privesc.enum arsenal/privesc/start")
    if nerezolvate:
        print()
        print("   (va merge dupa ce rezolvi toate sarcinile)")
    print()
    print("   Apoi urca totul in depozitul tau:")
    print()
    print("      git add Laborator_7")
    print('      git commit -m "Laboratorul 7: colectii, enumerare spre root"')
    print("      git push")


CODA_ENUM = '''

def main():
    p = argparse.ArgumentParser()
    p.add_argument("capturi")
    p.add_argument("--json", action="store_true")
    a = p.parse_args()
    raport = enumereaza(a.capturi)
    if a.json:
        print(json.dumps(raport, indent=2, ensure_ascii=False))
        return
    for categorie, lista in raport.items():
        mari = [c for c in lista if c.get("risc") == "mare"]
        print("%s: %d gasite, %d cu risc mare" % (categorie, len(lista), len(mari)))
    useri = utilizatori_implicati(raport)
    print("utilizatori implicati:", ", ".join(sorted(useri)))
    with io.open("enum.json", "w", encoding="utf-8") as fis:
        json.dump(raport, fis, indent=2, ensure_ascii=False)
    print("Raport salvat in enum.json")


if __name__ == "__main__":
    main()
'''

CODA_DIFERENTA = '''# -*- coding: utf-8 -*-
"""Laboratorul 7, partea B: ce e nou fata de un sistem curat."""
import os
from arsenal.privesc.enum import citeste_linii, nume, GTFO

AICI = os.path.join(os.path.dirname(os.path.abspath(__file__)), "start")


def cai(fisier):
    return set(citeste_linii(fisier))


def main():
    baza = cai(os.path.join(AICI, "baza_suid.txt"))
    acum = cai(os.path.join(AICI, "suid.txt"))
    print("baza:", len(baza), " acum:", len(acum))
    noi = acum - baza
    print(len(noi), "SUID noi fata de sistemul curat")
    for c in sorted(noi):
        print(" ", c)
    risc = {nume(c): ("mare" if nume(c) in GTFO else "normal") for c in noi}
    periculoase = [c for c in sorted(noi) if nume(c) in GTFO]
    print("periculoase NOI:", periculoase)
    return risc


if __name__ == "__main__":
    main()
'''

CODA_TEST = '''# -*- coding: utf-8 -*-
"""Un test care prinde regresia: diferenta de multimi da doar ce e nou."""


def test_doar_ce_e_nou():
    acum = {"a", "b", "c"}
    baza = {"a", "b"}
    assert acum - baza == {"c"}
'''


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
    if pregateste_capturile():
        print()
        print("   Am creat folderul  start/  cu capturile de pe masina.")

    while True:
        stare, eroare = stare_completa()
        if stare is None:
            titlu("CODUL TAU NU POATE FI CITIT", "!")
            print()
            for rand in eroare.split(chr(10)):
                print("   " + rand)
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
        # Orice alta eroare: o aratam si tinem fereastra deschisa, ca sa
        # nu dispara inainte sa apuci sa o citesti.
        print()
        print("   A aparut o eroare neasteptata in program:")
        print("   " + type(_e).__name__ + ": " + str(_e))
        _tine_fereastra_deschisa()
