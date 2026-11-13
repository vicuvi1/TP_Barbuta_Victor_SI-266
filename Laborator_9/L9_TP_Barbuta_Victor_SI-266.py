# -*- coding: utf-8 -*-
"""
===============================================================================

   LUCRAREA DE LABORATOR NR. 9  -  OBIECTE SI CLASE
   Windows in Python: inventar de procese si jurnalul de evenimente

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

          python L9_TP_Nume_Prenume_SI-26x.py

   3. Iti apare un meniu. Incepe cu optiunea  c , "Cum se lucreaza".

   -----------------------------------------------------------------------

   CE AI DE FACUT

   Tinta e o masina Windows. Modelezi procesele si evenimentele de securitate
   ca OBIECTE: clase cu campuri si metode. Apoi le interoghezi ca sa gasesti
   ce e suspect.

   Partea A - procesul si evenimentul ca obiecte   4 sarcini
   Partea B - clasa Inventar si raportul           4 sarcini

   Fiecare sarcina valoreaza un punct. Nota = punctajul obtinut.

   Clasele sunt deja scrise (campurile lor). Tu completezi METODELE si
   functiile: fiecare are un  # TODO  si se termina cu  raise NotImplementedError.
   Scrii codul, SALVEZI fisierul si apesi Enter in fereastra programului.

   -----------------------------------------------------------------------

   CAPTURILE

   La prima pornire, programul creeaza singur folderul  start/  cu doua
   fisiere: procese.json si evenimente.json. Nu ai nimic de descarcat.

   Pe o masina reala, procese.json s-ar obtine cu Get-Process / tasklist,
   iar evenimente.json cu Get-WinEvent. Au fost capturate o data, ca sa
   lucrezi pe date stabile.

===============================================================================
"""
import io
import json
import os
import sys
from dataclasses import dataclass, asdict

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

VERSIUNE = "L9-v1"
DOSAR = os.path.dirname(os.path.abspath(sys.argv[0])) or os.getcwd()
START = os.path.join(DOSAR, "start")

# Cai din care un proces nu ar trebui sa ruleze: folderul utilizatorului.
CAI_SUSPECTE = ("\\Temp\\", "\\Roaming\\")
# ID-uri de evenimente Windows cu sens: logon esuat, jurnal sters, serviciu nou.
SUSPECTE_ID = {4625, 1102, 7045}


# ===========================================================================
#
#    A I C I   S C R I I   T U
#
#    Clasele sunt gata (campurile lor). Tu scrii METODELE si functiile de mai
#    jos: fiecare are un  # TODO  si se termina cu  raise NotImplementedError.
#    Stergi randul acela si scrii codul tau in locul lui.
#
# ===========================================================================

# ---------------------------------------------------------------------------
#  PARTEA A - procesul si evenimentul ca obiecte
# ---------------------------------------------------------------------------

@dataclass
class Proces:
    """Un proces de pe masina, cu patru campuri legate."""
    pid: int
    nume: str
    user: str
    cale: str

    def e_suspect(self):
        """Sarcina 1. True daca procesul ruleaza dintr-o cale suspecta.

        Intoarce True daca una din CAI_SUSPECTE apare in self.cale, altfel
        False. Un proces care ruleaza din Temp sau Roaming e un semn clasic.

        Proces(1, "x.exe", "ana", r"C:\\Users\\ana\\AppData\\Local\\Temp\\x.exe")
            .e_suspect()  ->  True
        """
        for c in CAI_SUSPECTE:
            if c in self.cale:
                return True
        return False


@dataclass
class Eveniment:
    """Un eveniment din jurnalul de securitate Windows."""
    id: int
    nivel: str
    sursa: str
    cont: str
    mesaj: str

    def e_suspect(self):
        """Sarcina 2. True daca evenimentul merita atentie.

        Intoarce True daca self.id e in SUSPECTE_ID SAU self.nivel este
        "critical". Altfel False.

        Eveniment(4625, "warning", "Security", "admin", "...").e_suspect() -> True
        Eveniment(6008, "critical", "EventLog", "SYSTEM", "...").e_suspect() -> True
        """
        return self.id in SUSPECTE_ID or self.nivel == "critical"


