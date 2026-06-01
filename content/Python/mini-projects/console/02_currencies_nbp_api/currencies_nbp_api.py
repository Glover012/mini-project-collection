import requests

address = "http://api.nbp.pl/api/exchangerates/tables/a/?format=json"

response = requests.get("{}".format(address))

if response.ok == True:
    data = response.json()
    currenciesData = data[0]["rates"]

    print("Currency list and prices in PLN\n")
    for currencyInfo in currenciesData:
        print(f"Currency: { currencyInfo["currency"] } - Price: { currencyInfo["mid"] }")
