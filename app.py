from flask import Flask, request
from calc import stake_calc


app = Flask(__name__)

@app.post("/")
def index():
    # Retrieve form data
    coin = request.form.get('coin')
    #symbol = request.form.get('symbol')
    #price = float(request.form.get('price'))
    currency = request.form.get('currency')
    staking = float(request.form.get('staking')) # p
    min_reward = float(request.form.get('min_reward')) / 100 # r_min
    max_reward = float(request.form.get('max_reward')) / 100 # r_max
    duration_select = int(request.form.get('duration_select')) # t
    num_duration = request.form.get('num_duration')
    time = int(request.form.get('time'))
    time_period_comp = request.form.get('time_period_comp')
    compound = int(request.form.get('compound'))# n
    compound_repitition = request.form.get('compound_repitition')

    
    #coin_data = coin_data(coin, currency)
    stake = stake_calc(coin, currency, staking, min_reward, max_reward, 
                       duration_select, num_duration, time, time_period_comp, compound, 
                       compound_repitition) 

    return str(stake)

# Example of a return
# Coin: Tron
# Price: 0.06 {Symbol}
# Currency: USD
# Amount: 1 {currency}
# Min APY: 3%
# Max APY: 6%
# Duration of Staking: 1 Year
# Compounding: Weekly

# Min Reward: 0.03
# Max Reward: 0.06
# Min Earnings:  1.03 {currency}
# Max Earnings: 1.06 {currency}

    # result = f"Coin: {stake[0]}",
    # f"Price: {price} {symbol}",
    # f"Currency: {commodity} {commodity}",
    # f"Staking: {staking}"
    # f"Amount: {currency} ",
    # f"Min APY: {min_reward:.2%}",
    # f"Max APY: {max_reward:.2%}",
    # f"Duration of Staking: {duration_select} Year",
    # f"Compounding: {'Weekly' if compound == 52 else 'Monthly' if compound == 12 else 'Annually'}",
    # f"Min Earnings: {min_compound_interest_currency}",
    # f"Max Earnings: {max_compound_interest_currency}" #use here

    # Calculate stake
    # stake = stake_calc(
    #     f"Coin: {coin}",
    #     f"Price: {price} {symbol}",
    #     f"Currency: {commodity} {commodity}",
    #     f"Staking: {staking}"
    #     f"Amount: {currency} ",
    #     f"Min APY: {min_reward:.2%}",
    #     f"Max APY: {max_reward:.2%}",
    #     f"Duration of Staking: {duration_select} Year",
    #     f"Compounding: {'Weekly' if compound == 52 else 'Monthly' if compound == 12 else 'Annually'}",
    #     f"Min Earnings: {min_compound_interest_currency}",
    #     f"Max Earnings: {max_compound_interest_currency}"


# from flask import Flask, request
# from calc import stake_calc #import functions from calc.py

# app = Flask(__name__)
#  #a = p*(1 + (r/n))**(n*t)
# @app.post("/")
# def index():
#     coin = request.form.get('coin')
       
#     symbol = request.form.get('symbol')

#     price = request.form.get('price')

#     currency = request.form.get('currency')

#     staking = request.form.get('staking')#p

#     min_reward = request.form.get('min_reward')#r min
 
#     max_reward = request.form.get('max_reward')#r max
 
#     #time_period = request.form.get('W_M_Y')#???

#     duration_select = request.form.get('duration_select')#t

#     compound = request.form.get('compound')#n

#     min_reward = float(f'{min_reward / 100}')

#     max_reward = float(f'{max_reward / 100}')
# #convert from str to types floats int etc
#     magic_number = stake_calc("Coin: " {coin}, "Price: " {price} {symbol}, "Currency: " {currency},
#     Amount: 1 {currency}
# Min APY: 3%
# Max APY: 6%
# Duration of Staking: 1 Year
# Compounding: Weekly

# Min Reward: 0.03
# Max Reward: 0.06) #call function save to var

    
#     return str(magic_number)

# (f'<p>{coin_capitalize}</p>', 
#             price, 
#             staking,
#             min_reward,
#             max_reward,
#             min_compound_interest, 
#             max_compound_interest, 
#             symbol, 
#             currency, 
#             min_compound_interest_USD, 
#             max_compound_interest_USD,
#             compound, 
#             duration_select)

# from flask import Flask, request
# import requests
# from calc import stake_calc

# app = Flask(__name__)

# @app.post("/")
# def calculate_stake():

#     coin_id = request.form['coin']
#     symbol = request.form['symbol']
#     price = float(request.form['price'])
#     currency = request.form['currency']
#     staking_amount = float(request.form['staking'])
#     min_reward_percentage = float(request.form['min_reward'])
#     max_reward_percentage = float(request.form['max_reward'])
#     compound_period = request.form['compound']
#     duration = int(request.form['duration'])
#     duration_unit = request.form['duration_unit']
#     # Convert reward percentages to decimals
#     min_reward = min_reward_percentage / 100
#     max_reward = max_reward_percentage / 100
#     # Get current coin price
#     url = f'https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies={currency}'
#     response = requests.get(url)
#     response_json = response.json()
#     coin_price = response_json[coin_id][currency]
#     # Calculate staked amount after duration
#     staked_amount = stake_calc(
#         coin_id, symbol, currency, price, staking_amount,
#         min_reward, max_reward, compound_period, duration, duration_unit,
#         coin_price
#     )

#     return str(staked_amount)

    # stake_calc(coin)
    # calculateCompoundInterest(coin, contribution, symbol, current price, )
    # must be in calc.py

    # Coin: ', coin_capitalize, "\n"
    #     'Symbol: ', symbol_upper, '\n'
    #     'Price: ', '${:.2f}'.format(price), '\n'
    #     'Staking: ', staking, '\n'
    #     'Staking in USD: ', "${:.2f}".format(staking_USD), '\n'
    #     'Minimuim Reward: ', min_reward_percent, '\n'
    #     'Maximuim Reward: ', max_reward_percent, '\n'
    #     "Minimuim Compound Staking Interest: ", min_compound_interest, symbol_upper, '\n'
    #     "Maximuim Compound Staking Interest: ", max_compound_interest, symbol_upper, '\n'
    #     "Min USD interest: ", "${:.2f}".format(min_compound_interest_USD), '\n'
    #     "Max USD interest: ", "${:.2f}".format(max_compound_interest_USD), '\n'
    #     "Min USD Gains: ", "${:.2f}".format(min_USD_gains), '\n' 
    #     "Max USD Gains: ", "${:.2f}".format(max_USD_gains)