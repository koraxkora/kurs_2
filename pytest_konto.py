class BrakSrodkow(Exception):
    pass

class Konto:
    def __init__(self, no, owner, balance=0):
        self.no = no
        self.owner = owner
        self.balance = balance

    def wplata(self, amt):
        if amt <= 0:
            raise ValueError("Wpłata musi byc większa od zera")
        self.balance += amt

    def wyplata(self, amt):
        if amt < 0:
            raise ValueError("Kwota musi byc dodatnia")
        if amt > self.balance:
            raise BrakSrodkow("Wypłata nie może być wieksza niż saldo")
        self.balance -= amt

