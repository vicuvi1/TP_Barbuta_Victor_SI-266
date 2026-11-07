import requests

from arsenal.comun import TIMEOUT


def cere(url, **kw):
    return requests.get(url, timeout=TIMEOUT, **kw)


def exista(url):
    return cere(url).status_code == 200
