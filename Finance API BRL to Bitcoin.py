import requests

def convert_currency(amount, from_currency, to_currency):
    API_KEY = "3c8328e9c2e64402b63014720dbf8094"
    base_url = f"https://openexchangerates.org/api/latest.json?app_id={API_KEY}"
    response = requests.get(base_url)
    data = response.json()
    exchange_rate = data["rates"][to_currency]/data["rates"][from_currency]
    return amount * exchange_rate

amount = float(input("Digite a quantidade em Reais: "))
converted_amount = convert_currency(amount, "BRL", "BTC")

print(f"{amount} Reais é igual a {converted_amount} Bitcoins")
