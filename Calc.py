# lets make a calucator that shows our ROI in crypto staking
'''
V1
Insert coins manually and calculate

#convert to currency (e.g. usd -> $ etc.)

v2
See history of "would have been" investments

Create data structure
-tables #amount #relation
-API service (2 API) (optional)

v3
Connect through API (VPN?)

Money balance equation
robertson's cash-balance equation
p = m/kt

quantity theory of money formula
m*v = p*t
m = money supply
v = velocity of money
p = general price of goods
t = all transactions

Looks at your current shares:
1) Shows how much you have in Currency and USD (or any other variant of your choosing)
2) If you stake a coin, what will be the return in coin currency and in fiat currency
3) Shows minium and maximuim return estamates per week, month, and year.
4) Finds your target, and suggests how much you need to invest based on the current price
5) Shows changes in price and how much you should invest to make your target
6) Shows how much you would have needed to invest based on previous prices

#a = p(1 + (r/n))**(n*t)

n = number of times per t (e.g. 1 time a week is 52)
returns_per_week = (amount_staked * .04)/12)/4) #p
interest_rate = reward_percentage #kraken #r
def number_of_times_per_period(times) #n
if 1 time per week:
    num_of_times_per_period = 12/4
else: #twice a week
    num_of_times_per_period = (12/4)/2
t = length_of_time

staked_interest = returns_per_week(1 + (interest_rate/number_of_times_per_week))**(number_of_times_per_week/t) )

Select Coin
Select Currency
Select Compouded or Returned
#Connect Kraken account somehow?
See price history

{Coin}  {Symbol}    Price per {currency}   Staking     Staking ROI Percentage     Min ROI Per Week {Coin}   Max ROI Per Week {Coin}      Min ROI Per Week {Currency}   Max ROI Per Week {Currency}     

    Estimated ROI Per Month #average    Min ROI Per Month{coin}   Max ROI Per Month{coin}   Min ROI Per month based on {price per{currency}}    Max ROI Per month based on {price per{currency}}

    Estimated ROI per year #average     Min ROI in 1 year{coin}   Max ROI in 1 year{coin}   Min ROI Per year based on {price per{currency}}    Max ROI Per year based on {price per{currency}}

    Min max rewards earned      min max rewards earned

'''
#a = p*(1 + (r/n))**(n,t)
# A = the future value of the investment/loan, including interest
# P = the principal investment amount (the initial deposit or loan amount)
# r = the annual interest rate (decimal)
# n = the number of times that interest is compounded per unit t
# t = the time the money is invested or borrowed for
# [staked_interest = returns_per_week(1 + (interest_rate/number_of_times_per_week))**(number_of_times_per_week/t) )]
# If an amount of $5,000 is deposited into a savings account at an annual interest rate of 5%,
# compounded monthly, the value of the investment after 10 years can be calculated as follows...
#P = 5000.
# r = 5/100 = 0.05 (decimal).
#n = 12.
#t = 10.
# If we plug those figures into the formula, we get the following:
# A = 5000 (1 + 0.05 / 12) (12 * 10) = 8235.05.
# So, the investment balance after 10 years is $8,235.05
# This section only takes in the coin's value
# from pycoingecko import CoinGeckoAPI
# cg = CoinGeckoAPI()
import json
import requests

coin = input("Enter name of the coin: ")
symbol = input("Enter coin Symbol: ")
currency = input('Enter Currency: ')
url = f'https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies={currency}'#input('Enter - ') #ask for url
response = requests.get(url)
print('response.text: ', response.text)
data = json.loads(response.text)
print('data: ', data)
price = data[coin][currency]
print(coin, price)

# price_input = float(input("Enter current price of coin USD: "))
# price = float(price_input)
try:
    staking = float(input("Enter how many coins are being staked: "))
except:
    staking = int(input("Enter how many coins are being staked: "))    
min_reward_input = float(input("Enter minimuim reward percentage, e.g. 12: "))
# fstring converts to percentage
min_reward = float(f'{min_reward_input / 100}')


def max_reward_fun(max):
    if max == 'None' or 'none' or 0:
        return None
    else:
        return max

max = input(
    "Enter maximuim reward percentage (If there is only one, simply write 'none'): ")
try: #Should there not be a max percentage, the program will pass over
    max_reward = float(max) / 100
except:
    pass
print("Enter time period you would like to compound")
time_period = input("Enter either Y M W: ")
#a = p*(1 + (r/n))**(n*t)
def convert_time_period(time_period):  # t in the equation // amount of times in a period
    #Choose a time period
    if time_period.upper() == 'Y':
        years = int(input("Enter amount of years: "))
        time_period = int(years)
    elif time_period.upper() == 'M':
        months = int(input("Enter amount of months: "))
        time_period = int(months)  # find for different months
    elif time_period.upper() == 'W':
        weeks = int(input("Enter amount of weeks: "))
        time_period = int(weeks)
    else:
        print("Not a valid time period.")
        quit()
    return time_period

