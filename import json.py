import json
import requests

coin = input("Name of Coin: ")
url = f'https://api.coingecko.com/api/v3/coins/list'
response = requests.get(url)
data = json.loads(response.text)
#print(data)
def get_symbol(name):
    for coin in data:
        if coin ['name'] == name:
            return coin ['symbol']
    
        if coin ['symbol'] == None:
                coin = coin.upper()
                symbol = coin ['symbol']
                return symbol
        elif coin ['symbol'] == None:
                coin = coin.capitalize()
                return coin ['symbol']
        else:
                print(f"{coin}'s symbol is not found")
        return None
#coin = coin.capitalize()
print(f'Coin: {coin} /n Symbol {symbol}')