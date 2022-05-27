from decimal import Decimal

with open('sprzedaz.csv', 'r', encoding='utf-8') as f:
    lines = [line.strip().split(',') for line in f.readlines()][1:]

sales = 0
miasto = 'Katowice'
for line in lines:
    if line[1] == miasto:
        sales += round(float(line[5]) * float(line[6]), 2)
        # sales += Decimal(x[5]) * Decimal(x[6])  # Decimal approach

print(f"sales in {miasto}: {sales:.2f}")

