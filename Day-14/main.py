# Day-14/main.py
from forex_python.converter import CurrencyRates
c = CurrencyRates()
print("CURRENCY CONVERTER")
amount = float(input("Amount: "))
from_cur = input("From (USD/INR/EUR): ").upper()
to_cur = input("To (USD/INR/EUR): ").upper()
result = c.convert(from_cur, to_cur, amount)
print(f"{amount} {from_cur} = {result:.2f} {to_cur}")