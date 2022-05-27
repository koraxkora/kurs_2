import pytest
from pytest_konto import Konto, BrakSrodkow

@pytest.fixture  # dekorator dla - zestaw obiektów testowych dla metod testowych
def konto():  # metoda 'inicjalizacyjna' dostępna w innych klasach przez (1) dekorator; nazwa zgodna funkcjij do użycia
    return Konto(no=1, owner="Ala", balance=100)
# może być więcej metod inicjalizujących

# Teraz, gdy jakaś metoda testowa X posiada parametr o takiej nazwie Y, jak nazwa funkcji oznaczonej fixture,
# to do funkcji testującej X jest przekazywany wynik funkcji Y.
# Funkcja Y tworząca obiekt będzie uruchamiana za każdy razem. Nowy obiekt dla każdego testu.

# v3 zmiana na klasę
# v4 klasa z setup_method
# check jeszcze tear_down_method, tear_down_class, setup_class

def test_init(konto):  # metoda inicjalizacyjna jako parametr
    assert konto.no == 1
    assert konto.owner == 'Ala'
    assert konto.balance == 100

def test_init_bal_0():
    konto = Konto(1, 'Ala')
    assert konto.no == 1
    assert konto.owner == 'Ala'
    assert konto.balance == 0

def test_init_wplata(konto):
    konto.wplata(100)
    assert konto.balance == 200

def test_init_wplata_neg():
    konto = Konto(1, 'Ala', 300)
    with pytest.raises(ValueError):
        konto.wplata(-10)

def test_init_wyplata():
    konto = Konto(1, 'Ala', 200)
    konto.wyplata(30)
    assert konto.balance == 170

def test_init_wyplata_over():
    konto = Konto(1, 'Ala', 200)
    with pytest.raises(BrakSrodkow):  # match='text exception'
        konto.wyplata(300)
    assert konto.balance == 200

def test_init_wyplata_neg():
    konto = Konto(1, 'Ala', 1200)
    with pytest.raises(ValueError):
        konto.wyplata(-10)
    assert konto.balance == 1200
