lista = ['Warszawa', 'Kraków', 'Łódź', 'Wrocław', 'Poznań', 'Gdańsk', 'Żyrardów', 'Zielona Góra', 'Wąchock', 'Wadowice']

print(lista)
print(sorted(lista))
print(lista)
print()

# Do funkcji sorted jako dodatkowy parametry key można podać funkcję,
# która zostanie uruchomiona dla każdego elementu listy i zwróci jego "wagę".
# A elementy listy zostaną posortowane wg uzyskanych "wag", domyślnie rosnąco.

# Przyjmijmy, że dla słowa jako jego wagę zwracamy długość (liczbę liter)
print(sorted(lista, key=lambda s: len(s)))

# Akurat w tym przypadku można bezpośrednio wskazać funkcję len; nie trzeba pisać lambda
print(sorted(lista, key=len))

# Inny przykład: posortujmy wg drugiej litery
print(sorted(lista, key=lambda s: s[1]))

# Tylko, żeby wytłumaczyć kwestię lambdy.
# Taką funkcję biorącą drugi znak z napisu można też zdefiniować tradycyjnie:
def drugi_znak(napis):
   return napis[1]

# i teraz przekazać do sorted
print(sorted(lista, key=drugi_znak))
print()

### Sortowanie tekstów zgodnie z alfabetem polskim (i nie tylko) ###

import locale
# Zauważmy, że w tym miejscu jeszcze nie ma poprawnego sortowania
print(locale.getlocale(locale.LC_COLLATE))
print('Łukasz' < 'Marcin')
print(locale.strcoll('Łukasz', 'Marcin') < 0)
print(sorted(lista, key=locale.strxfrm))
print()

# Trzeba ustawić język w module locale
# Można ustawić na konkretny
locale.setlocale(locale.LC_COLLATE, 'Polish') # albo LC_ALL
print(locale.getlocale(locale.LC_COLLATE))
print('Łukasz' < 'Marcin')
print(locale.strcoll('Łukasz', 'Marcin') < 0)
print(sorted(lista, key=locale.strxfrm))
print()

locale.setlocale(locale.LC_COLLATE, 'pl_PL')
print(locale.getlocale(locale.LC_COLLATE))
print(sorted(lista, key=locale.strxfrm))
print()

locale.setlocale(locale.LC_ALL, 'French')
print(locale.getlocale(locale.LC_COLLATE))
print(sorted(lista, key=locale.strxfrm))
print()

locale.setlocale(locale.LC_ALL, 'fr_FR.UTF8')
print(locale.getlocale(locale.LC_COLLATE))
print(sorted(lista, key=locale.strxfrm))
print()


# Gdy podamy pusty string, to przyjmowane są bieżące ustawienia z systemu
locale.setlocale(locale.LC_ALL, '')
print(locale.getlocale(locale.LC_COLLATE))
print(sorted(lista, key=locale.strxfrm))
print()

# Jak działa sama funkcja strxfrm?
# Na podstawie tekstu źródłowego zwraca "techniczny" tekst, który sortowany już po kodach unicode/ascii da właściwą kolejność
print(locale.strxfrm('zebra'))
print(repr(locale.strxfrm('zebra')))
print(repr(locale.strxfrm('żebra')))
print(repr(locale.strxfrm('żółw')))


print()
# Tutaj element 0 uzyska wartość True, a po zrzutowaniu na int to będzie 1
# pozostałe False, a po zrzutowaniu na int to będzie 0.
# Wskazany element (0) będzie na końcu.
xs = [1, 0, 2]
print(sorted(xs, key=lambda x: x==0))



