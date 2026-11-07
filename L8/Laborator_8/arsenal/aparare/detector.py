# -*- coding: utf-8 -*-
"""Laboratorul 8 - partea B. Detectorul de brute force."""
import argparse, json
from collections import Counter
from arsenal.aparare.parse_auth import citeste_esecuri, pe_ip


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


#  

def main():
    p = argparse.ArgumentParser()
    p.add_argument('log')
    p.add_argument('--prag', type=int, default=10)
    p.add_argument('--json', action='store_true')
    a = p.parse_args()
    esecuri = citeste_esecuri(a.log)
    counts = pe_ip(esecuri)
    sus = suspecti(counts, a.prag)
    if a.json:
        print(json.dumps({'esecuri': len(esecuri),
                          'pe_ip': dict(counts),
                          'suspecti': sus}, indent=2))
        return
    print('Esecuri de autentificare:', len(esecuri))
    for ip, n in counts.most_common():
        print('  %s: %d' % (ip, n))
    print('Suspecti (prag %d):' % a.prag)
    for ip, n in sus:
        print('  %s  (%d incercari)  BRUTE FORCE' % (ip, n))


if __name__ == '__main__':
    main()
