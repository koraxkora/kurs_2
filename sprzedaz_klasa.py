from typing import List
from decimal import Decimal

class Transakcja:
    def __init__(self, data: str, miasto, sklep, kategoria, towar, cena: str, sztuk: int, *args):
        self.data = data
        self.miasto = miasto
        self.sklep = sklep
        self.kategoria = kategoria
        self.towar = towar
        self.cena = Decimal(cena)
        self.sztuk = int(sztuk)

    def __str__(self):
        return f'Transakcja z dnia {self.data} w mieście {self.miasto}: {self.sztuk} towaru {self.towar} ' \
               f'w cenie {self.cena}'

    @property
    def amt(self) -> Decimal:
        return self.cena * self.sztuk

    @staticmethod
    def read_file(file_name) -> List['Transakcja']:
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
                lista.append(Transakcja(*t))
        return lista

lista = Transakcja.read_file('sprzedaz.csv')

sales = 0
for rekord in lista:
    if rekord.miasto == 'Katowice':
        sales += rekord.amt

print(sales)

print(sum([rekord.amt for rekord in lista if rekord.miasto == 'Katowice']))