time_conversion = int(convert_time_period(time_period))
#a = p*(1 + (r/n))**(n*t)
print("Enter number of times interest is compounded: ") #find n - number of times the compound will be invested
num_times_interest_compounded_n = input(
    "Daily 'D' Weekly 'W' Monthly 'M' Yearly 'Y' or any number: ")  # Daily Weekly Monthly Yearly
# create flexibility in amount of time to compound (e.g. 2 times a week)
def find_num_of_compound(num_times_interest_compounded_n):
    if num_times_interest_compounded_n.isnumeric():
        return float(num_times_interest_compounded_n)

    char = num_times_interest_compounded_n.upper()
    if char == 'D' or char == 'DAILY':
        return 365 * time_conversion
    elif char == 'W' or char == 'WEEKLY':
        return 52 * time_conversion
    elif char == 'M' or char == 'Monthly':
        return 12 * time_conversion
    elif char == 'Y' or char == 'Yearly':
        return 1 * time_conversion

num_of_compound = int(find_num_of_compound(num_times_interest_compounded_n))
# def num_investments (n):
# def amount_time(time):
# n = amount of times in a certain period you invest (t)
# t = time period (Year, day, month, etc.)
#a = p*(1 + (r/n))**(n*t)
#round_compound = round(num_of_compound, 10)
# print(round_compound)
#round_compound = float(round_compound)
# min_returns_per_week = (staking * (round_compound/min_reward)) #p = the principal investment amount (the initial deposit or loan amount) /12 months /4 weeks
# max_returns_per_week = (staking * (round_compound/max_reward))
# p = the principal investment amount (the initial deposit or loan amount) /12 months /4 weeks
#min_returns_per_week = (staking * min_reward/num_of_compound)
#max_returns_per_week = (staking * max_reward/num_of_compound)
# 1 = 1 year need to figure out the time calculation// (n*t) n = amount of times done // t = time period

#needs to reinvest into staking variable?


min_compound_interest = staking * ((1 + (min_reward/num_of_compound))**(num_of_compound*time_conversion))
min_compound_interest = (min_reward + staking) * num_of_compound
try:
    max_compound_interest = staking * ((1 + (max_reward/num_of_compound))**(num_of_compound*time_conversion))
except:
    pass
min_compound_interest_USD = price * min_compound_interest
try:
    max_compound_interest_USD = price * max_compound_interest
except:
    pass
symbol_upper = symbol.upper()
coin_capitalize = coin.capitalize()
staking_USD = price * staking
min_USD_gains = min_compound_interest_USD + staking_USD
try:
    max_USD_gains = max_compound_interest_USD + staking_USD
except:
    pass
min_reward_percent = "{:.2f}".format(min_reward*100) + "%"
try:
    max_reward_percent = "{:.2f}".format(max_reward*100) + "%"
except:
    pass
try:
    print('Coin: ', coin_capitalize, "\n"
      'Symbol: ', symbol_upper, '\n'
      'Price: ', '${:.2f}'.format(price), '\n'
      'Staking: ', staking, '\n'
      'Staking in USD: ', "${:.2f}".format(staking_USD), '\n'
      'Minimuim Reward: ', min_reward_percent, '\n'
      'Maximuim Reward: ', max_reward_percent, '\n'
      "Minimuim Compound Staking Interest: ", min_compound_interest, symbol_upper, '\n'
      "Maximuim Compound Staking Interest: ", max_compound_interest, symbol_upper, '\n'
      "Min USD interest: ", "${:.2f}".format(min_compound_interest_USD), '\n'
      "Max USD interest: ", "${:.2f}".format(max_compound_interest_USD), '\n'
      "Min USD Gains: ", "${:.2f}".format(min_USD_gains), '\n' 
      "Max USD Gains: ", "${:.2f}".format(max_USD_gains))
except:
    print('Coin: ', coin_capitalize, "\n"
      'Symbol: ', symbol_upper, '\n'
      'Price: ', '${:.2f}'.format(price), '\n'
      'Staking: ', staking, '\n'
      'Staking in USD: ', "${:.2f}".format(staking_USD), '\n'
      'Minimuim Reward: ', min_reward_percent, '\n'
      "Minimuim Compound Staking Interest: ", min_compound_interest, symbol_upper, '\n'
      "Min USD interest: ", "${:.2f}".format(min_compound_interest_USD), '\n'
      "Min USD Gains: ", "${:.2f}".format(min_USD_gains), '\n')