def procese_din_json(cale):
    """Sarcina 3. Incarca o lista de obiecte Proces dintr-un fisier JSON.

    Citeste fisierul si intoarce o lista de Proces. Proces(**d) despacheteaza
    un dictionar din JSON direct in campurile obiectului, pe nume.

    procese_din_json("start/procese.json")  ->  lista cu 7 obiecte Proces
    """
    with open(cale, encoding="utf-8") as f:
        return [Proces(**d) for d in json.load(f)]


def evenimente_din_json(cale):
    """Sarcina 4. Incarca o lista de obiecte Eveniment dintr-un fisier JSON.

    La fel ca procese_din_json, dar pentru Eveniment.

    evenimente_din_json("start/evenimente.json")  ->  lista cu 8 obiecte
    """
    with open(cale, encoding="utf-8") as f:
        return [Eveniment(**d) for d in json.load(f)]


# ---------------------------------------------------------------------------
#  PARTEA B - clasa Inventar si raportul
# ---------------------------------------------------------------------------

@dataclass
class Inventar:
    """Tine lista de procese si stie sa o interogheze."""
    procese: list

    @classmethod
    def din_json(cls, cale):
        """Sarcina 5. Constructor alternativ: umple inventarul din JSON.

        E o metoda de clasa (@classmethod): primeste clasa in cls si intoarce
        un Inventar nou, cu lista de procese incarcata din fisier.

        Inventar.din_json("start/procese.json")  ->  un Inventar cu 7 procese
        """
        with open(cale, encoding="utf-8") as f:
            return cls([Proces(**d) for d in json.load(f)])

    def __len__(self):
        return len(self.procese)

    def suspecte(self):
        """Sarcina 6. Lista proceselor care se declara suspecte.

        Intoarce lista obiectelor Proces din self.procese pentru care
        p.e_suspect() este True, in ordinea din inventar.
        """
        return [p for p in self.procese if p.e_suspect()]

    def pe_user(self):
        """Sarcina 7. Gruparea numelor de proces pe utilizator.

        Intoarce un dictionar user -> lista de nume de proces ale acelui
        utilizator, in ordinea din inventar. Foloseste setdefault.

        {"SYSTEM": ["System", "svchost.exe"], "ana": ["explorer.exe", ...]}
        """
        d = {}
        for p in self.procese:
            d.setdefault(p.user, []).append(p.nume)
        return d


def raport(dosar):
    """Sarcina 8. Raportul complet, ca dictionar gata de pus in JSON.

    Primeste folderul capturilor. Incarca procesele si evenimentele, apoi
    intoarce un dictionar cu patru chei:

        {"procese": numarul de procese,
         "suspecte": [asdict(p) pentru fiecare proces suspect],
         "evenimente": numarul de evenimente,
         "alarma": [asdict(e) pentru fiecare eveniment suspect]}

    asdict(obiect) transforma un obiect @dataclass inapoi in dictionar.
    Nu tipari nimic aici; doar intoarce.
    """
    inv = Inventar.din_json(dosar + "/procese.json")
    ev = evenimente_din_json(dosar + "/evenimente.json")
    return {
        "procese": len(inv),
        "suspecte": [asdict(p) for p in inv.suspecte()],
        "evenimente": len(ev),
        "alarma": [asdict(e) for e in ev if e.e_suspect()],
    }


#  @@ AICI SE TERMINA ZONA TA @@
# ===========================================================================

# Marcajul e lipit din doua bucati dinadins: altfel randul acesta ar contine
# el insusi textul cautat, iar taierea ar cadea in mijlocul lui.
MARCAJ_ZONA = "@@ AICI SE TERMINA " + "ZONA TA @@"

