# Przedefiniowując metodę setattr możemy zmienić zachowanie Pythona
# w zakresie ustawiana atrybutów.
# Możemy np. zabronić ustawiania niektórych atrybutów, albo stworzyć klasę niemutowalną.

class C:
  def __init__(self, imie, nazwisko):
     self.imie = imie
     self.nazwisko = nazwisko

  def __setattr__(self, key, value):
     print(f'Próba ustawienia atrybutu {key} na wartość {value}')
     if key in ['imie', 'nazwisko']:
        print('OK, atrubut dopuszczalny')
        super().__setattr__(key, value)
     else:
        print('Niepoprawny atrybut')
        raise AttributeError(f'nie wolno ustawiać atrybutu {key}')


c = C('Ala', 'Kowalska')
c.imie = 'Alicja'
print('Udało się ustawić imię', c.imie)

try:
  c.zwierze = 'kot'
  print('Udało się ustawić zwierze', c.zwierze)
except Exception as e:
  print('Nie udało się ustawić zwierze:', e)

