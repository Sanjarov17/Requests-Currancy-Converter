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


