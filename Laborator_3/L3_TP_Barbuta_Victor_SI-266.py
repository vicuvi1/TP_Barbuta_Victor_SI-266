# -*- coding: utf-8 -*-
"""
===============================================================================

   LUCRAREA DE LABORATOR NR. 3  -  INTRODUCERE IN PYTHON

   Universitatea Tehnica a Moldovei
   Facultatea Calculatoare, Informatica si Microelectronica
   Disciplina: Tehnici de programare        Anul I, grupele SI-265 / SI-266

===============================================================================

   CUM PORNESTI PROIECTUL
   ----------------------

   1. Ai nevoie de Python 3 instalat.  Verifica scriind in linia de comanda:

          python --version

      Daca scrie ceva de forma  Python 3.x.x , esti in regula.
      Daca nu, descarca-l gratuit de la  https://www.python.org/downloads/
      La instalare BIFEAZA casuta  "Add Python to PATH" .

   2. Deschide o linie de comanda in folderul unde se afla acest fisier.
      In Windows: intra in folder, scrie  cmd  in bara de adresa a
      ferestrei si apasa Enter.

   3. Porneste programul:

          python L3_TP_Nume_Prenume_SI-26x.py

      (scrie numele fisierului asa cum il vezi in folder)

   4. Iti apare un meniu. Incepe cu optiunea 5, "Cum se lucreaza".

   -----------------------------------------------------------------------

   CE AI DE FACUT

   Partea 1 - Bazele      13 sarcini      13 puncte
   Partea 2 - Jocul        7 misiuni       7 puncte
   Partea 3 - Bonus        6 sarcini       puncte in plus

   Punctaj maxim luat in calcul: 20.  Nota = punctaj / 2.

   Scrii codul in functiile pregatite mai jos, salvezi fisierul si rulezi
   din nou programul. Iti spune imediat ce e corect si ce nu.

   -----------------------------------------------------------------------

   CUM PREDAI

   Din meniu alegi optiunea 6. Programul iti pregateste automat fisierul
   cu denumirea corecta si iti spune ce sa scrii in email.

   Fisier:   L3_TP_Nume_Prenume_Grupa.py
   Exemplu:  L3_TP_Popescu_Ion_SI-266.py
   Adresa:   cristian.gonceari@isa.utm.md
   Subiect:  acelasi text ca numele fisierului, fara .py

===============================================================================
"""

# ============================================================================
#   DATELE TALE  -  completeaza-le inainte de orice altceva
# ============================================================================

NUME = "Barbuta"        # numele de familie, de exemplu "Popescu"
PRENUME = "Victor"     # prenumele, de exemplu "Ion"
GRUPA = "SI-266"       # grupa exact asa: "SI-265" sau "SI-266"



import datetime
import re


# ============================================================================
#   PARTEA 1  -  BAZELE
#   13 sarcini, cate 1 punct fiecare
# ============================================================================

# --- Sarcina 1: Primul program: print sau return ----------------------------
# Scrie funcția saluta(). Ea nu primește nimic la intrare. Trebuie să dea
# înapoi, cu return, șirul de caractere Hello, World! scris exact așa:
# H și W majuscule, virgulă și un spațiu după ea, semnul exclamării la
# final. Nu folosi print, pentru că verificarea se uită doar la valoarea
# returnată.
def saluta():
    return "Hello, World!"

# --- Sarcina 2: Variabile și tipuri de date ---------------------------------
# Scrie funcția celsius_in_fahrenheit(c). Ea primește un singur număr, c,
# care este o temperatură în grade Celsius. Trebuie să calculeze
# temperatura corespunzătoare în grade Fahrenheit după formula
# F = C * 9/5 + 32 și să returneze rezultatul. Nu rotunji și nu afișa
# nimic: doar returnează numărul obținut.
def celsius_in_fahrenheit(c):
    return c * 9 / 5 + 32

# --- Sarcina 3: Liste -------------------------------------------------------
# Scrie funcția cele_mai_mari_trei(numere). Ea primește o listă de
# numere. Trebuie să returneze o listă nouă, care conține cele mai mari
# trei numere din listă, așezate de la cel mai mare la cel mai mic. Dacă
# lista primită are mai puțin de trei elemente, returnează toate
# elementele ei, tot în ordine descrescătoare. Lista primită nu trebuie
# stricată.
def cele_mai_mari_trei(numere):
    ordonate = sorted(numere, reverse=True)
    return ordonate[:3]

# --- Sarcina 4: Operatori de bază și tupluri --------------------------------
# Scrie funcția cat_si_rest(a, b). Ea primește două numere întregi.
# Trebuie să returneze un tuplu cu două valori: pe prima poziție câtul
# împărțirii întregi a lui a la b, iar pe a doua poziție restul acelei
# împărțiri. De exemplu, cat_si_rest(17, 5) trebuie să dea (3, 2).
# Returnează amândouă valorile dintr-un singur return.
def cat_si_rest(a, b):
    cat = a // b
    rest = a % b
    return cat, rest

# --- Sarcina 5: Formatarea textului -----------------------------------------
# Scrie funcția fisa_student(nume, grupa, media). Ea primește numele
# studentului ca text, grupa ca text și media ca număr. Trebuie să
# returneze un singur șir de caractere de forma exactă:
# Popescu Ion (SI-266) - media 8.50. Grupa stă în paranteze rotunde, apoi
# urmează spațiu, cratimă, spațiu, cuvântul media și valoarea scrisă cu
# exact două zecimale.
def fisa_student(nume, grupa, media):
    return f"{nume} ({grupa}) - media {media:.2f}"

# --- Sarcina 6: Operații cu text --------------------------------------------
# Scrie funcția initiale(nume_complet). Ea primește un nume scris ca
# text, de exemplu "popescu ion", și trebuie să returneze inițialele cu
# majuscule, fiecare urmată de punct: "P.I.".
# Numele poate avea două, trei sau mai multe cuvinte și poate avea
# spații în plus la început sau la final, deci curăță-l mai întâi.
# Funcția returnează un șir de caractere; nu îl afișa cu print.
def initiale(nume_complet):
    cuvinte = nume_complet.strip().split()
    rezultat = ""
    for cuvant in cuvinte:
        rezultat = rezultat + cuvant[0].upper() + "."
    return rezultat

# --- Sarcina 7: Instrucțiuni condiționale -----------------------------------
# Scrie funcția calificativ(nota). Ea primește un număr de la 1 la 10 și
# trebuie să returneze un text, în funcție de valoare:
# "excelent" pentru 9 sau 10, "bine" pentru 7 sau 8, "satisfacator"
# pentru 5 sau 6 și "nepromovat" pentru orice notă mai mică de 5.
# Scrie textele exact așa cum sunt date aici, cu litere mici și fără
# diacritice, altfel verificarea nu le recunoaște. Funcția returnează
# textul, nu îl afișează.
def calificativ(nota):
    if nota >= 9:
        return "excelent"
    elif nota >= 7:
        return "bine"
    elif nota >= 5:
        return "satisfacator"
    else:
        return "nepromovat"

# --- Sarcina 8: Cicluri -----------------------------------------------------
# Scrie funcția fizzbuzz(n). Ea trebuie să returneze o listă cu n
# elemente, câte unul pentru fiecare număr de la 1 la n.
# Pentru numerele care se împart și la 3 și la 5 pui textul "FizzBuzz",
# pentru cele care se împart doar la 3 pui "Fizz", pentru cele care se
# împart doar la 5 pui "Buzz", iar pentru restul pui chiar numărul,
# transformat în text.
# Pentru n = 5 rezultatul este ["1", "2", "Fizz", "4", "Buzz"].
# Returnezi lista întreagă, nu afișezi nimic.
def fizzbuzz(n):
    rezultat = []
    for numar in range(1, n + 1):
        if numar % 3 == 0 and numar % 5 == 0:
            rezultat.append("FizzBuzz")
        elif numar % 3 == 0:
            rezultat.append("Fizz")
        elif numar % 5 == 0:
            rezultat.append("Buzz")
        else:
            rezultat.append(str(numar))
    return rezultat

# --- Sarcina 9: Funcții proprii ---------------------------------------------
# Scrie funcția pret_final(pret, reducere=0). Ea primește un preț și un
# procent de reducere. Al doilea parametru este opțional: dacă nu îl dai
# la apelare, valoarea lui este 0, adică fără reducere.
# Funcția returnează prețul care rămâne după ce scazi reducerea,
# rotunjit la două zecimale cu round.
# De exemplu, pret_final(200, 25) întoarce 150.0, iar pret_final(80)
# întoarce 80.0.
def pret_final(pret, reducere=0):
    suma_reducere = pret * reducere / 100
    return round(pret - suma_reducere, 2)

# --- Sarcina 10: Clase și obiecte --------------------------------------------
# Completează clasa Student. În __init__ primești numele și grupa și le
# reții în obiect, iar pe lângă ele pregătești o listă goală de note.
# Metoda adauga_nota(nota) pune nota primită în acea listă și nu
# returnează nimic. Metoda media() returnează media notelor, rotunjită la
# două zecimale; dacă studentul nu are nicio notă, returnează 0.
class Student:
    def __init__(self, nume, grupa):
        self.nume = nume
        self.grupa = grupa
        self.note = []

    def adauga_nota(self, nota):
        self.note.append(nota)

    def media(self):
        if len(self.note) == 0:
            return 0
        return round(sum(self.note) / len(self.note), 2)

# --- Sarcina 11: Dicționare --------------------------------------------------
# Scrie funcția frecventa_litere(text), care primește un șir de caractere
# și returnează un dicționar. Fiecare cheie este o literă scrisă cu literă
# mică, iar valoarea este de câte ori apare acea literă în text. Se numără
# doar literele: spațiile, cifrele și semnele de punctuație se ignoră.
# De exemplu, frecventa_litere("Ana are") dă {"a": 3, "n": 1, "r": 1,
# "e": 1}. Rezultatul se returnează, nu se afișează.
def frecventa_litere(text):
    rezultat = {}
    for caracter in text:
        if caracter.isalpha():
            litera = caracter.lower()
            rezultat[litera] = rezultat.get(litera, 0) + 1
    return rezultat

# --- Sarcina 12: Module și pachete -------------------------------------------
# Scrie funcția zile_intre(data1, data2). Primești două date sub formă de
# șiruri de caractere, scrise în formatul "2026-09-22", adică an, lună, zi.
# Funcția returnează câte zile sunt între cele două date, ca număr întreg
# și întotdeauna pozitiv, indiferent care dată a fost dată prima. Trebuie
# să folosești modulul datetime, nu să calculezi tu zilele.
def zile_intre(data1, data2):
    d1 = datetime.datetime.strptime(data1, "%Y-%m-%d")
    d2 = datetime.datetime.strptime(data2, "%Y-%m-%d")
    diferenta = d2 - d1
    return abs(diferenta.days)

# --- Sarcina 13: Lucrul cu fișiere -------------------------------------------
# Scrie funcția salveaza_si_incarca(cale, note). Primești calea unui fișier
# și o listă de note (numere). Întâi scrii notele în fișier, câte una pe
# rând. Apoi deschizi același fișier, citești rândurile înapoi și
# returnezi lista de note citite, transformate în numere de tip float.
# De exemplu, salveaza_si_incarca("note.txt", [8, 9.5]) returnează
# lista [8.0, 9.5].
def salveaza_si_incarca(cale, note):
    with open(cale, "w") as fisier:
        for nota in note:
            fisier.write(str(nota) + "\n")
    rezultat = []
    with open(cale, "r") as fisier:
        for rand in fisier:
            rand = rand.strip()
            if rand != "":
                rezultat.append(float(rand))
    return rezultat



# ============================================================================
#   PARTEA 2  -  JOCUL
#   7 misiuni, cate 1 punct fiecare. Comenzi: player.move_forward(),
# ============================================================================

#   player.turn_left(), player.turn_right(), player.collect(),
#   player.push(), player.build("bridge"), player.can_move()

# --- Misiunea 1 ------------------------------------------------------------
# Obiectivul il vezi in program, la Partea 2, misiunea 1.
def misiunea_1(player):
    player.move_forward()
    player.move_forward()
    player.move_forward()
    player.move_forward()
    player.move_forward()

# --- Misiunea 2 ------------------------------------------------------------
# Obiectivul il vezi in program, la Partea 2, misiunea 2.
def misiunea_2(player):
    for pas in range(3):
        player.move_forward()
    player.turn_right()
    for pas in range(3):
        player.move_forward()

# --- Misiunea 3 ------------------------------------------------------------
# Obiectivul il vezi in program, la Partea 2, misiunea 3.
def misiunea_3(player):
    for pas in range(15):
        player.move_forward()

# --- Misiunea 4 ------------------------------------------------------------
# Obiectivul il vezi in program, la Partea 2, misiunea 4.
def misiunea_4(player):
    for bustean in range(3):
        player.move_forward()
        player.move_forward()
        player.collect()
    player.move_forward()

# --- Misiunea 5 ------------------------------------------------------------
# Obiectivul il vezi in program, la Partea 2, misiunea 5.
def misiunea_5(player):
    # Nu am reusit sa rezolv aceasta misiune.
    # Stanca se afla pe un coridor ingust, intre mine si stea. Cu push()
    # ea se opreste langa stea si nu am gasit cum sa trec de ea.
    # La moment nu stiu cum se rezolva, de aceea o las nerezolvata.
    pass

# --- Misiunea 6 ------------------------------------------------------------
# Obiectivul il vezi in program, la Partea 2, misiunea 6.
def misiunea_6(player):
    player.move_forward()
    for bustean in range(4):
        player.move_forward()
        player.collect()
    player.move_forward()
    player.build("bridge")
    for pas in range(4):
        player.move_forward()

# --- Misiunea 7 ------------------------------------------------------------
# Obiectivul il vezi in program, la Partea 2, misiunea 7.
def misiunea_7(player):
    # Nu am reusit sa rezolv aceasta misiune.
    # Stanca se opreste in fata primului bustean, asa ca nu am putut
    # ajunge la busteni si nu am putut construi podul.
    # La moment nu stiu cum se rezolva, de aceea o las nerezolvata.
    pass



# ============================================================================
#   PARTEA 3  -  BONUS
#   6 sarcini, cate 1 punct. Acopera sarcinile nerezolvate.
# ============================================================================

# --- Sarcina 1: Liste construite dintr-o singură expresie -------------------
# Scrie funcția def patrate_pare(n): care returnează lista pătratelor
# numerelor PARE de la 1 la n inclusiv. De exemplu, patrate_pare(6)
# returnează [4, 16, 36]. Trebuie să rezolvi folosind o list
# comprehension, nu un ciclu for clasic. Funcția dă lista înapoi cu
# return, nu o afișează cu print.
def patrate_pare(n):
    return [x * x for x in range(1, n + 1) if x % 2 == 0]

# --- Sarcina 2: Funcții anonime cu lambda -----------------------------------
# Scrie funcția def sorteaza_dupa_nota(studenti): care primește o listă de
# tupluri de forma (nume, notă) și returnează o listă nouă, sortată
# descrescător după notă. La note egale, studenții apar în ordine
# alfabetică după nume. De exemplu, sorteaza_dupa_nota([("Ana", 7),
# ("Bogdan", 9)]) returnează [("Bogdan", 9), ("Ana", 7)]. Lista primită
# rămâne neatinsă, iar rezultatul se dă cu return.
def sorteaza_dupa_nota(studenti):
    return sorted(studenti, key=lambda student: (-student[1], student[0]))