# Capturile de pe masina Windows. Doua procese ruleaza din folderul
# utilizatorului (update.exe din Temp, svch0st.exe din Roaming - cu zero in
# loc de o, imita svchost.exe). Cinci evenimente merita atentie.
PROCESE = [
    {"pid": 101,  "nume": "System",        "user": "SYSTEM", "cale": r"C:\Windows\System32\ntoskrnl.exe"},
    {"pid": 740,  "nume": "svchost.exe",   "user": "SYSTEM", "cale": r"C:\Windows\System32\svchost.exe"},
    {"pid": 2100, "nume": "explorer.exe",  "user": "ana",    "cale": r"C:\Windows\explorer.exe"},
    {"pid": 2560, "nume": "chrome.exe",    "user": "ana",    "cale": r"C:\Program Files\Google\Chrome\Application\chrome.exe"},
    {"pid": 3120, "nume": "update.exe",    "user": "ana",    "cale": r"C:\Users\ana\AppData\Local\Temp\update.exe"},
    {"pid": 3450, "nume": "powershell.exe","user": "ana",    "cale": r"C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe"},
    {"pid": 3890, "nume": "svch0st.exe",   "user": "ana",    "cale": r"C:\Users\ana\AppData\Roaming\svch0st.exe"},
]
EVENIMENTE = [
    {"id": 4625, "nivel": "warning",     "sursa": "Security", "cont": "administrator", "mesaj": "An account failed to log on"},
    {"id": 4625, "nivel": "warning",     "sursa": "Security", "cont": "administrator", "mesaj": "An account failed to log on"},
    {"id": 7045, "nivel": "warning",     "sursa": "Service Control Manager", "cont": "SYSTEM", "mesaj": "A service was installed in the system"},
    {"id": 6008, "nivel": "critical",    "sursa": "EventLog", "cont": "SYSTEM", "mesaj": "The previous system shutdown was unexpected"},
    {"id": 1102, "nivel": "critical",    "sursa": "Security", "cont": "administrator", "mesaj": "The audit log was cleared"},
    {"id": 4624, "nivel": "information", "sursa": "Security", "cont": "ana", "mesaj": "An account was successfully logged on"},
    {"id": 4634, "nivel": "information", "sursa": "Security", "cont": "ana", "mesaj": "An account was logged off"},
    {"id": 7036, "nivel": "information", "sursa": "Service Control Manager", "cont": "SYSTEM", "mesaj": "A service entered the running state"},
]


def pregateste_capturile():
    """Scrie folderul start/ cu cele doua fisiere JSON la prima pornire."""
    nou = False
    if not os.path.isdir(START):
        os.makedirs(START)
        nou = True
    for nume, date in (("procese.json", PROCESE), ("evenimente.json", EVENIMENTE)):
        cale = os.path.join(START, nume)
        if not os.path.exists(cale):
            json.dump(date, io.open(cale, "w", encoding="utf-8"),
                      indent=2, ensure_ascii=False)
            nou = True
    return nou


# ---------------------------------------------------------------------------
#  Rezultatele asteptate
# ---------------------------------------------------------------------------
_N_PROC = 7
_SUSP_PID = [3120, 3890]
_PE_USER = {
    "SYSTEM": ["System", "svchost.exe"],
    "ana": ["explorer.exe", "chrome.exe", "update.exe", "powershell.exe", "svch0st.exe"],
}
_N_EV = 8
_N_ALARM = 5


