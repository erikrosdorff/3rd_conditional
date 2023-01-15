import requests
import json
import numpy as np
import pandas
from datetime import datetime, date
#find enpoint for history of coin
#fetch data with python

coin = input('Name of coin: ')
currency = input('Enter currency: ')

start_date, end_date = None, None

while start_date is None:
    rawinput_start = input("Enter start date in DD MM YYYY: ")

    try:
        # %Y stands for a fully specified year, such as 2017, 1994, etc.
        # %m for the integer representation of a month, e.g. 01, 06, 12
        # and %d for the day of the month
        start_date = datetime.strptime(rawinput_start, "%d %m %Y")
    except ValueError:
        print('Input must be \<day number> <month number> <year number>')

while end_date is None:
    rawinput_end = input("Enter end date in DD MM YYYY: ")
    
    try:
        end_date = datetime.strptime(rawinput_end, "%d %m %Y")
    except ValueError:
        print('Input must be \<day number> <month number> <year number>')

diff_days = end_date - start_date

print("%d days" % diff_days.days)

url = f'https://api.coingecko.com/api/v3/coins/{coin}/market_chart?vs_currency={currency}&days={diff_days}'
response = requests.get(url)
data = json.loads(response.text) #.text converts it to text format
print(data)