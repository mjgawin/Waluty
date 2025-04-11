
def pobierz_kurs(iso, dzien):
    from requests import get

    odpowiedz = get(f"http://api.nbp.pl/api/exchangerates/rates/a/{iso}/{dzien}/?format=json")

# http://api.nbp.pl/api/exchangerates/rates/a/usd/2022-08-31/?format=json
# parametr dla JSONa ?format=json

# LISTY
# lista = ["a","b","c"]
# print(lista[2])USD

# SŁOWNIKI
# paczka = {
#     "imie": "jan",
#     "nazwisko": "kowalski",
# }

# print(paczka["nazwisko"])

# dane = {
#     "table": "A",
#     "currency": "dolar amerykański",
#     "code": "USD",
#     "rates": [
#         {
#             "no": "168/A/NBP/2022",
#             "effectiveDate": "2022-08-31",
#             "mid": 4.7360
#         }
#     ]
# }



    if odpowiedz.ok:
        dane = odpowiedz.json()
        kurs = dane["rates"][0]["mid"]
# print("1", iso.upper(), "=", kurs, "PLN")
    return kurs