# ---------------------------------------------------------------------------
#  Reincarcarea codului scris de student
# ---------------------------------------------------------------------------
def reincarca_codul():
    """Reciteste de pe disc zona in care scrii tu si actualizeaza clasele.
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
                       + chr(10) + "Codul dintr-o metoda se scrie cu 4 spatii "
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


def _scurt(v, maxim=56):
    t = repr(v)
    return t if len(t) <= maxim else t[:maxim - 3] + "..."


# ---------------------------------------------------------------------------
#  Verificatorii fiecarei sarcini
# ---------------------------------------------------------------------------
def _p(pid, nume, user, cale):
    return globals()["Proces"](pid, nume, user, cale)


def _e(idp, nivel, sursa, cont, mesaj):
    return globals()["Eveniment"](idp, nivel, sursa, cont, mesaj)


def v_proces_suspect():
    temp = _p(1, "x.exe", "ana", "C:\\Users\\ana\\AppData\\Local\\Temp\\x.exe")
    roam = _p(2, "y.exe", "ana", "C:\\Users\\ana\\AppData\\Roaming\\y.exe")
    curat = _p(3, "svchost.exe", "SYSTEM", "C:\\Windows\\System32\\svchost.exe")
    if temp.e_suspect() is not True:
        return False, "Un proces din Temp ar trebui sa fie suspect (True)."
    if roam.e_suspect() is not True:
        return False, "Un proces din Roaming ar trebui sa fie suspect (True)."
    if curat.e_suspect() is not False:
        return False, "Un proces din System32 NU e suspect (asteptam False)."
    return True, "Corect."


def v_eveniment_suspect():
    for idp, niv, ok in [(4625, "warning", True), (1102, "critical", True),
                         (7045, "warning", True), (6008, "critical", True),
                         (4624, "information", False), (4634, "information", False)]:
        got = _e(idp, niv, "S", "c", "m").e_suspect()
        if got is not ok:
            return False, ("Pentru id=%d nivel=%s asteptam %s, am primit %s."
                           % (idp, niv, ok, got))
    return True, "Corect."


def v_procese_json():
    lst = globals()["procese_din_json"](os.path.join(START, "procese.json"))
    if not isinstance(lst, list) or len(lst) != _N_PROC:
        return False, "Asteptam o lista cu %d procese." % _N_PROC
    if not all(isinstance(x, globals()["Proces"]) for x in lst):
        return False, "Lista trebuie sa contina obiecte Proces, nu dictionare."
    if sum(1 for p in lst if p.e_suspect()) != 2:
        return False, "Ar trebui sa iasa 2 procese suspecte."
    return True, "Corect."


def v_evenimente_json():
    lst = globals()["evenimente_din_json"](os.path.join(START, "evenimente.json"))
    if not isinstance(lst, list) or len(lst) != _N_EV:
        return False, "Asteptam o lista cu %d evenimente." % _N_EV
    if not all(isinstance(x, globals()["Eveniment"]) for x in lst):
        return False, "Lista trebuie sa contina obiecte Eveniment."
    if sum(1 for e in lst if e.e_suspect()) != _N_ALARM:
        return False, "Ar trebui sa iasa %d evenimente de alarma." % _N_ALARM
    return True, "Corect."


def v_inventar():
    inv = globals()["Inventar"].din_json(os.path.join(START, "procese.json"))
    if not isinstance(inv, globals()["Inventar"]):
        return False, "din_json trebuie sa intoarca un Inventar."
    if len(inv) != _N_PROC:
        return False, "len(inventar) ar trebui sa fie %d." % _N_PROC
    return True, "Corect."


def v_suspecte():
    inv = globals()["Inventar"].din_json(os.path.join(START, "procese.json"))
    s = inv.suspecte()
    if not isinstance(s, list) or len(s) != 2:
        return False, "suspecte() ar trebui sa intoarca 2 procese."
    if sorted(p.pid for p in s) != _SUSP_PID:
        return False, "Procesele suspecte asteptate au pid-urile %s." % _SUSP_PID
    return True, "Corect."


def v_pe_user():
    inv = globals()["Inventar"].din_json(os.path.join(START, "procese.json"))
    d = inv.pe_user()
    if d != _PE_USER:
        return False, ("pe_user() nu da gruparea asteptata." + chr(10) +
                       "   asteptam: " + _scurt(_PE_USER, 90) + chr(10) +
                       "   am primit: " + _scurt(d, 90))
    return True, "Corect."


def v_raport():
    r = globals()["raport"](START)
    if not isinstance(r, dict):
        return False, "raport trebuie sa intoarca un dictionar."
    for cheie in ("procese", "suspecte", "evenimente", "alarma"):
        if cheie not in r:
            return False, "Lipseste cheia '%s' din raport." % cheie
    if r["procese"] != _N_PROC or r["evenimente"] != _N_EV:
        return False, "Numarul de procese/evenimente nu e corect."
    if len(r["suspecte"]) != 2 or len(r["alarma"]) != _N_ALARM:
        return False, "Numarul de suspecte/alarma nu e corect."
    if not all(isinstance(x, dict) for x in r["suspecte"]):
        return False, "suspecte din raport trebuie sa fie dictionare (asdict)."
    if {x.get("pid") for x in r["suspecte"]} != set(_SUSP_PID):
        return False, "Procesele suspecte din raport nu sunt cele asteptate."
    return True, "Corect."


def verifica_sarcina(s):
    """Intoarce (reusit, mesaj)."""
    fn = globals().get(s["cheie_functie"])
    if fn is None and s.get("clasa"):
        fn = globals().get(s["clasa"])
    if fn is None:
        return False, "Nu gasesc " + (s.get("clasa") or s["cheie_functie"]) + " in fisier."
    try:
        return s["verificator"]()
    except NotImplementedError:
        return False, "Sarcina nu este inca rezolvata."
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
    return sum(1 for _, reusit, _ in stare if reusit)


# ---------------------------------------------------------------------------
#  Sarcinile
# ---------------------------------------------------------------------------
SARCINI = [
    {"nr": 1, "parte": "A", "cheie_functie": "e_suspect_proces", "clasa": "Proces",
     "titlu": "Metoda e_suspect pe Proces",
     "indiciu": "any(c in self.cale for c in CAI_SUSPECTE).",
     "verificator": v_proces_suspect},
    {"nr": 2, "parte": "A", "cheie_functie": "e_suspect_eveniment", "clasa": "Eveniment",
     "titlu": "Metoda e_suspect pe Eveniment",
     "indiciu": "self.id in SUSPECTE_ID or self.nivel == 'critical'.",
     "verificator": v_eveniment_suspect},
    {"nr": 3, "parte": "A", "cheie_functie": "procese_din_json",
     "titlu": "Incarca procesele din JSON",
     "indiciu": "[Proces(**d) for d in json.load(f)] - ** despacheteaza dictionarul.",
     "verificator": v_procese_json},
    {"nr": 4, "parte": "A", "cheie_functie": "evenimente_din_json",
     "titlu": "Incarca evenimentele din JSON",
     "indiciu": "La fel ca la procese, dar cu Eveniment(**d).",
     "verificator": v_evenimente_json},

    {"nr": 5, "parte": "B", "cheie_functie": "din_json", "clasa": "Inventar",
     "titlu": "Inventar.din_json (constructor de clasa)",
     "indiciu": "return cls([Proces(**d) for d in json.load(f)]).",
     "verificator": v_inventar},
    {"nr": 6, "parte": "B", "cheie_functie": "suspecte", "clasa": "Inventar",
     "titlu": "Inventar.suspecte()",
     "indiciu": "[p for p in self.procese if p.e_suspect()].",
     "verificator": v_suspecte},
    {"nr": 7, "parte": "B", "cheie_functie": "pe_user", "clasa": "Inventar",
     "titlu": "Inventar.pe_user()",
     "indiciu": "d.setdefault(p.user, []).append(p.nume).",
     "verificator": v_pe_user},
    {"nr": 8, "parte": "B", "cheie_functie": "raport",
     "titlu": "Raportul JSON, din obiecte",
     "indiciu": "asdict(p) transforma un obiect inapoi in dictionar.",
     "verificator": v_raport},
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
    """Ancheta pe masina Windows, care se completeaza pe masura ce rezolvi.
    Fiecare rand e un pas al apararii, aprins cu date adevarate cand rezolvi
    sarcina care il produce."""
    gata = set(s["nr"] for s, reusit, _ in stare if reusit)

    def are(*nrs):
        return all(n in gata for n in nrs)

    def rand(eticheta, deblocat, text, cheie):
        tinta = text if deblocat else "in ceata ... (rezolva %s)" % cheie
        marcaj = " +" if deblocat else "  "
        print("  %s %-12s %s" % (marcaj, eticheta, tinta[:52]))

    titlu("MASINA WINDOWS  -  inventar si jurnal", "-")
    print()
    rand("proces:", are(1), "stiu cand un proces ruleaza dintr-o cale suspecta",
         "sarcina 1")
    rand("eveniment:", are(2), "stiu cand un eveniment din jurnal e de alarma",
         "sarcina 2")
    rand("procese:", are(3), "%d procese incarcate ca obiecte" % _N_PROC,
         "sarcina 3")
    rand("evenimente:", are(4), "%d evenimente incarcate ca obiecte" % _N_EV,
         "sarcina 4")
    print()
    rand("inventar:", are(5), "inventarul stie cate procese are (%d)" % _N_PROC,
         "sarcina 5")
    rand("SUSPECTE:", are(6), "2 procese din folderul utilizatorului",
         "sarcina 6")
    rand("pe user:", are(7), "ce ruleaza fiecare cont", "sarcina 7")
    rand("RAPORT:", are(8), "2 procese + %d evenimente de alarma" % _N_ALARM,
         "sarcina 8")
    print()
    if are(*range(1, 9)):
        print("  >>> Masina e inventariata. update.exe si svch0st.exe sunt prinse. <<<")
    else:
        print("  Rezolva sarcinile ca sa risipesti ceata de pe masina.")


def arata_progres(stare):
    titlu("LABORATORUL 9  -  OBIECTE SI CLASE", "=")
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
                                       "" if reusit else mesaj.split(chr(10))[0][:26]))
    print()
    print("  Nota ta acum: %d" % max(1, min(10, p)))


def arata_sarcina(s, reusit, mesaj):
    titlu("SARCINA %d  (partea %s)  -  %s" % (s["nr"], s["parte"], s["titlu"]))
    print()
    # documentatia e in metoda/functia careia ii apartine sarcina
    doc = ""
    tinta = globals().get(s["cheie_functie"])
    if tinta is not None and getattr(tinta, "__doc__", None):
        doc = tinta.__doc__
    elif s.get("clasa"):
        cls = globals().get(s["clasa"])
        m = getattr(cls, s["cheie_functie"], None) if cls else None
        doc = (m.__doc__ or "") if m else ""
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

   2. Deschide fisierul  L9_TP_Nume_Prenume_SI-26x.py  intr-un editor.

   3. Clasele Proces, Eveniment si Inventar sunt deja scrise. Tu completezi
      METODELE lor (e_suspect, din_json, suspecte, pe_user) si functiile
      (procese_din_json, evenimente_din_json, raport). Fiecare are un  # TODO
      si se termina cu  raise NotImplementedError.

   4. SALVEZI fisierul.

   5. Vii inapoi in aceasta fereastra si apesi Enter. Programul reciteste
      fisierul si iti spune imediat daca merge.

   Capturile sunt in  start/ , create la prima pornire: procese.json si
   evenimente.json. Le poti deschide si citi oricand.
""")