# --- Sarcina 3: Tratarea erorilor cu try și except --------------------------
# Scrie funcția def imparte_sigur(a, b): care returnează rezultatul
# împărțirii a / b. Dacă b este zero, funcția returnează None. Dacă a sau
# b nu sunt numere, de exemplu dacă primești un șir de caractere,
# returnează tot None. Funcția nu are voie să se oprească niciodată cu
# eroare, oricare ar fi argumentele primite.
def imparte_sigur(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None
    except TypeError:
        return None

# --- Sarcina 4: Mulțimi (sets) ----------------------------------------------
# Scrie funcția cu semnătura def elemente_comune(a, b): care primește
# două liste și returnează o listă sortată crescător cu valorile care
# apar în AMBELE liste, fără duplicate. De exemplu,
# elemente_comune([1, 2, 2, 3], [2, 3, 4]) trebuie să dea [2, 3].
# Funcția returnează rezultatul cu return, nu îl afișează cu print.
def elemente_comune(a, b):
    comune = set(a) & set(b)
    return sorted(comune)

# --- Sarcina 5: Map, filter, reduce -----------------------------------------
# Scrie funcția cu semnătura def total_peste_prag(preturi, prag): care
# primește o listă de prețuri și un prag, apoi returnează suma prețurilor
# strict mai mari decât pragul, rotunjită la două zecimale. Trebuie să
# folosești filter, iar map sau sum sunt opționale. De exemplu,
# total_peste_prag([10, 50, 100], 20) trebuie să dea 150.0.
def total_peste_prag(preturi, prag):
    mari = filter(lambda pret: pret > prag, preturi)
    total = float(sum(mari))
    return round(total, 2)

# --- Sarcina 6: Expresii regulate -------------------------------------------
# Scrie funcția cu semnătura def extrage_grupe(text): care primește un
# text și returnează lista tuturor codurilor de grupă găsite, în ordinea
# apariției. Un cod de grupă are forma: două litere mari, o cratimă, apoi
# exact trei cifre, de exemplu SI-266. Pentru textul
# "Grupele SI-265 si FI-101 vin azi" funcția trebuie să dea
# ["SI-265", "FI-101"].
def extrage_grupe(text):
    return re.findall(r"\b[A-Z]{2}-[0-9]{3}\b", text)



# ############################################################################
#
#   NU MODIFICA NIMIC SUB ACEASTA LINIE
#
#   Aici se afla motorul care iti verifica raspunsurile si deseneaza jocul.
#   Daca stergi ceva din greseala, descarca din nou fisierul original.
#
# ############################################################################

import sys, os, time, io, re, math, shutil, datetime, traceback

if os.name == "nt":
    os.system("")
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

RESET = "\033[0m"; ALDIN = "\033[1m"; GRI = "\033[90m"; ROSU = "\033[91m"
VERDE = "\033[92m"; GALBEN = "\033[93m"; ALBASTRU = "\033[94m"; CYAN = "\033[96m"

EMAIL_PROFESOR = "cristian.gonceari@isa.utm.md"
COD_LAB = "L3"
LATIME = 74


def _c(t, culoare):
    return culoare + str(t) + RESET


def _sterge_ecran():
    try:
        os.system("cls" if os.name == "nt" else "clear")
    except Exception:
        print("\n" * 40)


def _linie(ch="-"):
    print(_c(ch * LATIME, GRI))


def _titlu(text, culoare=CYAN):
    print()
    print(_c("=" * LATIME, culoare))
    print(_c("  " + text, culoare + ALDIN))
    print(_c("=" * LATIME, culoare))
    print()


def _pauza():
    try:
        input(_c("\n  [Enter] pentru a continua...", GRI))
    except (EOFError, KeyboardInterrupt):
        print()


def _fara_diacritice(s):
    tabel = str.maketrans("ăâîșşțţĂÂÎȘŞȚŢ", "aaissttAAISSTT")
    return s.translate(tabel)


def _egale(a, b):
    if isinstance(a, float) or isinstance(b, float):
        try:
            return abs(float(a) - float(b)) < 1e-9
        except (TypeError, ValueError):
            return False
    if isinstance(a, (list, tuple)) and isinstance(b, (list, tuple)):
        if type(a) != type(b) or len(a) != len(b):
            return False
        return all(_egale(x, y) for x, y in zip(a, b))
    if isinstance(a, dict) and isinstance(b, dict):
        if set(a.keys()) != set(b.keys()):
            return False
        return all(_egale(a[k], b[k]) for k in a)
    return a == b


def _scurt(v, maxim=60):
    t = repr(v)
    return t if len(t) <= maxim else t[:maxim - 3] + "..."


# ---------------------------------------------------------------------------
#  Verificarea unei sarcini
# ---------------------------------------------------------------------------
def verifica_sarcina(s, detaliat=False):
    """Returneaza (reusit, mesaj)."""
    if "verificator" in s:
        try:
            return s["verificator"]()
        except NotImplementedError:
            return False, "Sarcina nu este inca rezolvata."
        except Exception as e:
            return False, "Eroare: " + type(e).__name__ + ": " + str(e)

    f = globals().get(s["functie"])
    if f is None:
        return False, "Functia " + s["functie"] + " nu exista in fisier."
    for args, asteptat in s["teste"]:
        try:
            obtinut = f(*args)
        except NotImplementedError:
            return False, "Sarcina nu este inca rezolvata."
        except Exception as e:
            return False, ("Codul tau a dat eroare la " + s["functie"] +
                           "(" + ", ".join(_scurt(a) for a in args) + ")\n" +
                           "         " + type(e).__name__ + ": " + str(e))
        if not _egale(obtinut, asteptat):
            return False, ("Pentru " + s["functie"] + "(" +
                           ", ".join(_scurt(a) for a in args) + ")\n" +
                           "         asteptam: " + _scurt(asteptat) + "\n" +
                           "         am primit: " + _scurt(obtinut))
    return True, "Corect."


def verifica_misiune(niv, animatie=False):
    f = globals().get("misiunea_" + str(niv["nr"]))
    if f is None:
        return False, "Functia misiunea_" + str(niv["nr"]) + " nu exista."
    try:
        gol = f.__code__.co_code == (lambda p: None).__code__.co_code
    except Exception:
        gol = False
    if gol:
        return False, "Misiunea nu este inca rezolvata."
    return ruleaza_misiune(niv, f, animatie)


def stare_completa():
    """Returneaza lista de (categorie, nr, titlu, reusit)."""
    out = []
    for s in SARCINI_BAZE:
        ok, _ = verifica_sarcina(s)
        out.append(("baze", s["nr"], s["titlu"], ok))
    for niv in NIVELURI:
        ok, _ = verifica_misiune(niv, animatie=False)
        out.append(("joc", niv["nr"], niv["titlu"], ok))
    for s in SARCINI_BONUS:
        ok, _ = verifica_sarcina(s)
        out.append(("bonus", s["nr"], s["titlu"], ok))
    return out


def punctaj(stare):
    ob = sum(1 for c, _, _, ok in stare if c in ("baze", "joc") and ok)
    bo = sum(1 for c, _, _, ok in stare if c == "bonus" and ok)
    total = min(ob + bo, 20)
    nota = max(1, min(10, round(total / 2)))
    return ob, bo, total, nota


# ---------------------------------------------------------------------------
#  Afisare
# ---------------------------------------------------------------------------
def bara(cate, din, latime=30):
    plin = int(latime * cate / din) if din else 0
    return ("[" + _c("#" * plin, VERDE) + _c("." * (latime - plin), GRI) +
            "] " + str(cate) + "/" + str(din))


def arata_progres(stare=None):
    stare = stare or stare_completa()
    _titlu("PROGRESUL TAU")
    for eticheta, cat, total in (("PARTEA 1 - Bazele", "baze", 13),
                                 ("PARTEA 2 - Jocul", "joc", 7),
                                 ("PARTEA 3 - Bonus", "bonus", len(SARCINI_BONUS))):
        randuri = [(n, t, ok) for c, n, t, ok in stare if c == cat]
        cate = sum(1 for _, _, ok in randuri if ok)
        print(_c("  " + eticheta, ALDIN) + "   " + bara(cate, total))
        for n, t, ok in randuri:
            semn = _c("[v]", VERDE) if ok else _c("[ ]", GRI)
            nume = t if ok else _c(t, GRI)
            print("     " + semn + " " + str(n).rjust(2) + ". " + nume)
        print()
    ob, bo, total, nota = punctaj(stare)
    _linie()
    print("  Puncte obligatorii: " + _c(str(ob) + " / 20", ALDIN) +
          "      Bonus: " + _c("+" + str(bo), VERDE if bo else GRI))
    print("  Punctaj total: " + _c(str(total) + " / 20", ALDIN) +
          "      Nota: " + _c(str(nota), (VERDE if nota >= 5 else ROSU) + ALDIN))
    _linie()


def arata_teorie(s):
    _sterge_ecran()
    _titlu(str(s["nr"]) + ". " + s["titlu"])
    for rand in s["teorie"].split("\n"):
        print("  " + rand)
    if s.get("exemplu"):
        print()
        print(_c("  EXEMPLU", GALBEN + ALDIN))
        _linie()
        for rand in s["exemplu"].split("\n"):
            print("  " + _c(rand, CYAN))
        _linie()
    print()
    print(_c("  SARCINA TA", VERDE + ALDIN))
    for rand in s["sarcina"].split("\n"):
        print("  " + rand)
    print()
    print(_c("  Scrie codul in functia  " + s["functie"] +
             "  din partea de sus a fisierului.", GRI))


def arata_indicii(s):
    _titlu("INDICII pentru " + s["titlu"], GALBEN)
    for i, ind in enumerate(s.get("indicii", []), 1):
        print(_c("  Indiciul " + str(i) + ":", GALBEN + ALDIN))
        for rand in ind.split("\n"):
            print("    " + rand)
        print()
        if i < len(s.get("indicii", [])):
            try:
                r = input(_c("    Vrei si urmatorul indiciu? (d/n) ", GRI)).strip().lower()
            except (EOFError, KeyboardInterrupt):
                return
            if r not in ("d", "da", "y", ""):
                return
    if s.get("greseala"):
        print(_c("  GRESEALA FRECVENTA", ROSU + ALDIN))
        for rand in s["greseala"].split("\n"):
            print("    " + rand)


def lucreaza_sarcina(s):
    while True:
        arata_teorie(s)
        ok, msg = verifica_sarcina(s)
        print()
        if ok:
            print(_c("  [v] REZOLVAT - " + msg, VERDE + ALDIN))
        else:
            print(_c("  [ ] Inca nu e gata.", ROSU + ALDIN))
            for rand in msg.split("\n"):
                print(_c("      " + rand, ROSU))
        print()
        print(_c("  [Enter] reverifica    [i] indicii    [q] inapoi la meniu", GRI))
        try:
            r = input("  > ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            return
        if r == "q":
            return
        if r == "i":
            arata_indicii(s)
            _pauza()


def lucreaza_misiune(niv):
    while True:
        _sterge_ecran()
        _titlu("MISIUNEA " + str(niv["nr"]) + " - " + niv["titlu"])
        for rand in niv["obiectiv"].split("\n"):
            print("  " + rand)
        print()
        print(_c("  Harta:", GALBEN + ALDIN))
        for rand in niv["harta"]:
            print("     " + _c(rand, GRI))
        print()
        print(_c("  @ = tu    * = iesirea    o = bustean    R = stanca", GRI))
        print(_c("  ~ = apa   X = loc de pod    # = perete", GRI))
        print()
        print(_c("  Scrie codul in functia  misiunea_" + str(niv["nr"]) +
                 "(player)  din fisier.", GRI))
        print()
        print(_c("  [Enter] ruleaza    [q] inapoi la meniu", GRI))
        try:
            r = input("  > ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            return
        if r == "q":
            return
        ok, msg = verifica_misiune(niv, animatie=True)
        print()
        if ok:
            print(_c("  [v] MISIUNE INDEPLINITA - " + msg, VERDE + ALDIN))
        else:
            print(_c("  [x] " + msg, ROSU + ALDIN))
        _pauza()


# ---------------------------------------------------------------------------
#  Pregatirea fisierului pentru trimitere
# ---------------------------------------------------------------------------
def nume_fisier_corect():
    n = _fara_diacritice(NUME.strip()).replace(" ", "_")
    p = _fara_diacritice(PRENUME.strip()).replace(" ", "_")
    g = GRUPA.strip().upper().replace(" ", "")
    if not (n and p and g):
        return None
    return COD_LAB + "_TP_" + n.capitalize() + "_" + p.capitalize() + "_" + g + ".py"


def date_completate():
    return bool(NUME.strip() and PRENUME.strip() and GRUPA.strip())


def pregateste_trimiterea():
    _sterge_ecran()
    _titlu("PREGATIREA FISIERULUI PENTRU TRIMITERE")
    if not date_completate():
        print(_c("  Nu ai completat datele tale.", ROSU + ALDIN))
        print()
        print("  Deschide fisierul si completeaza, sus de tot:")
        print(_c('      NUME = "Popescu"', CYAN))
        print(_c('      PRENUME = "Ion"', CYAN))
        print(_c('      GRUPA = "SI-266"', CYAN))
        return
    stare = stare_completa()
    ob, bo, total, nota = punctaj(stare)
    nume = nume_fisier_corect()
    sursa = os.path.abspath(__file__)
    tinta = os.path.join(os.path.dirname(sursa), nume)
    try:
        if os.path.abspath(tinta) != sursa:
            shutil.copyfile(sursa, tinta)
        creat = True
    except Exception as e:
        creat = False
        print(_c("  Nu am putut crea copia: " + str(e), ROSU))
    arata_progres(stare)
    print()
    if creat:
        print(_c("  Am pregatit fisierul:", VERDE + ALDIN))
        print(_c("     " + nume, VERDE + ALDIN))
        print(_c("  Il gasesti in acelasi folder cu acest fisier.", GRI))
    print()
    print(_c("  TRIMITE-L ASA:", GALBEN + ALDIN))
    print("     Adresa:  " + _c(EMAIL_PROFESOR, ALDIN))
    print("     Subiect: " + _c(nume[:-3], ALDIN))
    print("     Atasat:  " + _c(nume, ALDIN))
    print()
    print(_c("  Subiectul este exact numele fisierului, fara .py", GRI))


# ---------------------------------------------------------------------------
#  Meniuri
# ---------------------------------------------------------------------------
def meniu_lista(titlu, elemente, cat, stare):
    while True:
        _sterge_ecran()
        _titlu(titlu)
        for el in elemente:
            nr = el["nr"]
            ok = next((o for c, n, _, o in stare if c == cat and n == nr), False)
            semn = _c("[v]", VERDE) if ok else _c("[ ]", GRI)
            print("   " + semn + "  " + str(nr).rjust(2) + ". " + el["titlu"])
        print()
        print(_c("   Scrie numarul sarcinii, sau [q] pentru meniul principal.", GRI))
        try:
            r = input("   > ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            return
        if r == "q":
            return
        if not r.isdigit():
            continue
        el = next((e for e in elemente if e["nr"] == int(r)), None)
        if el is None:
            continue
        if cat == "joc":
            lucreaza_misiune(el)
        else:
            lucreaza_sarcina(el)
        stare = stare_completa()


def banner():
    print()
    print(_c("   ____        _   _                   _        _     ____  ", VERDE))
    print(_c("  |  _ \\ _   _| |_| |__   ___  _ __   | |    __ _| |__ |___ \\ ", VERDE))
    print(_c("  | |_) | | | | __| '_ \\ / _ \\| '_ \\  | |   / _` | '_ \\  __) |", VERDE))
    print(_c("  |  __/| |_| | |_| | | | (_) | | | | | |__| (_| | |_) |/ __/ ", VERDE))
    print(_c("  |_|    \\__, |\\__|_| |_|\\___/|_| |_| |_____\\__,_|_.__/|_____|", VERDE))
    print(_c("         |___/                                               ", VERDE))
    print(_c("        Tehnici de programare  -  Lucrarea de laborator 3", GRI))
    print()


def main():
    while True:
        stare = stare_completa()
        ob, bo, total, nota = punctaj(stare)
        _sterge_ecran()
        banner()
        if date_completate():
            print("   Student: " + _c(NUME + " " + PRENUME + "  (" + GRUPA + ")", ALDIN))
        else:
            print(_c("   ! Nu ti-ai completat NUME, PRENUME si GRUPA sus in fisier.", ROSU))
        print("   Progres: " + bara(total, 20) + "     Nota acum: " +
              _c(str(nota), (VERDE if nota >= 5 else ROSU) + ALDIN))
        print()
        _linie()
        print("   1. Partea 1 - Bazele          (13 sarcini, 13 puncte)")
        print("   2. Partea 2 - Jocul           (7 misiuni, 7 puncte)")
        print("   3. Partea 3 - Bonus           (" + str(len(SARCINI_BONUS)) +
              " sarcini, puncte in plus)")
        print("   4. Vezi progresul detaliat")
        print("   5. Cum se lucreaza (instructiuni)")
        print("   6. Pregateste fisierul pentru trimitere")
        print("   0. Iesire")
        _linie()
        try:
            r = input("   Alege > ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            return
        if r == "1":
            meniu_lista("PARTEA 1 - BAZELE", SARCINI_BAZE, "baze", stare)
        elif r == "2":
            meniu_lista("PARTEA 2 - JOCUL", NIVELURI, "joc", stare)
        elif r == "3":
            meniu_lista("PARTEA 3 - BONUS", SARCINI_BONUS, "bonus", stare)
        elif r == "4":
            arata_progres(stare); _pauza()
        elif r == "5":
            instructiuni(); _pauza()
        elif r == "6":
            pregateste_trimiterea(); _pauza()
        elif r == "0":
            print(_c("\n   Spor la treaba!\n", VERDE))
            return


def instructiuni():
    _sterge_ecran()
    _titlu("CUM SE LUCREAZA")
    for rand in INSTRUCTIUNI.split("\n"):
        print("  " + rand)



def _verif_student():
    S = globals().get("Student")
    if S is None:
        return False, "Clasa Student nu este definita."
    try:
        s = S("Popescu Ion", "SI-266")
    except NotImplementedError:
        return False, "Sarcina nu este inca rezolvata."
    except Exception as e:
        return False, "Student(\"Popescu Ion\", \"SI-266\") a dat eroare: " + str(e)
    if getattr(s, "nume", None) != "Popescu Ion":
        return False, "Obiectul trebuie sa retina numele in atributul self.nume"
    if getattr(s, "grupa", None) != "SI-266":
        return False, "Obiectul trebuie sa retina grupa in atributul self.grupa"
    try:
        m = s.media()
    except Exception as e:
        return False, "media() a dat eroare: " + str(e)
    if not _egale(m, 0):
        return False, ("Un student fara note trebuie sa aiba media 0.\n"
                       "         am primit: " + _scurt(m))
    try:
        s.adauga_nota(8)
        s.adauga_nota(9)
    except Exception as e:
        return False, "adauga_nota() a dat eroare: " + str(e)
    if not _egale(s.media(), 8.5):
        return False, ("Dupa notele 8 si 9, media trebuie sa fie 8.5\n"
                       "         am primit: " + _scurt(s.media()))
    s.adauga_nota(10)
    if not _egale(s.media(), 9.0):
        return False, ("Dupa notele 8, 9 si 10, media trebuie sa fie 9.0\n"
                       "         am primit: " + _scurt(s.media()))
    s2 = S("Ana Pop", "SI-265")
    if not _egale(s2.media(), 0):
        return False, "Fiecare student trebuie sa aiba propria lista de note."
    return True, "Corect."


def _verif_fisier():
    import tempfile
    f = globals().get("salveaza_si_incarca")
    if f is None:
        return False, "Functia salveaza_si_incarca nu exista."
    cale = os.path.join(tempfile.gettempdir(), "lab3_test_note.txt")
    if os.path.exists(cale):
        try:
            os.remove(cale)
        except Exception:
            pass
    try:
        rez = f(cale, [8, 9.5, 10])
    except NotImplementedError:
        return False, "Sarcina nu este inca rezolvata."
    except Exception as e:
        return False, "Codul tau a dat eroare: " + type(e).__name__ + ": " + str(e)
    if not _egale(rez, [8.0, 9.5, 10.0]):
        return False, ("Pentru salveaza_si_incarca(cale, [8, 9.5, 10])\n"
                       "         asteptam: [8.0, 9.5, 10.0]\n"
                       "         am primit: " + _scurt(rez))
    if not os.path.exists(cale):
        return False, "Fisierul nu a fost creat. Trebuie sa scrii efectiv pe disc."
    try:
        with open(cale, "r", encoding="utf-8") as fh:
            randuri = [r.strip() for r in fh if r.strip()]
    except Exception as e:
        return False, "Nu am putut citi fisierul creat: " + str(e)
    if len(randuri) != 3:
        return False, ("Fisierul trebuie sa aiba cate o nota pe fiecare rand.\n"
                       "         am gasit " + str(len(randuri)) + " randuri.")
    rez2 = f(cale, [])
    if not _egale(rez2, []):
        return False, "Pentru o lista goala trebuie sa returnezi []."
    return True, "Corect."

# ---------------------------------------------------------------------------
#  Jocul pe grila
# ---------------------------------------------------------------------------
class EroareJoc(Exception):
    pass


class Jucator:
    """Personajul pe care il comanzi din cod.

    Metode disponibile:
        player.move_forward()   - un pas inainte
        player.turn_left()      - rotire la stanga
        player.turn_right()     - rotire la dreapta
        player.collect()        - ridica busteanul de sub picioare
        player.push()           - impinge stanca din fata
        player.build("bridge")  - construieste un pod (ai nevoie de 4 busteni)
        player.can_move()       - True daca poti face un pas inainte
        player.at_exit()        - True daca esti pe stea
        player.look()           - ce se afla in fata ta, ca text
    """

    DIRECTII = [(-1, 0), (0, 1), (1, 0), (0, -1)]   # N, E, S, V
    SEMNE = ["^", ">", "v", "<"]
    NUME_DIR = ["nord", "est", "sud", "vest"]

    def __init__(self, harta, max_pasi=250, animatie=True):
        self.grila = [list(r) for r in harta]
        self.animatie = animatie
        self.max_pasi = max_pasi
        self.pasi = 0
        self.busteni = 0
        self.jurnal = []
        self.dir = 1
        self.lin = self.col = 0
        for i, rand in enumerate(self.grila):
            for j, c in enumerate(rand):
                if c == "@":
                    self.lin, self.col = i, j
                    self.grila[i][j] = "."
        self._deseneaza("start")

    # -- intern ------------------------------------------------------------
    def _consuma(self, ce):
        self.pasi += 1
        if self.pasi > self.max_pasi:
            raise EroareJoc(
                "Ai depasit " + str(self.max_pasi) + " de actiuni. "
                "Probabil ai un ciclu care nu se opreste niciodata."
            )
        self.jurnal.append(ce)

    def _in_fata(self):
        dl, dc = self.DIRECTII[self.dir]
        return self.lin + dl, self.col + dc

    def _celula(self, l, c):
        if 0 <= l < len(self.grila) and 0 <= c < len(self.grila[l]):
            return self.grila[l][c]
        return "#"

    def _deseneaza(self, actiune=""):
        if not self.animatie:
            return
        _sterge_ecran()
        print(_c("  " + actiune, GRI))
        print()
        for i, rand in enumerate(self.grila):
            out = "   "
            for j, c in enumerate(rand):
                if (i, j) == (self.lin, self.col):
                    out += _c(self.SEMNE[self.dir], VERDE + ALDIN)
                elif c == "#":
                    out += _c("#", GRI)
                elif c == "*":
                    out += _c("*", GALBEN + ALDIN)
                elif c == "o":
                    out += _c("o", GALBEN)
                elif c == "R":
                    out += _c("R", ROSU)
                elif c == "~":
                    out += _c("~", ALBASTRU)
                elif c == "X":
                    out += _c("X", ALBASTRU)
                elif c == "=":
                    out += _c("=", GALBEN)
                else:
                    out += _c(".", GRI)
            print(out)
        print()
        print(_c("   busteni: " + str(self.busteni) +
                 "    actiuni: " + str(self.pasi) +
                 "    privesti spre: " + self.NUME_DIR[self.dir], GRI))
        time.sleep(0.11)

    # -- API pentru student -------------------------------------------------
    def move_forward(self):
        self._consuma("move_forward")
        l, c = self._in_fata()
        tinta = self._celula(l, c)
        if tinta in ("#", "R"):
            self._deseneaza("te-ai lovit de un obstacol")
            raise EroareJoc("Nu poti merge inainte: in fata ta este un obstacol.")
        if tinta == "~":
            self._deseneaza("ai cazut in apa")
            raise EroareJoc("Ai cazut in apa. Ai nevoie de un pod ca sa treci.")
        if tinta == "X":
            self._deseneaza("ai cazut in apa")
            raise EroareJoc("Aici lipseste podul. Construieste-l cu build.")
        self.lin, self.col = l, c
        self._deseneaza("move_forward()")

    def turn_left(self):
        self._consuma("turn_left")
        self.dir = (self.dir - 1) % 4
        self._deseneaza("turn_left()")

    def turn_right(self):
        self._consuma("turn_right")
        self.dir = (self.dir + 1) % 4
        self._deseneaza("turn_right()")

    def collect(self):
        self._consuma("collect")
        if self.grila[self.lin][self.col] != "o":
            self._deseneaza("nu e nimic de colectat aici")
            raise EroareJoc("Nu exista niciun bustean pe casuta pe care stai.")
        self.grila[self.lin][self.col] = "."
        self.busteni += 1
        self._deseneaza("collect()")

    def push(self):
        self._consuma("push")
        l, c = self._in_fata()
        if self._celula(l, c) != "R":
            self._deseneaza("nu e nicio stanca in fata")
            raise EroareJoc("Nu ai ce impinge: in fata ta nu se afla o stanca.")
        dl, dc = self.DIRECTII[self.dir]
        l2, c2 = l + dl, c + dc
        if self._celula(l2, c2) not in (".", "~"):
            self._deseneaza("stanca nu se poate misca")
            raise EroareJoc("Stanca nu are unde sa fie impinsa.")
        self.grila[l][c] = "."
        self.grila[l2][c2] = "." if self._celula(l2, c2) == "~" else "R"
        self._deseneaza("push()")

    def build(self, ce=""):
        self._consuma("build")
        if str(ce).strip().lower() not in ("bridge", "pod"):
            raise EroareJoc('Scrie exact player.build("bridge") ca sa construiesti podul.')
        if self.busteni < 4:
            self._deseneaza("nu ai destui busteni")
            raise EroareJoc("Ai nevoie de 4 busteni ca sa construiesti un pod. "
                            "Ai doar " + str(self.busteni) + ".")
        l, c = self._in_fata()
        if self._celula(l, c) != "X":
            self._deseneaza("nu se poate construi aici")
            raise EroareJoc("Poti construi un pod doar in fata unui semn X.")
        self.grila[l][c] = "="
        self.busteni -= 4
        self._deseneaza("build(\"bridge\")")

    def can_move(self):
        l, c = self._in_fata()
        return self._celula(l, c) in (".", "*", "o", "=")

    def at_exit(self):
        return self.grila[self.lin][self.col] == "*"

    def look(self):
        l, c = self._in_fata()
        return {"#": "perete", ".": "liber", "*": "iesirea", "o": "bustean",
                "R": "stanca", "~": "apa", "X": "loc de pod",
                "=": "pod"}.get(self._celula(l, c), "necunoscut")


def ruleaza_misiune(nivel, functie, animatie=True):
    """Ruleaza codul studentului pe harta nivelului.
    Returneaza (reusit, mesaj)."""
    p = Jucator(nivel["harta"], nivel.get("max_pasi", 250), animatie)
    try:
        functie(p)
    except EroareJoc as e:
        return False, str(e)
    except RecursionError:
        return False, "Prea multe apeluri imbricate."
    except Exception as e:
        return False, "Codul tau a dat eroare: " + type(e).__name__ + ": " + e
    if not p.at_exit():
        return False, "Nu ai ajuns la stea. Te-ai oprit pe alta casuta."
    if p.busteni < nivel.get("busteni_min", 0):
        return False, ("Ai ajuns la iesire, dar ai colectat doar " +
                       str(p.busteni) + " busteni din " +
                       str(nivel["busteni_min"]) + " ceruti.")
    return True, "Misiune indeplinita in " + str(p.pasi) + " actiuni."


NIVELURI = [
    {
        "nr": 1,
        "titlu": "Primii pasi",
        "obiectiv": ("Mergi inainte pana ajungi pe stea.\n"
                     "Ai la dispozitie o singura comanda: player.move_forward()\n"
                     "Numara cate casute sunt pana la stea si apeleaza comanda\n"
                     "de exact atatea ori, una sub alta."),
        "harta": ["#######",
                  "#@....*",
                  "#######"],
        "invata": "apelarea unei functii, o comanda pe fiecare rand",
    },
    {
        "nr": 2,
        "titlu": "Prima cotitura",
        "obiectiv": ("Drumul face un colt. Pe langa move_forward ai acum\n"
                     "player.turn_right() si player.turn_left().\n"
                     "Rotirea nu te muta din loc, doar schimba directia in care privesti."),
        "harta": ["######",
                  "#@...#",
                  "####.#",
                  "####.#",
                  "####*#",
                  "######"],
        "invata": "ordinea instructiunilor conteaza",
    },
    {
        "nr": 3,
        "titlu": "Coridorul lung",
        "obiectiv": ("Pana la stea sunt multi pasi. Poti scrie move_forward de\n"
                     "zeci de ori... sau poti folosi un ciclu:\n"
                     "    for pas in range(10):\n"
                     "        player.move_forward()\n"
                     "Numara exact cate casute sunt si pune numarul in range."),
        "harta": ["##################",
                  "#@..............*#",
                  "##################"],
        "invata": "ciclul for si range",
    },
    {
        "nr": 4,
        "titlu": "Culegatorul",
        "obiectiv": ("Pe drum sunt busteni, marcati cu o. Cand ajungi pe o casuta\n"
                     "cu bustean, apeleaza player.collect() ca sa il ridici.\n"
                     "Trebuie sa aduni toti cei 3 busteni SI sa ajungi pe stea."),
        "harta": ["##########",
                  "#@.o.o.o*#",
                  "##########"],
        "busteni_min": 3,
        "invata": "combinarea mai multor comenzi intr-un ciclu",
    },
    {
        "nr": 5,
        "titlu": "Stanca din drum",
        "obiectiv": ("O stanca, marcata cu R, iti blocheaza drumul.\n"
                     "Apropie-te de ea si foloseste player.push() ca sa o impingi\n"
                     "in directia in care privesti. Apoi treci mai departe."),
        "harta": ["###########",
                  "#@..R....*#",
                  "###########"],
        "invata": "interactiunea cu obiectele",
    },
    {
        "nr": 6,
        "titlu": "Podul peste apa",
        "obiectiv": ("Apa, marcata cu ~, nu se poate traversa. In dreptul semnului X\n"
                     "poti construi un pod, dar ai nevoie de 4 busteni.\n"
                     "Aduna intai cei 4 busteni, apoi opreste-te chiar in fata lui X\n"
                     'si scrie player.build("bridge"). Apoi treci pe pod.'),
        "harta": ["#############",
                  "#@.oooo.X..*#",
                  "#############"],
        "busteni_min": 0,
        "invata": "conditii si resurse",
    },
    {
        "nr": 7,
        "titlu": "Toate la un loc",
        "obiectiv": ("Ultima misiune aduna tot ce ai invatat: coturi, busteni,\n"
                     "o stanca si un pod. Ia-o pas cu pas si deseneaza-ti traseul\n"
                     "pe hartie inainte sa scrii codul.\n"
                     "Trebuie sa ajungi pe stea cu cel putin 1 bustean ramas."),
        "harta": ["############",
                  "#@..R..ooo.#",
                  "##########.#",
                  "#*...X...o.#",
                  "############"],
        "busteni_min": 1,
        "invata": "descompunerea unei probleme mari in pasi mici",
    },
]


SARCINI_BAZE = [
    {
        'nr': 1,
        'functie': 'saluta',
        'titlu': 'Primul program: print sau return',
        'teorie': 'Bine ai venit. Primul program pe care îl scrie oricine învață să\nprogrameze afișează un salut. E un pas mic, dar îți confirmă că totul\nfuncționează și îți arată structura de bază a codului.\n\nO funcție (function) este o mică mașinărie cu nume. Uneori primește\ndate la intrare, face o treabă, iar la final dă înapoi un rezultat. O\ndefinești cu cuvântul def, apoi numele, apoi paranteze și două puncte.\nTot ce ține de funcție se scrie mai la dreapta, indentat cu patru\nspații. Indentarea nu e decor: ea îi spune lui Python unde începe și\nunde se termină funcția.\n\nAcum cel mai important lucru din acest capitol. Instrucțiunea print\nscrie ceva pe ecran, ca să vadă omul. Instrucțiunea return trimite o\nvaloare înapoi, către codul care a chemat funcția, ca să o poată folosi\nprogramul mai departe. Sunt lucruri complet diferite. Gândește-te la un\nbucătar: dacă strigă în sală "am făcut o pizza", asta e print. Dacă\npune pizza pe masa ta, asta e return. Mănânci doar ce ajunge pe masă,\nnu și anunțul.\n\nÎn acest laborator, programul care te verifică apelează funcția ta și\nse uită doar la valoarea returnată. Dacă tu afișezi textul cu print,\nfuncția nu returnează nimic (în Python asta se numește None), iar\nverificarea pică, chiar dacă pe ecran vezi exact ce trebuie. De aceea\nregula e simplă și rămâne valabilă la toate capitolele: folosește\nîntotdeauna return.\n\nUn text scris între ghilimele se numește șir de caractere (string).\nExactitatea contează: majusculele, virgula, spațiul și semnul\nexclamării fac parte din text. Pentru calculator, "hello world" și\n"Hello, World!" sunt două lucruri diferite.',
        'exemplu': 'def saluta_pe_cineva():\n    # funcția trimite înapoi un șir de caractere\n    return "Salut!"\n\nmesaj = saluta_pe_cineva()  # apelăm funcția și păstrăm rezultatul\nprint(mesaj)                # abia acum textul apare pe ecran',
        'sarcina': 'Scrie funcția saluta(). Ea nu primește nimic la intrare. Trebuie să dea\nînapoi, cu return, șirul de caractere Hello, World! scris exact așa:\nH și W majuscule, virgulă și un spațiu după ea, semnul exclamării la\nfinal. Nu folosi print, pentru că verificarea se uită doar la valoarea\nreturnată.',
        'indicii': ['Corpul funcției poate avea un singur rând. Întrebarea nu este cum\nafișezi textul, ci cum îl trimiți înapoi celui care a chemat funcția.', 'Ai nevoie de cuvântul return, urmat de textul scris între ghilimele\nduble. Rândul trebuie indentat cu patru spații față de def.', 'Pe rândul de sub def saluta():, indentat cu patru spații, scrie\ncuvântul return, un spațiu, ghilimele duble, apoi textul cerut copiat\nliteră cu literă din enunț, apoi ghilimele duble de închidere. Atât.\nNu mai adăuga niciun print și niciun alt rând.'],
        'greseala': 'Cea mai frecventă greșeală este print("Hello, World!") în loc de\nreturn "Hello, World!". Pe ecran pare corect, dar funcția nu dă nimic\nînapoi, așa că verificarea pică. A doua greșeală este textul scris\naproximativ: hello world, Hello World! fără virgulă, sau un spațiu în\nplus la final. Copiază textul exact. Verifică și indentarea: rândul cu\nreturn trebuie să fie mai la dreapta decât def.',
        'teste': [((), 'Hello, World!')],
    },
    {
        'nr': 2,
        'functie': 'celsius_in_fahrenheit',
        'titlu': 'Variabile și tipuri de date',
        'teorie': 'O variabilă este o cutie cu nume în care păstrezi o valoare. Scrii\nnume = valoare, iar semnul egal nu înseamnă aici "este egal cu" din\nmatematică, ci "pune valoarea din dreapta în cutia din stânga". Poți\noricând să pui altceva în aceeași cutie; vechea valoare se pierde.\n\nNumele se scriu cu litere mici, fără spații și fără diacritice, iar\ncuvintele se leagă cu liniuță de jos: temperatura_apei. Alege nume care\nspun ce conțin. Peste două săptămâni, x nu îți mai spune nimic.\n\nFiecare valoare are un tip (type). Cele patru tipuri de bază sunt:\nint, numărul întreg, ca 7 sau -3; float, numărul cu parte zecimală, ca\n2.5 sau 36.6, scris mereu cu punct, nu cu virgulă; str, șirul de\ncaractere (string), adică text între ghilimele, ca "Ana"; bool,\nvaloarea logică, care poate fi doar True sau False, scrise exact așa,\ncu majusculă.\n\nTipul contează, fiindcă hotărăște ce poți face cu valoarea. 2 + 3 dă 5,\ndar "2" + "3" dă "23", pentru că la text semnul plus înseamnă lipire.\nUn număr și un text nu se pot aduna: Python oprește programul cu\neroare. Dacă ai un text care conține cifre, îl transformi cu int("7")\nsau cu float("7.5").\n\nUn detaliu care surprinde mulți începători: împărțirea cu / dă\nîntotdeauna un float, chiar și când se împarte exact. 10 / 2 nu dă 5,\nci 5.0. Deci orice formulă care conține o împărțire produce un număr cu\nzecimale, iar asta e normal, nu e o greșeală.\n\nPython află singur tipul unei valori, nu trebuie să îl anunți. Dacă\nvrei să îl vezi cu ochii tăi, folosește type(valoare).',
        'exemplu': 'varsta = 19          # int, număr întreg\npret = 12.5          # float, număr cu zecimale\nnume = "Ana"         # str, șir de caractere\neste_student = True  # bool, adevărat sau fals\n\njumatate = 5 / 2     # împărțirea / dă mereu float\nprint(jumatate)      # afișează 2.5\nprint(type(varsta))  # afișează <class \'int\'>',
        'sarcina': 'Scrie funcția celsius_in_fahrenheit(c). Ea primește un singur număr, c,\ncare este o temperatură în grade Celsius. Trebuie să calculeze\ntemperatura corespunzătoare în grade Fahrenheit după formula\nF = C * 9/5 + 32 și să returneze rezultatul. Nu rotunji și nu afișa\nnimic: doar returnează numărul obținut.',
        'indicii': ['Formula ți-e dată deja în enunț. Trebuie doar rescrisă în Python,\nfolosind c, adică numărul primit de funcție.', 'Înmulțirea se scrie cu *, împărțirea cu /, iar rezultatul întregului\ncalcul se trimite înapoi cu return. Atenție la ordinea operațiilor: se\nînmulțește și se împarte înainte de a se aduna.', 'Înmulțește c cu 9, împarte rezultatul la 5, adună 32 la ce a ieșit și\nreturnează valoarea finală. Poți scrie tot calculul pe același rând,\nimediat după return, sau poți pune mai întâi rezultatul într-o\nvariabilă, de exemplu f, și apoi să returnezi variabila. Nu rotunji și\nnu transforma în int.'],
        'greseala': 'Mulți scriu c * (9 / 5 + 32), cu parantezele puse greșit, și obțin cu\ntotul alt număr. Alții scriu zecimalele cu virgulă, ca 9,5, ceea ce în\nPython înseamnă două valori separate, nu un număr. A treia capcană:\nrezultatul are zecimale, de exemplu 0 grade Celsius dă 32.0, nu 32, și\nașa trebuie să rămână. Și, ca peste tot, print nu ține loc de return.',
        'teste': [((0,), 32.0), ((100,), 212.0), ((-40,), -40.0), ((37,), 98.6)],
    },
    {
        'nr': 3,
        'functie': 'cele_mai_mari_trei',
        'titlu': 'Liste',
        'teorie': 'O listă (list) este o colecție ordonată de valori, ținute într-o\nsingură variabilă. Gândește-te la un catalog: un singur obiect, dar\nînăuntru sunt mai multe nume, într-o ordine anume.\n\nScrii o listă între paranteze drepte, cu elementele separate prin\nvirgulă: note = [8, 10, 5, 9]. Lista poate fi și goală: []. Elementele\npot fi numere, texte sau altceva.\n\nFiecare element are o poziție, numită index. Numărătoarea începe de la\n0, nu de la 1. Deci note[0] este 8, iar note[1] este 10. Ultimul\nelement se poate lua și cu index negativ: note[-1] este 9. Dacă ceri un\nindex care nu există, programul se oprește cu eroare.\n\nFuncția len(note) îți spune câte elemente are lista. Fiindcă indexarea\nîncepe de la 0, ultimul index valid este len(note) - 1.\n\nAdaugi un element la sfârșit cu note.append(7). Observă forma: punct\ndupă numele listei, apoi numele operației. Lista se schimbă pe loc, nu\nprimești una nouă.\n\nPoți lua o bucată dintr-o listă, numită felie (slice), cu note[1:3]:\nde la indexul 1 până înainte de indexul 3. Dacă lipsește numărul din\nstânga, se pornește de la început; dacă lipsește cel din dreapta, se\nmerge până la sfârșit. Foarte util: o felie care cere mai multe\nelemente decât are lista nu dă eroare, ci returnează liniștită doar\ncâte există.\n\nPentru ordonare ai sorted(note), care returnează o listă nouă,\nordonată crescător, fără să strice originalul. Cu sorted(note,\nreverse=True) obții ordinea descrescătoare, de la mare la mic.',
        'exemplu': 'numere = [4, 9, 2]\nprint(numere[0])       # primul element: 4\nnumere.append(7)       # adăugăm 7 la sfârșit\nprint(len(numere))     # câte elemente sunt: 4\n\nordonate = sorted(numere, reverse=True)  # copie de la mare la mic\nprint(ordonate)        # [9, 7, 4, 2]\nprint(ordonate[:2])    # felie: primele două, adică [9, 7]',
        'sarcina': 'Scrie funcția cele_mai_mari_trei(numere). Ea primește o listă de\nnumere. Trebuie să returneze o listă nouă, care conține cele mai mari\ntrei numere din listă, așezate de la cel mai mare la cel mai mic. Dacă\nlista primită are mai puțin de trei elemente, returnează toate\nelementele ei, tot în ordine descrescătoare. Lista primită nu trebuie\nstricată.',
        'indicii': ['Nu trebuie să inventezi tu o metodă de ordonare. Python știe deja să\nordoneze o listă; tu trebuie doar să îi ceri ordinea potrivită și apoi\nsă păstrezi doar începutul.', 'Folosește sorted cu argumentul reverse=True, ca să obții o listă nouă\nde la mare la mic, apoi ia din ea doar primele elemente cu o felie.', 'Pasul unu: obține o listă nouă, ordonată de la mare la mic, cu\nsorted(numere, reverse=True), și pune-o într-o variabilă. Pasul doi:\ndin acea variabilă ia primele trei elemente cu o felie care merge de la\nînceput până la poziția 3. Pasul trei: returnează felia. Nu ai nevoie\nde niciun if pentru listele scurte: felia care cere mai mult decât\nexistă returnează pur și simplu tot ce există.'],
        'greseala': 'Greșeala clasică este return numere.sort(reverse=True). Metoda sort nu\nreturnează lista, ci None, și pe deasupra strică lista primită.\nFolosește sorted, care dă o listă nouă. A doua greșeală este teama de\nlistele scurte și scrierea unui if în plus: felia [:3] funcționează\ncorect și pe o listă cu un singur element. A treia: ordinea inversată,\ncrescătoare, fiindcă s-a uitat reverse=True.',
        'teste': [(([5, 1, 9, 3, 7],), [9, 7, 5]), (([2, 1],), [2, 1]), (([4, 4, 4, 4],), [4, 4, 4]), (([],), []), (([-5, -1, -9],), [-1, -5, -9])],
    },
    {
        'nr': 4,
        'functie': 'cat_si_rest',
        'titlu': 'Operatori de bază și tupluri',
        'teorie': 'Operatorii sunt semnele cu care faci calcule. Cei de bază sunt + pentru\nadunare, - pentru scădere, * pentru înmulțire și / pentru împărțire.\nOrdinea operațiilor e cea din matematică: înmulțirea și împărțirea se\nfac înaintea adunării și scăderii, iar parantezele rotunde schimbă\nordinea.\n\nMai sunt trei operatori pe care îi întâlnești des. ** înseamnă ridicare\nla putere: 2 ** 5 dă 32. // este împărțirea întreagă și dă doar câtul,\nfără zecimale: 17 // 5 dă 3. % se numește modulo și dă restul\nîmpărțirii: 17 % 5 dă 2.\n\nȚine minte diferența dintre / și //. Împărțirea obișnuită 17 / 5 dă\n3.4, un float. Împărțirea întreagă 17 // 5 dă 3, un int. E exact\nîmpărțirea cu rest din școala primară: 17 împărțit la 5 face 3 rest 2.\nAici // îți dă câtul 3, iar % îți dă restul 2. Verificarea e simplă:\ncâtul înmulțit cu împărțitorul, plus restul, dă numărul de la care ai\npornit.\n\nModulo e surprinzător de util. n % 2 este 0 când n e par și 1 când e\nimpar, iar un număr de secunde % 60 îți dă secundele rămase după\nminutele întregi.\n\nUn tuplu (tuple) este o grupare de mai multe valori într-una singură,\nscrisă între paranteze rotunde: (3, 2). Seamănă cu lista, dar nu poate\nfi modificat după ce a fost creat. Se folosește mai ales atunci când o\nfuncție trebuie să dea înapoi două lucruri deodată. Scrii\nreturn (cat, rest) sau, la fel de corect, return cat, rest: Python\nîmpachetează singur valorile într-un tuplu. Cine apelează funcția poate\ndespacheta rezultatul cu c, r = cat_si_rest(17, 5).',
        'exemplu': 'a = 17\nb = 5\nprint(a + b, a - b, a * b)  # 22 12 85\nprint(a / b)                # 3.4 -> împărțire obișnuită, float\nprint(a // b)               # 3 -> câtul împărțirii întregi\nprint(a % b)                # 2 -> restul împărțirii\nprint(2 ** 10)              # 1024 -> ridicare la putere\n\npereche = (a // b, a % b)   # un tuplu cu două valori\nprint(pereche)              # (3, 2)',
        'sarcina': 'Scrie funcția cat_si_rest(a, b). Ea primește două numere întregi.\nTrebuie să returneze un tuplu cu două valori: pe prima poziție câtul\nîmpărțirii întregi a lui a la b, iar pe a doua poziție restul acelei\nîmpărțiri. De exemplu, cat_si_rest(17, 5) trebuie să dea (3, 2).\nReturnează amândouă valorile dintr-un singur return.',
        'indicii': ['Ai nevoie de doi operatori diferiți, unul pentru cât și unul pentru\nrest, și de un mod de a trimite înapoi amândouă valorile deodată.', 'Câtul se obține cu //, iar restul cu %. Cele două valori se grupează\nîntr-un tuplu, adică se scriu una după alta, separate prin virgulă.', 'Calculează a // b și pune rezultatul într-o variabilă numită cat.\nCalculează a % b și pune rezultatul într-o variabilă numită rest. Apoi\nscrie un singur return, urmat de cele două variabile pe același rând,\nseparate prin virgulă: Python le împachetează singur într-un tuplu.\nOrdinea contează, întâi câtul și abia apoi restul.'],
        'greseala': 'Cea mai des întâlnită greșeală este / în loc de //: 17 / 5 dă 3.4, nu\n3, iar verificarea cere un număr întreg. A doua greșeală este scrierea\na două return-uri, unul sub altul, pentru cele două valori: al doilea\nnu se execută niciodată, pentru că funcția se oprește la primul return.\nPune ambele valori într-un singur return. A treia: returnarea unei\nliste, [cat, rest], în loc de un tuplu.',
        'teste': [((17, 5), (3, 2)), ((10, 2), (5, 0)), ((7, 3), (2, 1)), ((0, 4), (0, 0))],
    },
    {
        'nr': 5,
        'functie': 'fisa_student',
        'titlu': 'Formatarea textului',
        'teorie': 'Până acum ai lucrat cu texte fixe. De cele mai multe ori însă ai nevoie\nde un text în care unele bucăți se schimbă: numele studentului, nota,\ndata. Construirea unui astfel de text se numește formatare.\n\nSe poate face și prin lipire cu plus, dar iese greoi și, pe deasupra,\nun număr nu se poate lipi de un text fără să îl transformi mai întâi.\nSoluția modernă în Python se numește f-string. Pui litera f imediat\nînainte de ghilimeaua de deschidere, iar apoi, oriunde în text, scrii\nîntre acolade numele unei variabile. Python înlocuiește acolada cu\nvaloarea acelei variabile.\n\nExemplu: dacă nume are valoarea "Ana", atunci f"Bună, {nume}!" produce\ntextul Bună, Ana!. Între acolade poți pune și un calcul mic, de pildă\n{a + b}. Fără litera f din față, acoladele rămân simple caractere în\ntext; este greșeala cea mai des întâlnită aici.\n\nAl doilea lucru util este controlul felului în care arată un număr.\nDupă numele variabilei pui două puncte și o specificație de format. Cea\nmai folosită este .2f, care înseamnă: scrie ca număr zecimal, cu exact\ndouă zecimale. Deci f"{media:.2f}" transformă 8.5 în 8.50, iar 9.376 în\n9.38, cu rotunjire. Fără .2f ai fi obținut 8.5, ceea ce într-un raport\narată neîngrijit.\n\nRestul textului dintre ghilimele se copiază exact cum îl scrii, literă\ncu literă. Spațiile, cratimele și parantezele fac și ele parte din\nrezultat. De aceea, când ți se cere un format exact, compară modelul cu\nce produci tu caracter cu caracter.',
        'exemplu': 'nume = "Ana"\nnota = 9.3\n\n# litera f dinainte de ghilimele activează înlocuirea acoladelor\nprint(f"Studenta {nume} are nota {nota}")\n\n# :.2f scrie numărul cu exact două zecimale\nprint(f"Media: {nota:.2f}")  # Media: 9.30\npret = 7\nprint(f"{pret:.2f} lei")     # 7.00 lei',
        'sarcina': 'Scrie funcția fisa_student(nume, grupa, media). Ea primește numele\nstudentului ca text, grupa ca text și media ca număr. Trebuie să\nreturneze un singur șir de caractere de forma exactă:\nPopescu Ion (SI-266) - media 8.50. Grupa stă în paranteze rotunde, apoi\nurmează spațiu, cratimă, spațiu, cuvântul media și valoarea scrisă cu\nexact două zecimale.',
        'indicii': ['Rezultatul este un singur șir de caractere. Uită-te atent la model și\nsepară ce este text fix, mereu la fel, de ce vine din cei trei\nparametri ai funcției.', 'Folosește un f-string: litera f înainte de ghilimele, iar cei trei\nparametri puși între acolade, la locul lor. La media adaugă și\nspecificația de format pentru două zecimale.', 'Scrie return, apoi litera f lipită de ghilimele. Înăuntru pui, în\nordine: acolade cu nume, un spațiu, paranteză rotundă deschisă, acolade\ncu grupa, paranteză rotundă închisă, un spațiu, o cratimă, un spațiu,\ncuvântul media, un spațiu, și acolade în care scrii media urmată de\ndouă puncte și .2f. Închide ghilimelele. Fără spații în plus la început\nsau la sfârșit.'],
        'greseala': 'Prima greșeală este uitarea literei f: atunci rezultatul conține\nacoladele ca atare, de exemplu {nume}, în loc de valoare. A doua este\nlipsa lui :.2f, care dă media 8.5 în loc de 8.50, sau 8 în loc de 8.00.\nA treia sunt spațiile: cratima are un spațiu de o parte și de alta, iar\nîntre nume și paranteză este exact un spațiu. Compară rezultatul tău cu\nmodelul caracter cu caracter.',
        'teste': [(('Popescu Ion', 'SI-266', 8.5), 'Popescu Ion (SI-266) - media 8.50'), (('Ana Pop', 'SI-265', 10), 'Ana Pop (SI-265) - media 10.00'), (('Ion Rusu', 'SI-266', 7.333), 'Ion Rusu (SI-266) - media 7.33')],
    },
    {
        'nr': 6,
        'functie': 'initiale',
        'titlu': 'Operații cu text',
        'teorie': 'Un șir de caractere (string) este text: o succesiune de litere, cifre\nși spații, scrisă între ghilimele. Gândește-te la el ca la un colier\nde mărgele: fiecare mărgea este un caracter, iar poziția ei contează.\n\nPoziția se numește indice și începe de la 0, nu de la 1. Dacă ai\ncuvant = "Ion", atunci cuvant[0] este "I", cuvant[1] este "o", iar\ncuvant[2] este "n". Primul caracter are întotdeauna indicele 0.\n\nPeste șiruri poți aplica metode, adică operații gata scrise în Python.\nLe apelezi punând un punct după șir:\n- strip() taie spațiile de la început și de la sfârșit; "  ana  "\n  devine "ana", iar spațiile dintre cuvinte rămân neatinse.\n- upper() transformă totul în majuscule, lower() în litere mici.\n- split() rupe textul în bucăți acolo unde întâlnește spații și îți\n  dă o listă de cuvinte: "popescu ion" devine ["popescu", "ion"].\n- "-".join(lista) face drumul invers: lipește elementele unei liste\n  într-un singur șir, punând între ele textul dinaintea punctului.\n\nFoarte important: metodele nu modifică șirul original. Șirurile sunt\nimuabile (immutable, adică nu pot fi schimbate), deci nume.upper() nu\nschimbă variabila nume, ci produce un șir nou. Dacă vrei să păstrezi\nrezultatul, pune-l într-o variabilă: nume_mare = nume.upper().\n\nMetodele se pot înlănțui, fiindcă fiecare întoarce un șir nou: poți\nscrie text.strip().lower().split(), iar execuția merge de la stânga\nla dreapta. Iar un caracter scos dintr-un cuvânt este tot un șir, deci\nși pe el poți aplica upper(): cuvinte[0][0].upper().',
        'exemplu': 'text = "   Maria Ionescu  "\ncurat = text.strip()          # taie spațiile de la capete\ncuvinte = curat.split()       # [\'Maria\', \'Ionescu\']\nprint(cuvinte[0][0])          # M, primul caracter din primul cuvânt\nprint(curat.upper())          # MARIA IONESCU\nprint("-".join(cuvinte))      # Maria-Ionescu',
        'sarcina': 'Scrie funcția initiale(nume_complet). Ea primește un nume scris ca\ntext, de exemplu "popescu ion", și trebuie să returneze inițialele cu\nmajuscule, fiecare urmată de punct: "P.I.".\nNumele poate avea două, trei sau mai multe cuvinte și poate avea\nspații în plus la început sau la final, deci curăță-l mai întâi.\nFuncția returnează un șir de caractere; nu îl afișa cu print.',
        'indicii': ['Gândește problema în doi pași: întâi desparte numele în cuvinte, apoi\nia câte ceva din fiecare cuvânt. Ce metodă îți dă lista cuvintelor?', 'Ai nevoie de strip() pentru spațiile în plus, de split() pentru lista\nde cuvinte, de indicele [0] ca să iei prima literă a unui cuvânt și de\nupper() ca litera să fie majusculă. Rezultatul îl poți aduna bucată cu\nbucată într-un șir, folosind operatorul +.', 'Pornește de la un șir gol, de exemplu rezultat = "". Curăță numele cu\nstrip() și desparte-l cu split(); obții o listă de cuvinte. Parcurge\nlista cuvânt cu cuvânt, cu un ciclu for. La fiecare cuvânt ia\ncaracterul de la poziția 0, transformă-l în majusculă și adaugă-l la\nrezultat, imediat urmat de un punct. După ce ciclul s-a terminat, în\nafara lui, returnează rezultatul. Punctul de la final apare de la sine,\nfiindcă îl pui după fiecare inițială.'],
        'greseala': 'Cea mai frecventă greșeală este să crezi că nume.upper() schimbă\nvariabila nume. Nu o schimbă: metoda întoarce un șir nou, iar dacă nu\nîl salvezi sau nu îl returnezi, se pierde.\nA doua greșeală este despărțirea cu split(" ") în loc de split(). Dacă\nîntre cuvinte se strecoară două spații, prima variantă produce cuvinte\ngoale, iar [0] pe un cuvânt gol oprește programul cu eroare. Folosește\nsplit() fără argument: el sare peste orice spații în plus.',
        'teste': [(('popescu ion',), 'P.I.'), (('  Ana Maria Pop ',), 'A.M.P.'), (('Ion',), 'I.'), (('vasile alecsandri',), 'V.A.')],
    },
    {
        'nr': 7,
        'functie': 'calificativ',
        'titlu': 'Instrucțiuni condiționale',
        'teorie': 'Un program care merge mereu pe același drum nu este prea util.\nInstrucțiunea if (dacă) îi dă programului puterea de a alege: verifică\no condiție și execută un bloc de cod doar atunci când condiția este\nadevărată. Este exact ca regula "dacă plouă, iau umbrela".\n\nO condiție este o expresie cu doar două rezultate posibile: True\n(adevărat) sau False (fals). O obții cu operatori de comparație:\n== înseamnă egal (atenție, cu două semne egal; unul singur atribuie o\nvaloare), != diferit, < mai mic, > mai mare, <= mai mic sau egal,\n>= mai mare sau egal.\n\nStructura completă este if, apoi oricâte elif (prescurtare de la\nelse if, adică altfel dacă), apoi cel mult un else (altfel). Python\nverifică condițiile de sus în jos și se oprește la prima care este\nadevărată; restul nici nu mai sunt citite. Ramura else prinde tot ce a\nrămas.\n\nDupă condiție pui obligatoriu două puncte, iar liniile dinăuntru se\nscriu mai la dreapta, de obicei cu patru spații. Această deplasare,\nnumită indentare, este modul în care Python înțelege ce aparține\nblocului; fără ea, programul dă eroare.\n\nCondițiile se pot combina: and (și) cere ca ambele să fie adevărate,\nor (sau) cere măcar una, not (nu) inversează rezultatul. Pentru\nintervale, Python acceptă și scrierea firească 5 <= nota <= 6.\n\nOrdinea contează enorm. Dacă întrebi întâi dacă nota este mai mare sau\negală cu 5, atunci și un 10 intră pe acea ramură și nu mai ajunge\nniciodată la ramura pentru excelent. Regula practică: pune întâi\ncondițiile cele mai restrânse și lasă la urmă pe cele largi.',
        'exemplu': 'varsta = 20\nif varsta < 18:\n    categorie = "minor"      # prima condiție adevărată câștigă\nelif varsta < 65:\n    categorie = "adult"      # aici ajunge doar dacă nu e minor\nelse:\n    categorie = "pensionar"\nprint(categorie)             # adult',
        'sarcina': 'Scrie funcția calificativ(nota). Ea primește un număr de la 1 la 10 și\ntrebuie să returneze un text, în funcție de valoare:\n"excelent" pentru 9 sau 10, "bine" pentru 7 sau 8, "satisfacator"\npentru 5 sau 6 și "nepromovat" pentru orice notă mai mică de 5.\nScrie textele exact așa cum sunt date aici, cu litere mici și fără\ndiacritice, altfel verificarea nu le recunoaște. Funcția returnează\ntextul, nu îl afișează.',
        'indicii': ['Ai patru situații diferite, deci ai nevoie de patru ramuri.\nÎntreabă-te în ce ordine le verifici, ca să nu se calce una pe alta.', 'Folosește if, apoi două elif și la final else. Fiecare ramură are\npropriul return. Poți testa fie cu un singur prag (nota >= 9), fie cu\nun interval (7 <= nota <= 8), fie cu or (nota == 9 or nota == 10);\ntoate trei sunt corecte, alege varianta pe care o înțelegi cel mai\nbine.', 'Verifică întâi dacă nota este mai mare sau egală cu 9 și, dacă da,\nreturnează imediat "excelent". Dacă nu, verifică pe o ramură elif dacă\neste mai mare sau egală cu 7 și returnează "bine". Apoi, tot pe elif,\ndacă este mai mare sau egală cu 5, returnează "satisfacator". Pentru\ntot ce a rămas, pe ramura else, returnează "nepromovat".\nFiindcă Python merge de sus în jos, când ajungi la a doua verificare\nștii deja sigur că nota este sub 9, deci nu mai ai nevoie de condiții\ndublă.'],
        'greseala': 'Două greșeli clasice. Prima este ordinea inversă: dacă începi cu\nif nota >= 5, absolut orice notă de trecere primește "satisfacator",\nfiindcă prima condiție adevărată câștigă și restul nu se mai citesc.\nÎncepe cu pragul cel mai mare.\nA doua este confuzia dintre = și ==. Un singur semn egal atribuie o\nvaloare și dă eroare de sintaxă într-o condiție; comparația se scrie\nmereu cu două semne egal. Și nu uita cele două puncte la finalul\nfiecărei linii cu if, elif sau else.',
        'teste': [((10,), 'excelent'), ((9,), 'excelent'), ((8,), 'bine'), ((7,), 'bine'), ((6,), 'satisfacator'), ((5,), 'satisfacator'), ((4,), 'nepromovat'), ((1,), 'nepromovat')],
    },
    {
        'nr': 8,
        'functie': 'fizzbuzz',
        'titlu': 'Cicluri',
        'teorie': 'Când vrei să repeți o acțiune de mai multe ori, nu copiezi codul de\nzece ori: folosești un ciclu (loop, adică buclă). Este ca rețeta care\nspune "amestecă de 20 de ori": o singură instrucțiune, executată\nrepetat.\n\nCiclul for parcurge, pe rând, elementele unei colecții. Scrii\nfor element in colectie: iar la fiecare rotire variabila element ia\nvaloarea următoare. Colecția poate fi o listă, un șir de caractere sau\nun interval de numere.\n\nIntervalele se fac cu range. range(5) dă numerele 0, 1, 2, 3, 4:\nîncepe de la 0 și se oprește înainte de 5. Dacă ai nevoie de numerele\nde la 1 la n, scrii range(1, n + 1); primul număr este inclus, al\ndoilea niciodată.\n\nCiclul while (cât timp) repetă atâta timp cât o condiție rămâne\nadevărată. Îl folosești când nu știi dinainte câte repetări sunt\nnecesare. Ai grijă ca ceva să se schimbe în interior, altfel condiția\nrămâne adevărată la nesfârșit și programul se blochează.\n\nCa să construiești o listă într-un ciclu, procedezi mereu la fel:\ncreezi o listă goală înainte de ciclu, apoi la fiecare pas adaugi în ea\nun element cu metoda append (adaugă la final). Când ciclul se termină,\nlista conține tot. Dacă declari lista goală din greșeală în interiorul\nciclului, ea se golește la fiecare pas și rămâi cu un singur element.\n\nUn detaliu de care ai nevoie acum: operatorul % (modulo) dă restul\nîmpărțirii. 9 % 3 este 0, deci 9 se împarte exact la 3. Testul "se\nîmparte exact" se scrie întotdeauna numar % divizor == 0.',
        'exemplu': 'rezultat = []                     # lista goală, ÎNAINTE de ciclu\nfor i in range(1, 6):             # i ia valorile 1, 2, 3, 4, 5\n    if i % 2 == 0:\n        rezultat.append("par")\n    else:\n        rezultat.append(str(i))   # str transformă numărul în text\nprint(rezultat)                   # [\'1\', \'par\', \'3\', \'par\', \'5\']',
        'sarcina': 'Scrie funcția fizzbuzz(n). Ea trebuie să returneze o listă cu n\nelemente, câte unul pentru fiecare număr de la 1 la n.\nPentru numerele care se împart și la 3 și la 5 pui textul "FizzBuzz",\npentru cele care se împart doar la 3 pui "Fizz", pentru cele care se\nîmpart doar la 5 pui "Buzz", iar pentru restul pui chiar numărul,\ntransformat în text.\nPentru n = 5 rezultatul este ["1", "2", "Fizz", "4", "Buzz"].\nReturnezi lista întreagă, nu afișezi nimic.',
        'indicii': ['La fiecare număr adaugi exact un element în listă. Deci ai nevoie de o\nlistă goală înainte de ciclu și de un ciclu care trece prin numerele\nde la 1 până la n.', 'Folosește for împreună cu range(1, n + 1), metoda append ca să pui\nelemente în listă și operatorul % ca să verifici divizibilitatea.\nNumărul îl transformi în text cu str(numar). Pentru cele patru cazuri\nai nevoie de if, elif, elif și else.', 'Creează o listă goală. Parcurge cu for numerele de la 1 la n inclusiv.\nPentru fiecare număr verifică, exact în această ordine: dacă restul\nîmpărțirii la 3 și restul împărțirii la 5 sunt amândouă 0, adaugă\n"FizzBuzz"; altfel, dacă doar restul la 3 este 0, adaugă "Fizz";\naltfel, dacă doar restul la 5 este 0, adaugă "Buzz"; altfel adaugă\nnumărul convertit în text.\nDupă ce ciclul s-a terminat, în afara lui, returnează lista.'],
        'greseala': 'Cel mai des, condiția pentru "FizzBuzz" este pusă ultima. Atunci\nnumărul 15 intră pe ramura "Fizz" și nu mai ajunge niciodată la\n"FizzBuzz". Verifică întâi cazul dublu.\nA doua greșeală este return scris înăuntrul ciclului, la aceeași\nindentare cu append: funcția se oprește după primul pas și întoarce o\nlistă cu un singur element. Scrie return lipit de marginea funcției,\nîn afara ciclului.\nȘi nu uita str(numar): lista trebuie să conțină text, nu numere, iar\n"4" nu este același lucru cu 4.',
        'teste': [((5,), ['1', '2', 'Fizz', '4', 'Buzz']), ((3,), ['1', '2', 'Fizz']), ((15,), ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']), ((1,), ['1'])],
    },
    {
        'nr': 9,
        'functie': 'pret_final',
        'titlu': 'Funcții proprii',
        'teorie': 'Până acum ai folosit funcții gata făcute, ca len sau round. Acum le\nscrii tu. O funcție este o mașinărie mică: îi dai ceva la intrare, face\no treabă și îți întoarce un rezultat. Odată scrisă, o poți folosi de o\nmie de ori, din locuri diferite, fără să rescrii codul; iar dacă\ndescoperi o greșeală, o repari într-un singur loc.\n\nO definești cu cuvântul def, urmat de nume, paranteze și două puncte.\nNumele dintre paranteze se numesc parametri: sunt variabile goale, care\nprimesc valori abia la apelare. Valorile concrete pe care le trimiți\ncând chemi funcția se numesc argumente. Tot ce ține de funcție se scrie\nindentat, mai la dreapta.\n\nUn parametru poate avea o valoare implicită, scrisă cu semnul egal în\nantet: def pret_final(pret, reducere=0). Dacă la apelare nu dai al\ndoilea argument, Python folosește automat 0. Parametrii cu valoare\nimplicită se scriu întotdeauna după cei fără.\n\nCuvântul return încheie funcția și trimite rezultatul înapoi celui care\na apelat-o. Aici este capcana clasică: print doar desenează ceva pe\necran, pentru ochii omului, și nu întoarce nimic folositor. return\npredă valoarea programului, ca să poată fi salvată într-o variabilă sau\nfolosită mai departe. O funcție care afișează în loc să returneze pare\ncorectă când o rulezi, dar întoarce None (nimic), iar orice verificare\nautomată o respinge. Când execuția întâlnește return, funcția se oprește\npe loc; liniile de după nu se mai execută.\n\nÎți mai trebuie round(valoare, 2), care rotunjește la două zecimale, și\nregula că un procent devine sumă dacă înmulțești și împarți la 100.',
        'exemplu': 'def salut(nume, politicos=True):\n    if politicos:\n        return "Buna ziua, " + nume + "!"   # valoarea pleacă înapoi\n    return "Salut, " + nume + "!"\n\nmesaj = salut("Ana")            # folosește valoarea implicită True\nprint(mesaj)                    # Buna ziua, Ana!\nprint(salut("Ana", False))      # Salut, Ana!',
        'sarcina': 'Scrie funcția pret_final(pret, reducere=0). Ea primește un preț și un\nprocent de reducere. Al doilea parametru este opțional: dacă nu îl dai\nla apelare, valoarea lui este 0, adică fără reducere.\nFuncția returnează prețul care rămâne după ce scazi reducerea,\nrotunjit la două zecimale cu round.\nDe exemplu, pret_final(200, 25) întoarce 150.0, iar pret_final(80)\nîntoarce 80.0.',
        'indicii': ['Reducerea este un procent, nu o sumă de bani. Întreabă-te mai întâi\ncâți lei înseamnă acel procent din prețul primit.', 'Îți ajung o linie de calcul și un return. Un procent se transformă în\nsumă înmulțind prețul cu procentul și împărțind la 100. Rotunjirea se\nface cu round(valoare, 2). Pentru valoarea implicită 0 nu trebuie să\nfaci nimic special: ea este deja scrisă în antetul funcției.', 'Calculează suma reducerii: prețul înmulțit cu reducere, apoi împărțit\nla 100. Scade această sumă din preț și obții prețul final. Trece\nrezultatul prin round, cu al doilea argument 2, și returnează-l.\nPoți face totul într-o singură instrucțiune return sau poți folosi\nîntâi o variabilă intermediară; ambele variante sunt corecte.\nNu trebuie să tratezi separat cazul în care reducerea lipsește:\natunci ea este 0, iar scăderea lui 0 nu schimbă nimic.'],
        'greseala': 'Greșeala numărul unu rămâne print în loc de return: pe ecran apare\n150.0, totul pare corect, dar funcția întoarce None și verificarea\npică. Reține: print este pentru om, return este pentru program.\nA doua greșeală este uitarea împărțirii la 100: scazi 25 din 200 și\nobții 175 în loc de 150.\nA treia este round(valoare) fără al doilea argument, care rotunjește\npână la număr întreg. Scrie round(valoare, 2).',
        'teste': [((200, 25), 150.0), ((100,), 100.0), ((99.99, 10), 89.99), ((50, 100), 0.0)],
    },
    {
        'nr': 10,
        'functie': 'Student',
        'titlu': 'Clase și obiecte',
        'teorie': 'Până acum ai folosit tipuri de date gata făcute: numere, șiruri, liste.\nO clasă (class) îți dă voie să construiești tu un tip de date nou,\npotrivit problemei tale.\n\nAnalogie: clasa este planul de arhitectură al unei case, iar obiectul\neste casa construită după acel plan. Dintr-un singur plan se ridică zeci\nde case: toate au aceeași structură, dar fiecare are alt proprietar și\nalte lucruri înăuntru. La fel, dintr-o clasă Student poți crea oricâți\nstudenți, fiecare cu numele lui și cu notele lui.\n\nÎntr-o clasă scrii două feluri de lucruri:\n- atribute: datele pe care le are obiectul (numele, grupa, notele);\n- metode: funcțiile care știu să lucreze cu acele date (adaugă o notă,\n  calculează media).\n\nMetoda specială __init__ se numește constructor. Ea se execută automat\nîn clipa în care creezi obiectul și are rolul de a pregăti atributele de\nstart. Când scrii s = Student("Ana", "SI-265"), Python cheamă singur\n__init__ și îi trimite cele două valori.\n\nself este obiectul curent, cel asupra căruia lucrezi chiar acum. Este\nprimul parametru al oricărei metode, dar nu îl dai tu la apelare, îl\ntrimite Python. Tot ce salvezi cu self.ceva rămâne în obiect și poate fi\nfolosit mai târziu de altă metodă. Dacă uiți self, valoarea dispare în\nclipa în care metoda se termină.\n\nDiferența practică: s.nume este un atribut, adică o valoare, un\nsubstantiv; s.media() este o metodă, adică o acțiune, un verb, și se\napelează cu paranteze.\n\nRegula rămâne aceeași și aici: o metodă care calculează ceva returnează\nrezultatul cu return, nu îl afișează cu print.',
        'exemplu': 'class Masina:\n    def __init__(self, marca):\n        self.marca = marca      # atribut: ce are obiectul\n        self.km = 0             # pornim de la zero kilometri\n    def merge(self, distanta):  # metodă: ce știe să facă\n        self.km = self.km + distanta\n\na = Masina("Dacia")             # creăm un obiect din clasă\na.merge(120)\nprint(a.marca, a.km)            # Dacia 120',
        'sarcina': 'Completează clasa Student. În __init__ primești numele și grupa și le\nreții în obiect, iar pe lângă ele pregătești o listă goală de note.\nMetoda adauga_nota(nota) pune nota primită în acea listă și nu\nreturnează nimic. Metoda media() returnează media notelor, rotunjită la\ndouă zecimale; dacă studentul nu are nicio notă, returnează 0.',
        'indicii': ['Gândește-te ce trebuie să țină minte obiectul între două apeluri: sunt\ntrei lucruri. Toate trei se pregătesc în __init__ și toate trei se\nlipesc de self.', 'În __init__ ai nevoie de self.nume, self.grupa și self.note = [].\nÎn adauga_nota folosește metoda append a listei. Pentru numărul de note\nfolosește len, iar pentru rotunjire funcția round(valoare, 2).', 'În __init__: salvează cei doi parametri în self și pune self.note\negal cu o listă goală. În adauga_nota: apelează self.note.append(nota),\nfără return. În media: verifică întâi dacă len(self.note) este 0 și în\nacest caz returnează 0. Altfel adună toate notele (cu sum sau cu un for\nși un contor), împarte suma la numărul de note și returnează rezultatul\ntrecut prin round cu două zecimale.'],
        'greseala': 'Cea mai frecventă greșeală este să scrii note = [] în loc de\nself.note = []. Fără self, lista este o simplă variabilă locală, care\ndispare când se termină __init__, iar la primul adauga_nota primești\neroarea AttributeError. A doua greșeală: împărțirea la zero, când\nstudentul nu are nicio notă; de aceea se verifică lista goală înainte de\ncalcul. A treia: media afișată cu print în loc de returnată cu return.',
        'verificator': _verif_student,
    },
    {
        'nr': 11,
        'functie': 'frecventa_litere',
        'titlu': 'Dicționare',
        'teorie': 'Lista ține valorile la rând și le găsești după poziție: note[0], note[1].\nDicționarul (dictionary) ține perechi cheie-valoare (key-value) și\ngăsești valoarea după cheie, nu după poziție.\n\nAnalogie: un catalog de note. Nu cauți nota după al câtelea rând este,\nci după numele studentului. Numele este cheia, nota este valoarea.\n\nUn dicționar se scrie cu acolade:\npreturi = {"paine": 12, "lapte": 18}\n\nCe poți face cu el:\n- citești o valoare: preturi["lapte"];\n- adaugi sau modifici: preturi["cafea"] = 45, iar dacă cheia nu există\n  se creează, dacă există valoarea veche se înlocuiește;\n- verifici dacă o cheie există: "ceai" in preturi;\n- îl parcurgi cu for: for cheie in preturi, iar preturi[cheie] îți dă\n  valoarea corespunzătoare.\n\nAtenție la o capcană: dacă ceri preturi["ceai"] și cheia nu există,\nprogramul se oprește cu eroarea KeyError. Soluția curată este metoda\nget, care primește și o valoare implicită: preturi.get("ceai", 0)\nreturnează 0 în loc să dea eroare. Exact asta folosești când numeri\nlucruri. Rândul\n  contor[c] = contor.get(c, 0) + 1\nînseamnă, în cuvinte: ia câte am până acum pentru c, sau zero dacă nu am\ndeloc, și mai adaugă unu.\n\nCheile trebuie să fie unice și de un tip fix, de obicei șir sau număr.\nValorile pot fi orice: numere, șiruri, liste, chiar alte dicționare.\n\nCând alegi între listă și dicționar, întreabă-te: am nevoie de o ordine\nși de poziții, sau de o etichetă după care caut? Căutarea după cheie\nrămâne foarte rapidă oricât de mare ar fi dicționarul.',
        'exemplu': 'preturi = {"paine": 12, "lapte": 18}  # perechi cheie: valoare\npreturi["cafea"] = 45                 # adăugăm o pereche nouă\nprint(preturi["lapte"])               # 18\nprint(preturi.get("ceai", 0))         # 0, cheia nu există\n\nfor cheie in preturi:                 # parcurgem cheile\n    print(cheie, preturi[cheie])      # paine 12, lapte 18, cafea 45',
        'sarcina': 'Scrie funcția frecventa_litere(text), care primește un șir de caractere\nși returnează un dicționar. Fiecare cheie este o literă scrisă cu literă\nmică, iar valoarea este de câte ori apare acea literă în text. Se numără\ndoar literele: spațiile, cifrele și semnele de punctuație se ignoră.\nDe exemplu, frecventa_litere("Ana are") dă {"a": 3, "n": 1, "r": 1,\n"e": 1}. Rezultatul se returnează, nu se afișează.',
        'indicii': ['Pornește de la un dicționar gol și parcurge textul caracter cu caracter.\nScrii for c in text și primești pe rând fiecare caracter, inclusiv\nspațiile, pe care va trebui să le lași deoparte.', 'Ca să păstrezi doar literele folosește metoda isalpha() a caracterului,\ncare răspunde cu True sau False. Ca să nu numeri separat A și a,\ntransformă caracterul cu lower(). Numărarea se face cel mai simplu cu\nget, cu valoarea implicită 0.', 'Algoritmul pas cu pas: creează rezultat, un dicționar gol. Parcurge\ntextul caracter cu caracter. Pentru fiecare caracter verifică dacă este\nliteră; dacă nu este, treci la următorul. Dacă este, transformă-l în\nliteră mică și pune-l într-o variabilă. Apoi scrie în dicționar valoarea\nveche a acelei chei, luată cu get și valoarea implicită 0, la care\nadaugi unu. După ce s-a terminat parcurgerea, returnează dicționarul.'],
        'greseala': 'Două greșeli apar aproape mereu. Prima: se uită verificarea cu isalpha\nși atunci în rezultat ajung și spațiile sau virgulele, ca și cum ar fi\nlitere. A doua: se scrie rezultat[c] = rezultat[c] + 1 pentru o cheie\ncare încă nu există, iar programul se oprește cu KeyError; folosește get\ncu valoarea implicită 0 sau verifică întâi dacă c este în dicționar.\nA treia, mai discretă: se uită lower() și atunci A și a ajung două chei\ndiferite.',
        'teste': [(('Ana are',), {'a': 3, 'n': 1, 'r': 1, 'e': 1}), (('',), {}), (('A1 b!',), {'a': 1, 'b': 1}), (('aaa',), {'a': 3})],
    },
    {
        'nr': 12,
        'functie': 'zile_intre',
        'titlu': 'Module și pachete',
        'teorie': 'Un modul (module) este un fișier cu cod Python scris de altcineva, pe\ncare îl poți folosi în programul tău. Un pachet (package) este un grup\nde module strânse la un loc.\n\nAnalogie: nu îți făurești singur cheia atunci când trebuie să schimbi o\nroată. Iei o cheie gata făcută din trusă. Modulele sunt trusa de scule a\nlimbajului: cod deja scris, verificat de mii de oameni și, aproape\nsigur, mai corect decât ce ai scrie tu într-o seară.\n\nAi două feluri de a aduce un modul în programul tău:\n  import math          apoi scrii math.sqrt(81)\n  from math import sqrt    apoi scrii direct sqrt(81)\nAmândouă sunt corecte. Prima variantă este mai clară, pentru că se vede\ndin ce modul vine funcția. Importurile se pun la începutul fișierului.\n\nPython vine cu o bibliotecă standard mare, deja instalată pe calculator:\nmath are rădăcini, puteri, numărul pi și rotunjiri;\nrandom dă numere la întâmplare și alege elemente dintr-o listă;\ndatetime lucrează cu date calendaristice și ore.\n\nDin datetime îți trebuie acum două lucruri. Întâi, datetime.strptime\ntransformă un șir de text într-o dată adevărată, dacă îi spui formatul:\n"%Y-%m-%d" înseamnă an din patru cifre, lună, zi. Apoi, scăderea a două\ndate îți dă un obiect de tip timedelta, iar din el atributul days este\nnumărul de zile dintre ele.\n\nDe ce nu rescriem ce există deja? Pentru că anii bisecți, lunile de 30\nsau 31 de zile și trecerea dintr-un an în altul sunt rezolvate corect\nacolo. Codul tău rămâne scurt, se citește ușor și are mult mai puține\nșanse să greșească.',
        'exemplu': 'import math\nfrom datetime import datetime\n\nprint(math.sqrt(81))              # 9.0\nd1 = datetime.strptime("2026-09-22", "%Y-%m-%d")\nd2 = datetime.strptime("2026-10-02", "%Y-%m-%d")\ndiferenta = d2 - d1               # obiect de tip timedelta\nprint(diferenta.days)             # 10',
        'sarcina': 'Scrie funcția zile_intre(data1, data2). Primești două date sub formă de\nșiruri de caractere, scrise în formatul "2026-09-22", adică an, lună, zi.\nFuncția returnează câte zile sunt între cele două date, ca număr întreg\nși întotdeauna pozitiv, indiferent care dată a fost dată prima. Trebuie\nsă folosești modulul datetime, nu să calculezi tu zilele.',
        'indicii': ['Nu încerca să numeri tu zilele lunilor. Transformă cele două șiruri în\ndate adevărate și lasă limbajul să le scadă una din alta.', 'Ai nevoie de from datetime import datetime și de\ndatetime.strptime(șir, "%Y-%m-%d"). Diferența dintre două date are\natributul days. Ca să scapi de semnul minus folosește funcția abs.', 'Algoritmul pas cu pas: importă datetime la începutul fișierului.\nTransformă data1 într-un obiect dată, cu strptime și formatul\n"%Y-%m-%d". Fă la fel cu data2. Scade cele două obiecte unul din altul\nși păstrează rezultatul într-o variabilă. Ia din el atributul days.\nTrece numărul prin abs, ca să fie pozitiv indiferent de ordinea datelor.\nReturnează acest număr.'],
        'greseala': 'Greșeala cea mai deasă este să returnezi întreg rezultatul scăderii, adică\nobiectul timedelta, care arată așa: 10 days, 0:00:00. Ție îți trebuie\nnumai numărul, deci atributul days. A doua greșeală este uitarea lui abs:\ndacă prima dată este mai mare decât a doua, primești un număr negativ.\nȘi a treia: încercarea de a scădea direct șirurile de caractere sau de a\nînmulți anii cu 365, ceea ce dă un rezultat greșit la ani bisecți.',
        'teste': [(('2026-09-22', '2026-09-25'), 3), (('2026-09-25', '2026-09-22'), 3), (('2026-01-01', '2026-12-31'), 364), (('2026-03-01', '2026-03-01'), 0)],
    },
    {
        'nr': 13,
        'functie': 'salveaza_si_incarca',
        'titlu': 'Lucrul cu fișiere',
        'teorie': 'Până acum tot ce calcula programul dispărea în clipa în care el se\nînchidea. Un fișier îți dă memorie de lungă durată: scrii azi, citești\nmâine.\n\nTotul începe cu funcția open, care primește calea fișierului și modul de\nlucru:\n"w" (write, scriere) deschide fișierul gol; dacă există deja, tot ce era\nîn el se pierde;\n"r" (read, citire) deschide fișierul doar pentru citit; dacă fișierul nu\nexistă, primești eroare;\n"a" (append, adăugare) scrie la sfârșit, fără să șteargă ce era.\n\nForma recomandată este cu with:\n  with open(cale, "w") as f:\n      f.write("text")\nTot ce scrii indentat sub with lucrează cu fișierul deschis. La ieșirea\ndin bloc, fișierul se închide automat, chiar dacă a apărut o eroare. De\nce contează: un fișier lăsat deschis poate rămâne cu datele nescrise pe\ndisc și ține resurse ocupate degeaba. Cu with nu ai cum să uiți să îl\nînchizi.\n\nSpre deosebire de print, f.write nu trece singur pe rândul următor. Dacă\nvrei un rând nou, pui tu \\n la sfârșitul textului: f.write("8\\n").\n\nLa citire ai două variante: f.readlines() îți dă o listă cu toate\nrândurile, sau parcurgi direct fișierul cu for rand in f.\n\nFoarte important: din fișier iese întotdeauna text, niciodată numere.\nUn rând citit arată așa: "8.5\\n". Ca să obții un număr, îl treci prin\nfloat(rand), care nu se supără de spații sau de trecerea la rând nou de\nla capete. Dacă vrei să cureți explicit rândul, folosește rand.strip().',
        'exemplu': 'with open("test.txt", "w") as f:   # "w" scrie de la zero\n    f.write("10\\n")                # \\n = trecere pe rând nou\n    f.write("7.5\\n")\n\nwith open("test.txt", "r") as f:   # "r" doar citește\n    randuri = f.readlines()\n\nprint(randuri[0])                  # 10 urmat de rând nou\nprint(float(randuri[1]))           # 7.5 ca număr',
        'sarcina': 'Scrie funcția salveaza_si_incarca(cale, note). Primești calea unui fișier\nși o listă de note (numere). Întâi scrii notele în fișier, câte una pe\nrând. Apoi deschizi același fișier, citești rândurile înapoi și\nreturnezi lista de note citite, transformate în numere de tip float.\nDe exemplu, salveaza_si_incarca("note.txt", [8, 9.5]) returnează\nlista [8.0, 9.5].',
        'indicii': ['Sunt două etape complet separate: întâi deschizi fișierul ca să scrii și\nîl închizi, abia apoi îl deschizi din nou ca să citești. Deci vei avea\ndouă blocuri with, unul după altul.', 'Pentru scriere: with open(cale, "w") as f, iar înăuntru un for peste\nlista de note și f.write(str(nota) + "\\n"). Pentru citire:\nwith open(cale, "r") as f și apoi f.readlines(). Transformarea din text\nîn număr se face cu float().', 'Algoritmul pas cu pas: deschide calea în modul "w". Pentru fiecare notă\ndin listă, scrie în fișier nota transformată în text, urmată de trecerea\nla rând nou. Ieși din bloc, fișierul se închide singur. Deschide aceeași\ncale în modul "r". Pregătește o listă goală pentru rezultat. Parcurge\nrândurile citite și, pentru fiecare rând care nu este gol după strip,\nadaugă în listă valoarea lui transformată cu float. La final returnează\nlista.'],
        'greseala': 'Prima greșeală: f.write(nota) direct cu un număr. Funcția write cere text,\ndeci primești TypeError; se rezolvă cu str(nota). A doua: uitarea lui \\n,\nși atunci toate notele se lipesc pe un singur rând și nu mai pot fi\ncitite separat. A treia: returnarea rândurilor așa cum au fost citite,\nadică "8\\n" în loc de 8.0, pentru că s-a uitat conversia cu float.\nȘi ultima: deschiderea fișierului în modul "w" a doua oară, la citire,\nceea ce șterge exact ce tocmai ai scris.',
        'verificator': _verif_fisier,
    },
]

SARCINI_BONUS = [
    {
        'nr': 1,
        'functie': 'patrate_pare',
        'titlu': 'Liste construite dintr-o singură expresie',
        'teorie': 'Ai scris deja multe cicluri care construiesc o listă. Tiparul se repetă\nmereu: pornești de la o listă goală, parcurgi ceva cu for și adaugi\nrezultatul cu append.\n\nrezultat = []\nfor x in range(1, 6):\n    rezultat.append(x * x)\n\nPython îți oferă o scurtătură exact pentru acest tipar, numită list\ncomprehension (listă construită dintr-o singură expresie). Aceleași trei\nrânduri se scriu așa:\n\nrezultat = [x * x for x in range(1, 6)]\n\nCitește de la stânga la dreapta: ia fiecare x din range(1, 6) și pune în\nlistă valoarea x * x. Partea dinaintea lui for spune ce pui, partea cu\nfor spune de unde iei.\n\nLa sfârșit poți adăuga un filtru cu if:\n\nrezultat = [x * x for x in range(1, 6) if x % 2 == 0]\n\nAcum intră în listă doar valorile care trec de condiție. Este exact\nechivalentul unui if pus în interiorul ciclului, înainte de append.\n\nDe ce merită? Pentru că spui intenția, nu mecanismul: nu mai citești\ntrei rânduri ca să înțelegi că se construiește o listă. Codul e mai\nscurt și mai greu de stricat, fiindcă nu ai ce uita, nici lista goală,\nnici append-ul.\n\nCând nu merită? Când ai nevoie de mai mulți pași, de condiții încâlcite\nsau de un try. Dacă o comprehension nu mai încape comod pe un rând,\nscrie un for obișnuit. Regula practică: o comprehension trebuie să se\ncitească dintr-o privire.',
        'exemplu': '# varianta clasica, cu ciclu for\ncuburi = []\nfor x in range(1, 5):\n    cuburi.append(x ** 3)\n# exact aceeasi lista, scrisa cu list comprehension\ncuburi2 = [x ** 3 for x in range(1, 5)]\n# comprehension cu filtru: pastreaza doar multiplii lui 3\nmici = [x for x in range(1, 11) if x % 3 == 0]\nprint(cuburi == cuburi2, mici)',
        'sarcina': 'Scrie funcția def patrate_pare(n): care returnează lista pătratelor\nnumerelor PARE de la 1 la n inclusiv. De exemplu, patrate_pare(6)\nreturnează [4, 16, 36]. Trebuie să rezolvi folosind o list\ncomprehension, nu un ciclu for clasic. Funcția dă lista înapoi cu\nreturn, nu o afișează cu print.',
        'indicii': ['Desparte problema în două întrebări: care numere te interesează, adică\ncele pare de la 1 la n, și ce pui în listă pentru fiecare dintre ele,\nadică pătratul lui.', 'Ai nevoie de o list comprehension peste range(1, n + 1), cu un filtru if\ncare păstrează doar numerele pare. Paritatea se verifică cu operatorul\nmodulo, %.', 'Pornești de la range(1, n + 1), ca să prinzi și numărul n. Pentru\nfiecare număr verifici dacă restul împărțirii la 2 este zero. Dacă da,\nîl ridici la pătrat, iar valoarea intră în listă. Totul se scrie într-o\nsingură pereche de paranteze pătrate: mai întâi expresia cu pătratul,\napoi partea cu for, apoi filtrul cu if. Lista obținută o dai înapoi cu\nreturn.'],
        'greseala': 'Cea mai frecventă greșeală este range(1, n), care lasă ultimul număr pe\ndinafară: patrate_pare(6) ar da [4, 16] în loc de [4, 16, 36]. Scrie\nrange(1, n + 1). A doua greșeală este ordinea: filtrul if se pune la\nsfârșit, după for, nu înaintea lui. Forma [x * x if x % 2 == 0 for x in\n...] este eroare de sintaxă.',
        'teste': [((6,), [4, 16, 36]), ((1,), []), ((10,), [4, 16, 36, 64, 100]), ((2,), [4])],
    },
    {
        'nr': 2,
        'functie': 'sorteaza_dupa_nota',
        'titlu': 'Funcții anonime cu lambda',
        'teorie': 'O funcție obișnuită are un nume și un corp scris cu def. Uneori însă ai\nnevoie de o funcție minusculă, folosită o singură dată, într-un singur\nloc. Să inventezi un nume pentru ea e muncă în plus. Pentru asta există\nlambda, adică o funcție anonimă (fără nume).\n\ndublu = lambda x: x * 2\n\nSe citește: primește x și întoarce x * 2. După lambda pui parametrii,\ndupă două puncte pui o singură expresie, iar valoarea ei este returnată\nautomat. Nu scrii return și nu ai voie cu mai multe instrucțiuni.\n\nUtilitatea reală apare când o funcție primește altă funcție ca argument.\nCel mai des: sorted. Ea are parametrul key (cheie), o funcție aplicată\nfiecărui element ca să obții criteriul după care se compară.\n\nperechi = [("Ana", 7), ("Bogdan", 9)]\nsorted(perechi, key=lambda p: p[1])\n\nAici key spune: nu compara tuplurile întregi, compară doar al doilea\nelement, nota. Fără lambda ar trebui să definești o funcție separată\npentru un singur rând de cod.\n\nParametrul reverse=True întoarce ordinea, de la mare la mic. Atenție:\nreverse răstoarnă tot criteriul, deci și departajările.\n\nUn truc util: cheia poate întoarce un tuplu, iar un număr se inversează\ncu minus, ca în key=lambda p: (-p[1], p[0]). Python compară tuplurile\nelement cu element, de la stânga la dreapta, deci întâi nota, apoi\nnumele.\n\nCând nu folosești lambda? Când funcția merită un nume, când o\nrefolosești în mai multe locuri sau când are nevoie de mai mult de o\nexpresie. Atunci def este mai limpede.',
        'exemplu': '# o functie anonima pastrata intr-o variabila\ndublu = lambda x: x * 2\nprint(dublu(5))\n# lambda folosita drept criteriu de sortare\norase = [("Chisinau", 3), ("Balti", 1), ("Orhei", 2)]\nprint(sorted(orase, key=lambda p: p[1]))\n# cheie cu tuplu: descrescator dupa numar, apoi alfabetic\nprint(sorted(orase, key=lambda p: (-p[1], p[0])))',
        'sarcina': 'Scrie funcția def sorteaza_dupa_nota(studenti): care primește o listă de\ntupluri de forma (nume, notă) și returnează o listă nouă, sortată\ndescrescător după notă. La note egale, studenții apar în ordine\nalfabetică după nume. De exemplu, sorteaza_dupa_nota([("Ana", 7),\n("Bogdan", 9)]) returnează [("Bogdan", 9), ("Ana", 7)]. Lista primită\nrămâne neatinsă, iar rezultatul se dă cu return.',
        'indicii': ['Ai două criterii, nu unul: nota contează prima, iar numele doar atunci\ncând notele sunt egale. Gândește-te cum poți exprima amândouă într-o\nsingură cheie de sortare.', 'Folosește funcția sorted cu parametrul key și o expresie lambda care\nprimește un tuplu (nume, notă). Reține că o cheie poate fi ea însăși un\ntuplu, cu două componente.', 'Pentru fiecare student, cheia are două părți. Prima este nota cu semn\nschimbat, ca sortarea crescătoare implicită să dea de fapt notele de la\nmare la mic. A doua este numele, lăsat așa cum este, ca la note egale\ndepartajarea să iasă alfabetic. Dai lista și cheia lui sorted, iar lista\nnouă întoarsă de sorted o returnezi direct.'],
        'greseala': 'Greșeala clasică este sorted(studenti, key=lambda p: p[1],\nreverse=True): notele ies corect, dar reverse răstoarnă și numele, deci\nla egalitate ordinea devine invers alfabetică. Pune minus pe notă în\ncheie și lasă sortarea crescătoare să rezolve numele. A doua capcană:\nstudenti.sort() modifică lista primită și returnează None, pe când\nsorted întoarce o listă nouă.',
        'teste': [(([('Ana', 7), ('Bogdan', 9)],), [('Bogdan', 9), ('Ana', 7)]), (([('Zina', 8), ('Ana', 8)],), [('Ana', 8), ('Zina', 8)]), (([],), []), (([('C', 5), ('A', 10), ('B', 7)],), [('A', 10), ('B', 7), ('C', 5)])],
    },
    {
        'nr': 3,
        'functie': 'imparte_sigur',
        'titlu': 'Tratarea erorilor cu try și except',
        'teorie': 'Când Python întâlnește ceva ce nu poate face, nu îți întoarce un cod de\neroare: aruncă o excepție. O excepție (situație excepțională) este un\nobiect care descrie problema și care oprește programul dacă nimeni nu o\nprinde. Împărțirea la zero ridică ZeroDivisionError, adunarea unui număr\ncu un șir ridică TypeError, un index prea mare ridică IndexError.\n\nCa programul să nu moară, pui codul riscant într-un bloc try și scrii în\nexcept ce faci la necaz:\n\ntry:\n    x = 10 / 0\nexcept ZeroDivisionError:\n    x = None\n\nMai există două ramuri. else rulează doar dacă în try nu a apărut nicio\nexcepție, iar finally rulează întotdeauna, cu eroare sau fără, și e\nlocul unde închizi un fișier sau eliberezi o resursă.\n\nRegula importantă: prinde excepția concretă. Un except gol prinde\nabsolut orice, inclusiv greșelile tale de scriere. Rezultatul e un\nprogram care tace și lucrează greșit, iar tu cauți ore întregi de unde\nvine problema. Scrie except ZeroDivisionError sau except (TypeError,\nValueError) și lasă restul erorilor să iasă la suprafață, ca să le poți\nrepara.\n\nȚine blocul try cât mai scurt, ideal doar rândul care chiar poate eșua.\nDacă bagi zece rânduri într-un try, nu mai știi care dintre ele a\naruncat excepția.\n\nȘi un sfat de gândire: excepțiile nu sunt pentru orice verificare. Dacă\npoți testa simplu înainte, testează. try se folosește când verificarea\nprealabilă ar fi complicată sau când eroarea vine din afară: un fișier\nlipsă, date scrise de utilizator, o rețea căzută.',
        'exemplu': 'def citeste_numar(text):\n    try:\n        n = int(text)      # poate arunca ValueError\n    except ValueError:\n        return None        # valoare de rezerva la eroare\n    else:\n        return n           # doar daca nu a aparut eroare\n    finally:\n        print("gata")      # ruleaza intotdeauna\nprint(citeste_numar("42"), citeste_numar("abc"))',
        'sarcina': 'Scrie funcția def imparte_sigur(a, b): care returnează rezultatul\nîmpărțirii a / b. Dacă b este zero, funcția returnează None. Dacă a sau\nb nu sunt numere, de exemplu dacă primești un șir de caractere,\nreturnează tot None. Funcția nu are voie să se oprească niciodată cu\neroare, oricare ar fi argumentele primite.',
        'indicii': ['Sunt două necazuri diferite, dar amândouă apar la aceeași operație, a /\nb: împărțirea la zero și argumentele care nu sunt numere. Lasă Python să\nîți spună care dintre ele s-a întâmplat.', 'Ai nevoie de un bloc try cu două ramuri except: una pentru\nZeroDivisionError și una pentru TypeError. Le poți scrie separat sau\nîntr-un singur except, cu un tuplu de excepții.', 'Pui împărțirea în try și returnezi rezultatul direct de acolo. Dacă b\neste zero, execuția sare în ramura pentru ZeroDivisionError, de unde\nreturnezi None. Dacă unul dintre argumente este text sau altceva ce nu\nse împarte, sare în ramura pentru TypeError și returnezi tot None. Nu ai\nnevoie de niciun if înainte: try acoperă amândouă cazurile.'],
        'greseala': 'Greșeala frecventă este un except gol, care prinde absolut orice,\ninclusiv greșelile tale de tipar, și ascunde erorile adevărate. Scrie\nnumele excepțiilor. A doua greșeală este să prinzi doar împărțirea la\nzero: un șir împărțit la un număr nu dă ZeroDivisionError, ci TypeError,\ndeci ai nevoie de ambele ramuri. Și nu înlocui return cu print, funcția\ntrebuie să întoarcă valoarea.',
        'teste': [((10, 2), 5.0), ((1, 0), None), (('a', 2), None), ((7, 2), 3.5), ((5, None), None)],
    },
    {
        'nr': 4,
        'functie': 'elemente_comune',
        'titlu': 'Mulțimi (sets)',
        'teorie': 'O mulțime (set, în engleză) este o colecție de valori în care fiecare\nvaloare apare o singură dată și în care ordinea nu contează. O scrii\nîntre acolade: {1, 2, 3}. Pentru mulțimea goală folosești set(), fiindcă\n{} înseamnă dicționar gol.\n\nDe ce nu are duplicate? Python ține valorile într-o tabelă de dispersie\n(hash table): calculează un cod numeric pentru fiecare valoare și o\nașază direct la locul ei. Dacă valoarea este deja acolo, nu o mai adaugă\na doua oară. Din același motiv nu are nici ordine: poziția depinde de\ncod, nu de momentul în care ai adăugat valoarea.\n\nTrei operații îți vor fi de folos mereu. Intersecția, a & b, îți dă\nvalorile care apar în ambele mulțimi. Reuniunea, a | b, îți dă toate\nvalorile, fiecare o singură dată. Diferența, a - b, îți dă ce este în a\nși nu este în b.\n\nCel mai mare câștig practic este însă viteza. Când scrii x in lista,\nPython parcurge lista element cu element: dacă lista are un milion de\nvalori, în cazul cel mai rău face un milion de comparații. Când scrii\nx in multime, calculează o singură dată codul lui x și se uită direct\nacolo. Verificarea aproape că nu depinde de mărimea mulțimii.\n\nDeci folosește mulțimi când vrei să scapi de duplicate, când compari\ndouă colecții sau când verifici de multe ori dacă o valoare există.\nFolosește liste când ordinea contează sau când ai nevoie de duplicate.\nDin mulțime revii oricând la o listă ordonată cu sorted(multime).',
        'exemplu': 'a = {1, 2, 2, 3}         # duplicatele dispar: {1, 2, 3}\nb = set([2, 3, 4])       # dintr-o lista faci o multime cu set()\nprint(a & b)             # intersectie: {2, 3}\nprint(a | b)             # reuniune: {1, 2, 3, 4}\nprint(a - b)             # diferenta: {1}\nprint(3 in a)            # apartenenta, foarte rapida: True\nprint(sorted(a & b))     # inapoi la lista sortata: [2, 3]',
        'sarcina': 'Scrie funcția cu semnătura def elemente_comune(a, b): care primește\ndouă liste și returnează o listă sortată crescător cu valorile care\napar în AMBELE liste, fără duplicate. De exemplu,\nelemente_comune([1, 2, 2, 3], [2, 3, 4]) trebuie să dea [2, 3].\nFuncția returnează rezultatul cu return, nu îl afișează cu print.',
        'indicii': ['Uită-te la cele trei cerințe din enunț: valori comune, fără\nduplicate, în ordine crescătoare. Fiecare dintre ele îți indică\ninstrumentul potrivit.', 'Îți trebuie set() ca să transformi listele în mulțimi, operatorul &\n(sau metoda intersection) pentru valorile comune și funcția sorted()\npentru ordonare.', 'Pas cu pas: transformă prima listă în mulțime; transformă și a doua\nlistă în mulțime; calculează intersecția celor două mulțimi, care îți dă\nexact valorile comune și scapă automat de duplicate; trece rezultatul\nprin sorted, care îți întoarce direct o listă crescătoare; returnează\nacea listă.'],
        'greseala': 'Greșeala cea mai frecventă este să returnezi mulțimea așa cum e:\n{2, 3} nu este o listă și nu are ordine garantată, deci verificarea\ncade. Trece mereu rezultatul prin sorted(), care returnează o listă.\nA doua capcană: set("abc") sparge șirul în litere și îți dă\n{"a", "b", "c"}, nu o mulțime cu un singur element.',
        'teste': [(([1, 2, 2, 3], [2, 3, 4]), [2, 3]), (([1], [2]), []), (([5, 3, 1], [1, 3, 5]), [1, 3, 5]), (([], [1]), [])],
    },
    {
        'nr': 5,
        'functie': 'total_peste_prag',
        'titlu': 'Map, filter, reduce',
        'teorie': 'Până acum prelucrai o listă cu un ciclu for: porneai de la o listă\ngoală, treceai prin elemente și adăugai ce te interesa. Există și un alt\nstil, numit programare funcțională: descrii transformarea pe care o\nvrei, nu pașii buclei.\n\nmap (aplică) primește o funcție și o colecție, apoi aplică funcția\nfiecărui element: map(int, ["1", "2"]) transformă fiecare șir în număr.\nfilter (filtrează) primește o funcție care răspunde cu True sau False și\npăstrează doar elementele pentru care răspunsul este True. reduce\n(reduce) combină toate elementele într-o singură valoare, luându-le câte\ndouă; stă în modulul functools, însă în practică folosești mai des\nfuncțiile gata făcute sum, min și max, care fac același lucru mai clar.\n\nFuncția scurtă pe care o dai lui map sau filter se scrie de obicei cu\nlambda: lambda x: x > 20 este o funcție fără nume, scrisă pe un rând.\n\nAtenție la un detaliu important: map și filter nu returnează o listă, ci\nun obiect leneș (lazy, adică amânat), care calculează valorile abia\natunci când i le ceri. De aceea îl treci prin list() ca să vezi\nrezultatul, sau direct prin sum() dacă vrei suma. Un obiect leneș se\nconsumă o singură dată: dacă l-ai parcurs deja, a doua oară pare gol.\nAvantajul lenei este memoria: nu se construiesc milioane de valori dacă\ntu ai nevoie doar de primele.\n\nAceleași lucruri le poți scrie și cu list comprehension (listă prin\nînțelegere): [x for x in preturi if x > prag] face exact ce face filter.\nAlege stilul care se citește mai ușor în locul acela.',
        'exemplu': 'preturi = [10, 50, 100]\nmari = filter(lambda x: x > 20, preturi)  # obiect lenes, nu lista\nprint(list(mari))                         # [50, 100]\nprint(list(mari))                         # [] - s-a consumat deja\ndublu = map(lambda x: x * 2, preturi)     # aplica functia peste tot\nprint(list(dublu))                        # [20, 100, 200]\nprint(sum(filter(lambda x: x > 20, preturi)))   # 150\nprint(round(float(150), 2))               # 150.0, cu doua zecimale',
        'sarcina': 'Scrie funcția cu semnătura def total_peste_prag(preturi, prag): care\nprimește o listă de prețuri și un prag, apoi returnează suma prețurilor\nstrict mai mari decât pragul, rotunjită la două zecimale. Trebuie să\nfolosești filter, iar map sau sum sunt opționale. De exemplu,\ntotal_peste_prag([10, 50, 100], 20) trebuie să dea 150.0.',
        'indicii': ['Ai două lucruri de făcut, în ordinea asta: mai întâi alegi prețurile\ncare depășesc pragul, abia apoi le aduni și rotunjești.', 'Îți trebuie filter cu o funcție lambda pentru selecție, apoi sum()\npentru total și round() cu al doilea argument egal cu 2.', 'Pas cu pas: construiește un filter peste lista de prețuri, cu o\nlambda care răspunde True atunci când prețul este strict mai mare decât\npragul; trece obiectul obținut prin sum, care îl consumă și îți dă\ntotalul; transformă totalul în float, ca să ai zecimale; rotunjește-l la\ndouă zecimale cu round; returnează valoarea rotunjită.'],
        'greseala': 'Greșeala clasică este să uiți că filter nu este o listă: afișat\ndirect, arată ca filter object at 0x..., iar parcurs a doua oară pare\ngol. Consumă-l o singură dată, prin sum sau prin list. A doua capcană\neste semnul >= în loc de >: pragul nu intră în sumă, se cer valori\nstrict mai mari. Și ține minte că round(150, 2) dă 150, nu 150.0, deci\nconvertește totalul la float înainte de rotunjire.',
        'teste': [(([10, 50, 100], 20), 150.0), (([1, 2], 5), 0.0), (([10.5, 20.25], 10), 30.75), (([], 3), 0.0)],
    },
    {
        'nr': 6,
        'functie': 'extrage_grupe',
        'titlu': 'Expresii regulate',
        'teorie': 'O expresie regulată (regular expression, pe scurt regex) este un mic\nlimbaj pentru descris tipare de text. În loc să cauți un cuvânt fix,\ndescrii forma a ceea ce cauți: două litere mari, o cratimă, trei cifre.\nApoi lași Python să găsească toate bucățile care se potrivesc. Fără\nregex ai scrie zeci de rânduri cu verificări de litere și cifre; cu\nregex, un singur rând.\n\nInstrumentele stau în modulul re, din biblioteca standard, și îl aduci\ncu import re. Cea mai utilă funcție pentru tine acum este\nre.findall(tipar, text): îți întoarce o listă cu toate potrivirile, în\nordinea în care apar în text. Dacă nu găsește nimic, îți dă lista goală,\nnu None.\n\nCărămizile tiparului sunt clasele de caractere și cuantificatorii.\nO clasă spune ce fel de caracter accepți: [A-Z] este o literă mare,\n[0-9] este o cifră, \\d înseamnă tot o cifră, \\w înseamnă literă, cifră\nsau liniuță de subliniere, iar punctul înseamnă orice caracter. Un\ncuantificator spune de câte ori se repetă ce ai scris înainte: {3}\nînseamnă exact de trei ori, + cel puțin o dată, * de zero ori sau mai\nmulte, ? cel mult o dată.\n\nDe ce se scrie r în fața tiparului? Fiindcă într-un șir obișnuit\nbackslash-ul pornește o secvență de evadare (escape) și ar trebui să\nscrii \\\\d ca să obții \\d. Un șir brut (raw string), scris r"\\d", îi\nspune lui Python să lase backslash-ul exact așa cum este, iar tiparul\nrămâne lizibil. Obișnuiește-te să pui r la orice tipar, chiar și când\npare că nu e nevoie.',
        'exemplu': 'import re\ntext = "Grupele SI-265 si FI-101 vin azi, dar ab-12 nu conteaza"\ntipar = r"[A-Z]{2}-[0-9]{3}"  # 2 litere mari, cratima, 3 cifre\nprint(re.findall(tipar, text))       # [\'SI-265\', \'FI-101\']\nprint(re.findall(r"\\d+", "a1 b22"))  # [\'1\', \'22\'] - una sau mai multe\nprint(re.findall(r"ZZ-000", text))   # [] - nicio potrivire',
        'sarcina': 'Scrie funcția cu semnătura def extrage_grupe(text): care primește un\ntext și returnează lista tuturor codurilor de grupă găsite, în ordinea\napariției. Un cod de grupă are forma: două litere mari, o cratimă, apoi\nexact trei cifre, de exemplu SI-266. Pentru textul\n"Grupele SI-265 si FI-101 vin azi" funcția trebuie să dea\n["SI-265", "FI-101"].',
        'indicii': ['Spune mai întâi cu voce tare forma codului, bucată cu bucată.\nTraducerea ei în tipar vine aproape de la sine.', 'Îți trebuie modulul re, funcția re.findall și un tipar scris ca șir\nbrut, cu clase de caractere și cuantificatorul {3}.', 'Pas cu pas: importă re; scrie tiparul ca șir brut, punând pe rând o\nclasă pentru litere mari repetată de două ori, apoi caracterul cratimă\nscris ca atare, apoi o clasă pentru cifre repetată de exact trei ori;\ncheamă re.findall cu tiparul și cu textul primit; findall îți dă deja o\nlistă în ordinea apariției, deci returneaz-o ca atare.'],
        'greseala': 'Două greșeli apar cel mai des. Prima: pui paranteze rotunde în tipar\nca să grupezi ceva, iar atunci findall nu mai returnează potrivirea\nîntreagă, ci doar conținutul grupurilor. Dacă nu ai nevoie de grupuri,\nscoate parantezele. A doua: folosești + în loc de {3} pentru cifre, iar\natunci un cod cu patru sau cinci cifre trece, deși nu ar trebui. Exact\ntrei cifre înseamnă {3}.',
        'teste': [(('Grupele SI-265 si FI-101 vin azi',), ['SI-265', 'FI-101']), (('nimic aici',), []), (('SI-266',), ['SI-266']), (('si-266 nu e valid, SI-2666 nici',), [])],
    },
]

INSTRUCTIUNI = 'Acest fisier este in acelasi timp manualul tau, terenul de\nantrenament si lucrarea pe care o predai. Nu ai nevoie de nimic altceva.\n\nPASUL 1 - Completeaza-ti datele\n  Deschide fisierul cu un editor de text (Notepad merge, dar IDLE sau\n  Visual Studio Code sunt mai comode) si scrie sus de tot numele,\n  prenumele si grupa ta, intre ghilimele.\n\nPASUL 2 - Alege o sarcina din meniu\n  Programul iti arata teoria in romana, un exemplu de cod si ce ai de\n  facut. Citeste tot inainte sa scrii ceva.\n\nPASUL 3 - Scrie codul in fisier\n  Fiecare sarcina are o functie pregatita, in partea de sus a fisierului.\n  Sterge randul  pass  si scrie rezolvarea ta in locul lui.\n  ATENTIE: functia trebuie sa RETURNEZE rezultatul cu  return , nu sa il\n  afiseze cu  print . Sunt lucruri diferite.\n\nPASUL 4 - Salveaza si verifica\n  Salveaza fisierul, intoarce-te in program si apasa Enter ca sa\n  reverifice. Daca nu e bine, iti spune exact ce se astepta si ce a\n  primit. Daca te blochezi, ai trei indicii, de la bland la aproape-solutie.\n\nPASUL 5 - Trimite lucrarea\n  Cand esti multumit de punctaj, alege din meniu optiunea\n  Pregateste fisierul pentru trimitere. Programul iti face automat o copie\n  denumita corect si iti scrie adresa si subiectul emailului.\n\nCUM SE CALCULEAZA NOTA\n  Partea 1 - Bazele: 13 sarcini, cate 1 punct fiecare.\n  Partea 2 - Jocul:   7 misiuni, cate 1 punct fiecare.\n  Partea 3 - Bonus:   6 sarcini, cate 1 punct, care acopera sarcinile\n                      nerezolvate din primele doua parti.\n  Punctaj maxim luat in calcul: 20.   Nota = punctaj impartit la 2.\n  Deci 20 de puncte inseamna nota 10, iar 10 puncte inseamna nota 5.\n\nDE UNDE INVETI\n  Teoria din program e suficienta. Daca vrei mai mult, fiecare capitol are\n  corespondent pe learnpython.org, sectiunea Learn the Basics, iar partea\n  bonus in sectiunea Advanced Tutorials. Pentru joc, te poti antrena si pe\n  codingforkids.io, nivelurile 1-7 din cursul de Python.\n\nREGULI\n  Codul il scrii tu. Poti discuta cu colegii despre CUM se rezolva, dar nu\n  copia codul altuia: se vede imediat, pentru ca iese identic caracter cu\n  caracter.'

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n   Intrerupt. Codul tau ramane salvat in fisier.\n")
