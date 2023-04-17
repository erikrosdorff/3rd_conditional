import json
import requests
def con_data(coin, currency):
        coin = input("Name of Coin: ")

        url_name_symbol = 'https://api.coingecko.com/api/v3/coins/list'
        response_name_symbol = requests.get(url_name_symbol)
        data = json.loads(response_name_symbol.text)

        desired_coin = coin
        for c in data:
            if c['id'] == desired_coin:
                symbol = c['symbol']
                break
        else:
            print(f"Coin '{coin}' not found.")
        currency = input("Currency: ")
        url_data = f'https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies={currency}' 
        response = requests.get(url_data)
        data = json.loads(response.text)
        price = data[coin][currency]
        print({coin:price})
        #return coin, symbol
        print(f'Coin: {coin.capitalize()}\n Symbol : {symbol} with a price of {price} {currency.upper()}')