# ---------------------------------------------------------------------------
#  Predarea: scrie fisierele cerute in fisa
# ---------------------------------------------------------------------------
MAIN_INVENTAR = (chr(10) + chr(10) +
    "def main():" + chr(10) +
    "    import argparse" + chr(10) +
    "    p = argparse.ArgumentParser()" + chr(10) +
    "    p.add_argument('capturi')" + chr(10) +
    "    p.add_argument('--json', action='store_true')" + chr(10) +
    "    a = p.parse_args()" + chr(10) +
    "    inv = Inventar.din_json(a.capturi + '/procese.json')" + chr(10) +
    "    ev = evenimente_din_json(a.capturi + '/evenimente.json')" + chr(10) +
    "    alarma = [e for e in ev if e.e_suspect()]" + chr(10) +
    "    if a.json:" + chr(10) +
    "        print(json.dumps(raport(a.capturi), indent=2, ensure_ascii=False))" + chr(10) +
    "        return" + chr(10) +
    "    sus = inv.suspecte()" + chr(10) +
    "    print('Procese: %d | suspecte: %d' % (len(inv), len(sus)))" + chr(10) +
    "    for p in sus:" + chr(10) +
    "        print('  [%d] %s  (%s)  %s' % (p.pid, p.nume, p.user, p.cale))" + chr(10) +
    "    print('Evenimente: %d | alarma: %d' % (len(ev), len(alarma)))" + chr(10) +
    "    for e in alarma:" + chr(10) +
    "        print('  %d [%s] %s: %s' % (e.id, e.nivel, e.cont, e.mesaj))" + chr(10) +
    chr(10) + chr(10) + "if __name__ == '__main__':" + chr(10) + "    main()" + chr(10))

