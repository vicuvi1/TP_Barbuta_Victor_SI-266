# -*- coding: utf-8 -*-
"""Trei teste care dovedesc ca unealta merge (ruleaza din radacina depozitului:
   python -m pytest -q arsenal/forensics/test_amprente.py)."""
import os
from arsenal.forensics.amprente import tip, amprenta_fisier, scaneaza
PROBE = os.path.join(os.path.dirname(__file__), "probe")


def test_tip_din_magic():
    assert tip(b"\x89PNG") == "PNG"
    assert tip(b"text") == "necunoscut"


def test_amprenta_png():
    r = amprenta_fisier(os.path.join(PROBE, "imagine.png"))
    assert r["sha256"] == "ea3a9848da7e6c1d"


def test_scaneaza_toate():
    assert len(scaneaza(PROBE)) == 4
