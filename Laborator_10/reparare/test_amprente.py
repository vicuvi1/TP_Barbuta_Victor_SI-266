# -*- coding: utf-8 -*-
# Teste pentru Lucrarea B. NU le modifica: descriu cum TREBUIE sa se poarte unealta.
# Ruleaza cu: python -m pytest -q   (din folderul reparare/)
import os
from amprente import tip, amprenta_fisier, scaneaza
PROBE = os.path.join(os.path.dirname(__file__), "probe")


def test_tip_din_magic():
    assert tip(b"\x89PNG\r\n") == "PNG"
    assert tip(b"%PDF-1.4") == "PDF"
    assert tip(b"text oarecare") == "necunoscut"


def test_amprenta_png():
    r = amprenta_fisier(os.path.join(PROBE, "imagine.png"))
    assert r["tip"] == "PNG"
    assert r["sha256"] == "ea3a9848da7e6c1d"


def test_scaneaza_toate():
    rez = scaneaza(PROBE)
    assert len(rez) == 4
    assert {f["tip"] for f in rez} == {"PNG", "PDF", "ZIP", "necunoscut"}
