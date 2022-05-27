# W tej wersji funkcja, którą chcemy przetestować, oraz jej testy umieszczamy w jednym pliku.
# 0 1 1 2 3 5 8 13 21 34 55

import pytest

def fib(n):
   if n < 0:
       raise ValueError('Ujemny argument fib')
   if n <= 1:
       return n
   return fib(n-1) + fib(n-2)

# albo a parametrami
@pytest.mark.parametrize("argument, wynik", [(0, 0), (1, 1), (2, 1), (5, 5), (10, 55)])
@pytest.mark.timeout(10)  # after n sek break the program - not working sth else
def test_fib(argument, wynik):
   assert fib(argument) == wynik

# albo pojedynczo
def test_fib_0():
   assert fib(0) == 0

def test_fib_1():
   assert fib(1) == 1

def test_fib_5():
   assert fib(10) == 55

def test_fib_ujemna():
   # ma dojść do takiego wyjątku
   with pytest.raises(ValueError):
       fib(-1)



