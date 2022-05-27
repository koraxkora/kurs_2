"""
Zaimplementuj klasę Vector dostarczającą funkcjonalność wektora
swobodnego na dwuwymiarowej płaszczyźnie. Wektory powinny
mieć możliwość dodawania, odejmowania, mnożenia (przez liczbę),
porównywania (po długości) oraz powinny posiadać czytelną
reprezentację napisową.

"""



halo halo!  kora z tej strony
import math

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"<{self.x},{self.y}>"

    def __repr__(self):
        return f"Vector({self.x},{self.y})"

    def __add__(self, other):
        return Vector((self.x + other.x), (self.y + other.y))

    def __sub__(self, other):
        return Vector((self.x - other.x), (self.y - other.y))

    def __mul__(self, a):
        return Vector((self.x * a), (self.y * a))

    def __rmul__(self, a):
        return Vector((self.x * a), (self.y * a))

    def v_len(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __eq__(self, other):
        return self.v_len() == other.v_len()

    def __le__(self, other):
        return self.v_len() <= other.v_len()

    def __lt__(self, other):
        return self.v_len() < other.v_len()

    def __bool__(self):
        return self.v_len() != 0

vector_1 = Vector(x=1, y=2)
vector_11 = Vector(x=2, y=1)
vector_2 = Vector(x=3, y=1)
vector_3 = vector_1 + vector_2
vector_4 = vector_1 - vector_2
vector_5 = vector_1 * 3
vector_6 = 3 * vector_1
vector_7 = Vector(0, 0)

print(vector_1)
print(vector_2)
print('+', vector_3)
print('-', vector_4)
print('v*int', vector_5)
print('int*v', vector_6)
print('len', vector_3.v_len())
print(True if vector_6 else False, 'v6')
print(True if vector_7 else False, 'v7')


print(vector_1, 'vs', vector_11)
print('==', vector_1 == vector_11)
print('<=', vector_1 <= vector_11)
print('<', vector_1 < vector_11)
print('!=', vector_1 != vector_11)
print('>=', vector_1 >= vector_11)
print('>', vector_1 > vector_11)
print(vector_1, 'vs', vector_2)
print('==', vector_1 == vector_2)
print('<=', vector_1 <= vector_2)
print('<', vector_1 < vector_2)
print('!=', vector_1 != vector_2)
print('>=', vector_1 >= vector_2)
print('>', vector_1 > vector_2)


def proste_testy():
   a = Vector(3, 4)
   b = Vector(5, 11)
   print('a:', a)
   print('b:', b)

   print('repr a:', repr(a))
   print('repr b:', repr(b))
   print()

   wynik = a + b
   print(wynik)

   wynik = a - b
   print(wynik)

   wynik = a * 5
   print(wynik)

proste_testy()
