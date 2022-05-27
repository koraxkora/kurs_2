from typing import List
from decimal import Decimal
from dataclasses import dataclass

@dataclass  # automatycznie generuje init, str, repr, eq
# które działają we właściwy sposób dla rekordów z polami takimi, jak wymienione w klasie
class Transakcja:
    data: str
    miasto: str
    sklep: str
    kategoria: str
    towar: str
    cena: Decimal
    sztuk: int

    def __str__(self):
        return f'Transakcja z dnia {self.data} w mieście {self.miasto}: {self.sztuk} towaru {self.towar} ' \
               f'w cenie {self.cena}al bo zupełnie coś innego'

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
                lista.append(Transakcja(*t[:5], Decimal(t[5]), int(t[6])))
                # lista.append(Transakcja(Decimal(t[5]), int(t[6]), *t[:5]))
        return lista

lista = Transakcja.read_file('sprzedaz.csv')  # inna zmiana

sales = 0
for rekord in lista:
    if rekord.miasto == 'Katowice':
        sales += rekord.amt

print(sales)

print(sum([rekord.amt for rekord in lista if rekord.miasto == 'Katowice']))