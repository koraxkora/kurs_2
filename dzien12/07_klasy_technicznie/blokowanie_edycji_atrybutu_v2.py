
class C:
	def __init__(self, imie, nazwisko):
		self.imie = imie
		self.nazwisko = nazwisko
		self._freezed = True

	def __setattr__(self, key, value):
		if '_freezed' in self.__dict__ and self._freezed:
			raise AttributeError(f'nie wolno już zmieniać obiektu')
		super().__setattr__(key, value)


c = C('Ala', 'Kowalska')
print('Jest obiekt, imie = ', c.imie)
c.imie = 'Alicja'
print('Udało się ustawić imię', c.imie)
