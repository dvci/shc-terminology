import pytest
from cvx_parsing import *


def test_retrieve_new_cvx():
    cvx = retrieve_new_cvx()
    assert cvx[208]['short-description'] == "COVID-19, mRNA, LNP-S, PF, 30 mcg/0.3 mL dose"


def test_retrieve_new_cvx_product_names():
    names = retrieve_new_cvx_product_names()
    assert names[208] == 'COMIRNATY'

    # No empty product names
    assert [n for n in names.values() if n == ''] == []


def test_filter_cvx():
    cvx = retrieve_new_cvx()

    filter1 = filter_cvx(cvx, ['smallpox', 'monkeypox'])
    assert list(filter1.keys()) == [75, 105, 206]