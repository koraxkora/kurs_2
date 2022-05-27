import statistics

class Uczen:

    def __init__(self, imie, nazwisko, lista_ocen=None):
        self.imie = imie
        self.nazwisko = nazwisko
        if lista_ocen is None:
            lista_ocen = []
        self.lista_ocen = lista_ocen

    def srednia(self):
        if len(self.lista_ocen) == 0:
            return("brak ocen")
        else:
            # return round(sum(self.lista_ocen) / len(self.lista_ocen), 1)
            return(statistics.mean(self.lista_ocen))

    def dodaj(self, ocena):
        self.lista_ocen.append(ocena)

    def __str__(self):
        return(f"Imie: {self.imie} Nazwisko: {self.nazwisko} Lista ocen: {', '.join(str(i) for i in self.lista_ocen):10} Średnia: {self.srednia()}")

u1 = Uczen("Ala", 'Maj')
u2 = Uczen("Jan", "Kow", [2, 3, 4])
print(u1)
print(u2)
u1.dodaj(2)
u1.dodaj(5)
print(u1)
print(u2)
