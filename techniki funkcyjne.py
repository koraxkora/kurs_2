# Funkcję można wpisać jako element kolekcji

def powitaj():
   print('Witamy serdecznie')

def pozegnaj():
   print('Do zobaczenia!')


lista_funkcji = [powitaj, pozegnaj, lambda: print('A to jest lambda'), lambda: print('A to kolejna lambda')]

for f in lista_funkcji:
   f()
y=2
print(lambda y:2**2 if y==2 else 3)
