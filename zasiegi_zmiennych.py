class Konto:
   def __init__(self, numer, wlasciciel, saldo):
       self._numer = numer
       self._wlasciciel = wlasciciel
       self._saldo = saldo

   def __str__(self):
       return f'Konto nr {self._numer}, wł. {self._wlasciciel}, saldo: {self._saldo}'

   def wplata(self, kwota):
       self._saldo += kwota

   def wyplata(self, kwota):
       self._saldo -= kwota

class Osoba:
   def __init__(self, imie, nazwisko):
       self.imie = imie
       self.nazwisko = nazwisko

   def __str__(self):
       return f'{self.imie} {self.nazwisko}'

def funkcja(a, b, c, x):
   print('Początek funkcji:')
   print('a:', a, id(a))
   print('b:', b, id(b))
   print('c:', c, id(c))
   print('x:', x, id(x))
   print()

   print('Koniec funkcji:')
   print('a:', a, id(a))
   print('b:', b, id(b))
   print('c:', c, id(c))
   print('x:', x, id(x))
   print()


def main():
   a = Konto(1, 'Ala', 1000)
   b = Konto(2, 'Ola', 2000)
   c = b
   x = 5000

   print('Początek main:')
   print('a:', a, id(a))
   print('b:', b, id(b))
   print('c:', c, id(c))
   print('x:', x, id(x))
   print()

   funkcja(a, b, c, x)
   print('Koniec main:')
   print('a:', a, id(a))
   print('b:', b, id(b))
   print('c:', c, id(c))
   print('x:', x, id(x))


main()
