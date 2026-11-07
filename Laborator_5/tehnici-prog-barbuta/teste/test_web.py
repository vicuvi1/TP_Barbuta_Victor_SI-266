from arsenal.web.client import exista


def test_exista():
    assert exista("http://example.com/")


def test_lipsa():
    assert not exista("http://example.com/zzz")
