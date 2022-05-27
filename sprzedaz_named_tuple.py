from typing import List
from decimal import Decimal
from dataclasses import dataclass
from collections import namedtuple

# Transakcja = namedtuple('Transakcja', 'data, miasto, sklep, kategoria, towar, cena, sztuk')  # kind of collection
Transakcja = namedtuple('Transakcja', ['data', 'miasto', 'sklep','kategoria', 'towar', 'cena', 'sztuk'])
#  raczej jako zestaw danych jeżeli nie chcemy używac funkcji na tych dancyh

def read_file(file_name):
    """
    funkcja czyta dane z pliku

    :param file_name: ścieżka do pliku .csv
    :return: lista obiektów Transakcje wczytanych z pliku
    """
    lista = []
    with open(file_name, 'r', encoding='utf-8') as f:
        f.readline()
        for linia in f:
            t = linia.strip(). split(',')
            lista.append(Transakcja(*t[:5], Decimal(t[5]), int(t[6])))
            # lista.append(Transakcja(Decimal(t[5]), int(t[6]), *t[:5]))
    return lista

lista = read_file('sprzedaz.csv')

sales = 0
for rekord in lista:
    if rekord.miasto == 'Katowice':
        sales += rekord.cena * rekord.sztuk

# print(sales)


print(lista[2])