CODA_TEST = (
    "# -*- coding: utf-8 -*-" + chr(10) +
    '"""Doua teste: metoda e_suspect pe un proces din Temp si pe unul curat."""' +
    chr(10) + "from arsenal.windows.inventar import Proces" + chr(10) + chr(10) + chr(10) +
    "def test_proces_din_temp_e_suspect():" + chr(10) +
    "    p = Proces(1, 'x.exe', 'ana', r'C:\\Users\\ana\\AppData\\Local\\Temp\\x.exe')" + chr(10) +
    "    assert p.e_suspect() is True" + chr(10) + chr(10) + chr(10) +
    "def test_proces_din_windows_nu_e_suspect():" + chr(10) +
    "    p = Proces(2, 'svchost.exe', 'SYSTEM', r'C:\\Windows\\System32\\svchost.exe')" + chr(10) +
    "    assert p.e_suspect() is False" + chr(10))


def pregateste_predarea(stare):
    nerezolvate = [s["nr"] for s, reusit, _ in stare if not reusit]
    sursa = io.open(os.path.abspath(sys.argv[0]), encoding="utf-8").read()
    zona = sursa[:sursa.find(MARCAJ_ZONA)]
    # pastram tot din zona studentului de la prima clasa in jos (fara intro)
    corp = zona[zona.find("@dataclass"):].rstrip()

    LUCRARE = os.path.join(DOSAR, "Laborator_9")
    dest = os.path.join(LUCRARE, "arsenal", "windows")
    os.makedirs(dest, exist_ok=True)
    io.open(os.path.join(LUCRARE, "arsenal", "__init__.py"), "w",
            encoding="utf-8").write("")
    io.open(os.path.join(dest, "__init__.py"), "w", encoding="utf-8").write("")
    io.open(os.path.join(LUCRARE, ".gitignore"), "w", encoding="utf-8").write(
        "__pycache__/" + chr(10) + "*.pyc" + chr(10) + "venv/" + chr(10) +
        ".venv/" + chr(10))

    antet = ("# -*- coding: utf-8 -*-" + chr(10) +
             '"""Laboratorul 9 - inventar de procese si jurnal ca obiecte."""' +
             chr(10) + "import json" + chr(10) +
             "from dataclasses import dataclass, asdict" + chr(10) + chr(10) +
             "CAI_SUSPECTE = (" + repr("\\Temp\\") + ", " + repr("\\Roaming\\") + ")" +
             chr(10) + "SUSPECTE_ID = {4625, 1102, 7045}" + chr(10) + chr(10) + chr(10))
    io.open(os.path.join(dest, "inventar.py"), "w", encoding="utf-8").write(
        antet + corp + MAIN_INVENTAR)
    io.open(os.path.join(dest, "test_inventar.py"), "w", encoding="utf-8").write(CODA_TEST)

    sdest = os.path.join(dest, "start")
    os.makedirs(sdest, exist_ok=True)
    json.dump(PROCESE, io.open(os.path.join(sdest, "procese.json"), "w",
              encoding="utf-8"), indent=2, ensure_ascii=False)
    json.dump(EVENIMENTE, io.open(os.path.join(sdest, "evenimente.json"), "w",
              encoding="utf-8"), indent=2, ensure_ascii=False)

    titlu("PREDAREA E PREGATITA")
    print()
    print("   Am scris, in folderul lucrarii:")
    print()
    print("      Laborator_9/arsenal/windows/inventar.py       clasele si raportul")
    print("      Laborator_9/arsenal/windows/test_inventar.py  testele")
    print("      Laborator_9/arsenal/windows/start/            capturile JSON")
    print()
    if nerezolvate:
        linie("!")
        print("  ATENTIE. Mai ai de rezolvat sarcinile: " +
              ", ".join(str(x) for x in nerezolvate))
        print("  Pana le termini, comanda de mai jos se opreste cu eroare la")
        print("  prima metoda nescrisa. Asa trebuie, nu e o defectiune.")
        linie("!")
        print()
    print("   Verifica-l asa:")
    print()
    print("      cd Laborator_9")
    print("      python -m arsenal.windows.inventar arsenal/windows/start")
    print()
    print("   Apoi urca totul in depozitul tau:")
    print()
    print("      git add Laborator_9")
    print('      git commit -m "Laboratorul 9: obiecte si clase"')
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
    if pregateste_capturile():
        print()
        print("   Am creat folderul  start/  cu capturile JSON.")

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
