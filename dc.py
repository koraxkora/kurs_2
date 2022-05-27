from dataclasses import dataclass


class Osoba1:
    imie: str
    nazwisko: str
    wiek: int


a = Osoba1()
b = Osoba1()

a.imie = 'Ala'
print(b.imie)
########

@dataclass
class Osoba2:
    imie: str
    nazwisko: str
    wiek: int

a = Osoba2('Ala', 'Kowalska', 30)
print(a)
