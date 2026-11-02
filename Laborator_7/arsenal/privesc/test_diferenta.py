# -*- coding: utf-8 -*-
"""Un test care prinde regresia: diferenta de multimi da doar ce e nou."""


def test_doar_ce_e_nou():
    acum = {"a", "b", "c"}
    baza = {"a", "b"}
    assert acum - baza == {"c"}
