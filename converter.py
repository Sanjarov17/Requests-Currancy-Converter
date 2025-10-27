import requests

url = "https://cbu.uz/uz/arkhiv-kursov-valyut/json/"
response = requests.get(url)
data = response.json()

usd_rate = None
eur_rate = None
date = None

for item in data:
    if item["Ccy"] == "USD":
        usd_rate = float(item["Rate"])
        date = item["Date"]
    elif item["Ccy"] == "EUR":
        eur_rate = float(item["Rate"])

if not usd_rate or not eur_rate:
    print("Valyuta kurslarini olishda xatolik!")
    exit()

while True:
    try:
        amount = float(input("Enter amount: "))
        break
    except ValueError:
        print("Notogri qiymat! Iltimos, son kiriting.")

from_currency = input("From currency (USD, UZS, EUR): ").upper()
to_currency = input("To currency (USD, UZS, EUR): ").upper()

def convert(amount, from_cur, to_cur):
    if from_cur == to_cur:
        return amount
    if from_cur == "USD":
        uzs = amount * usd_rate
    elif from_cur == "EUR":
        uzs = amount * eur_rate
    elif from_cur == "UZS":
        uzs = amount
    else:
        raise ValueError("Noma'lum valyuta turi!")
    if to_cur == "USD":
        return uzs / usd_rate
    elif to_cur == "EUR":
        return uzs / eur_rate
    elif to_cur == "UZS":
        return uzs
    else:
        raise ValueError("Noma'lum valyuta turi!")

try:
    result = convert(amount, from_currency, to_currency)
    print(f"\n{amount:,.2f} {from_currency} = {result:,.2f} {to_currency} ({date})")
except ValueError as e:
    print(e)

