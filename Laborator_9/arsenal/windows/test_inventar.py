# -*- coding: utf-8 -*-
"""Doua teste: metoda e_suspect pe un proces din Temp si pe unul curat."""
from arsenal.windows.inventar import Proces


def test_proces_din_temp_e_suspect():
    p = Proces(1, 'x.exe', 'ana', r'C:\Users\ana\AppData\Local\Temp\x.exe')
    assert p.e_suspect() is True


def test_proces_din_windows_nu_e_suspect():
    p = Proces(2, 'svchost.exe', 'SYSTEM', r'C:\Windows\System32\svchost.exe')
    assert p.e_suspect() is False
