from babel.numbers import format_currency, get_currency_symbol
import json
import requests
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
import base64

def read_html_file(result_page):
      with open(result_page, 'r') as file:
            html = file.read()
      return html

def stake_calc(coin, currency, staking, min_reward, max_reward, 
               time, time_period_comp, compound, compound_repitition):
      
      url_name_symbol = 'https://api.coingecko.com/api/v3/coins/list'
      response_name_symbol = requests.get(url_name_symbol)
      data_currency = json.loads(response_name_symbol.text)
      for c in data_currency:
            desired_coin = coin 
            if c['id'] == desired_coin:
                  symbol = c['symbol']
                  break
      else:
            print(f"coin '{coin}' not found.")
      
      url_data = f'https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies={currency}' 
      response_data = requests.get(url_data)
      data = json.loads(response_data.text)
      price = data[coin][currency.lower()]
      
      url_chart = f'https://api.coingecko.com/api/v3/coins/{coin}/market_chart?vs_currency={currency}&days=12'  #add days
      response_chart = requests.get(url_chart)
      data_chart = json.loads(response_chart.content.decode())
      prices = data_chart['prices']
      timestamps = [datetime.utcfromtimestamp(t/1000).strftime('%Y-%m-%d %H:%M:%S') for t, p in prices]

      prices = [price[1] for price in data_chart['prices']]

      fig, ax = plt.subplots()
      ax.plot(timestamps, prices)

      ax.set(xlabel='date', ylabel= f'Price {currency}', title= f'Price History {coin.capitalize()}')
      ax.grid()

      fig.savefig('price_history.png')
      # convert the duration t
      if time_period_comp == "w":
          time = time / 52
      elif time_period_comp == "m":
          time = time / 30
      elif time_period_comp == "y":
          time = time * 1
      
      #find n
      if compound_repitition == 'd':
            compound = 365 * compound
      elif compound_repitition == 'w':
            compound = 52 * compound
      elif compound_repitition == 'm':
            compound = 12 * compound
      elif compound_repitition == 'y':
            compound = 1 * compound
      elif compound_repitition == 'q':
            compound = 0.25 * compound
      elif compound_repitition == 'b':
            compound = 0.5 * compound
    
      min_compound_interest = staking * ((1 + (min_reward/compound))**(compound*time))
      max_compound_interest = staking * ((1 + (max_reward/compound))**(compound*time))
      min_compound_interest_currency = price * min_compound_interest
      max_compound_interest_currency = price * max_compound_interest
      min_earnings_currency = min_compound_interest_currency + price
      max_earnings_currency = max_compound_interest_currency + price
      min_earnings_coin = min_compound_interest - staking
      max_earnings_coin = max_compound_interest - staking

      currency_to_locale = {'USD': 'en_us', 'EUR': 'de_de', 'GBP': 'en_gb', 'AFN': 'ps_af',
      'ALL': 'sq_al', 'DZD': 'ar_dz', 'AOA': 'pt_ao', 'ARS': 'es_ar', 'AMD': 'hy_am',
      'AWG': 'nl_aw', 'AUD': 'en_au', 'AZN': 'az_latn_az', 'BSD': 'en_bs',
      'BHD': 'ar_bh', 'BDT': 'bn_bd', 'BBD': 'en_bb', 'BYR': 'be_by',
      'BEF': 'fr_be', 'BZD': 'en_bz', 'BMD': 'en_bm', 'BTN': 'dz_bt',
      'BOB': 'es_bo', 'BAM': 'bs_latn_ba', 'BWP': 'en_bw', 'BRL': 'pt_br',
      'BND': 'ms_bn', 'BGN': 'bg_bg', 'BIF': 'fr_bi', 'KHR': 'km_kh',
      'CAD': 'en_ca', 'CVE': 'pt_cv', 'KYD': 'en_ky', 'XOF': 'fr_xof',
      'XAF': 'fr_xaf', 'XPF': 'fr_xpf', 'CLP': 'es_cl', 'CNY': 'zh_cn',
      'COP': 'es_co', 'KMF': 'fr_km', 'CDF': 'fr_cd', 'CRC': 'es_cr',
      'HRK': 'hr_hr', 'CUC': 'es_cu', 'CZK': 'cs_cz', 'DKK': 'da_dk',
      'DJF': 'fr_dj', 'DOP': 'es_do', 'XCD': 'en_xc', 'EGP': 'ar_eg',
      'ERN': 'ti_er', 'EEK': 'et_ee', 'ETB': 'am_et', 'FKP': 'en_fk',
      'FJD': 'en_fj', 'GMD': 'en_gm', 'GEL': 'ka_ge', 'DEM': 'de_de', 
      'GHS': 'ak_gh', 'GIP': 'en_gi', 'GRD': 'el_gr'}

      format_var = [price, min_compound_interest_currency, max_compound_interest_currency, 
                    min_earnings_currency, max_earnings_currency]
      
      formatted_var = []
      for var in format_var:
            if isinstance(var, str):
                  var = var.upper()
            elif isinstance(var, (int, float)):
                        currency = currency.upper()
                        formatted_var.append(format_currency(var, currency=currency, locale=currency_to_locale[currency]))
      with open('price_history.png', 'rb') as f:
            img_data = base64.b64encode(f.read()).decode('utf-8')
      coin = coin.capitalize()
      symbol = symbol.upper()
      html_template = '<p><table>' \
             '<tr><th>coin</th><td>{}</td></tr>' \
             '<tr><th>symbol</th><td>{}</td></tr>' \
             '<tr><th>price</th><td>{}</td></tr>' \
             '<tr><th>currency</th><td>{}</td></tr>' \
             '<tr><th>staking</th><td>{} {}</td></tr>' \
             '<tr><th>min reward</th><td>{} {}</td></tr>' \
             '<tr><th>max reward</th><td>{} {}</td></tr>' \
             '<tr><th>time</th><td>{}</td></tr>' \
             '<tr><th>time period comp</th><td>{}</td></tr>' \
             '<tr><th>compound</th><td>{}</td></tr>' \
             '<tr><th>compound repitition</th><td>{}</td></tr>' \
             '<tr><th>min compound interest</th><td>{} {}</td></tr>' \
             '<tr><th>max compound interest</th><td>{} {}</td></tr>' \
             '<tr><th>min compound interest currency</th><td>{}</td></tr>' \
             '<tr><th>max compound interest currency</th><td>{}</td></tr>' \
             '<tr><th>min earnings currency</th><td>{}</td></tr>' \
             '<tr><th>max earnings currency</th><td>{}</td></tr>' \
             '<tr><th>min earnings coin</th><td>{} {}</td></tr>' \
             '<tr><th>max earnings coin</th><td>{} {}</td></tr>' \
      '</table></p>' \
      '<div><img src="data:image/png;base64,{}"</div>'
      final_html = html_template.format(coin, symbol, formatted_var[0], currency, staking, symbol, 
                  min_reward, symbol, max_reward, symbol, time, time_period_comp, 
                  compound, compound_repitition, min_compound_interest, symbol, 
                  max_compound_interest, symbol, formatted_var[1], formatted_var[2], 
                  formatted_var[3], formatted_var[4], min_earnings_coin, symbol, 
                  max_earnings_coin, symbol, img_data) 
      return final_html

      # return {'coin': coin, 'symbol': symbol, 'price': formatted_var[0], 'currency': currency, 
      #    'staking': [staking, symbol],
      #    'min_reward': [min_reward, symbol], 'max_reward': [max_reward, symbol], 'time':time, 
      #    'time_period_comp': time_period_comp, 
      #    'compound': compound, 'compound_repitition': compound_repitition, 
      #    'min_compound_interest': [min_compound_interest, symbol],
      #    'max_compound_interest': [max_compound_interest, symbol],
      #    'min_compound_interest_currency' : formatted_var[1],
      #    'max_compound_interest_currency' : formatted_var[2],
      #    'min_earnings_currency' : formatted_var[3], 'max_earnings_currency' : formatted_var[4],
      #    'min_earnings_coin':min_earnings_coin, 'max_earnings_coin': max_earnings_coin}

# def stake_calc(coin, symbol, price, currency, staking, time, duration,
#                compounding, min_reward, max_reward, time_period):
    
#     url = f'https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies={currency}' 
#     response = requests.get(url)
#     data = json.loads(response.text)
#     price = data[coin][currency]
#        # price = data[coin][currency]
#     print('min_reward',min_reward)
#     print('compounding', compounding)
#     #a = p*(1 + (r/n))**(n*t)
#     print(time)


#     min_compound_interest = staking * ((1 + (min_reward/compounding))**(compounding*time))
#     #min_compound_interest = (min_reward + staking) * num_of_compound

#     max_compound_interest = staking * ((1 + (max_reward/compounding))**(compounding*time))

#     min_compound_interest_currency = price * min_compound_interest

#     max_compound_interest_currency = price * max_compound_interest

#     #symbol_upper = symbol.upper()
#     coin = coin.capitalize()
#     staking_USD = price * staking
#     min_earnings = min_compound_interest_currency + staking_USD

#     max_earnings = max_compound_interest_currency + staking_USD
#     min_APY = "{:.2f}".format(min_reward*100) + "%"
#     max_APY = "{:.2f}".format(max_reward*100) + "%"

#     return {'coin' : coin, 'symbol': symbol, 'price': price, 'currency': currency, 'staking' : staking, 
#             'min_APY' : min_APY, 'max_APY': max_APY, 'time' : time, 'duration': duration,
#                'compounding' : compounding, 'min_reward': min_reward, 'max_reward': max_reward, 
                  # 'min_earnings' : min_earnings, 'max_earnings': max_earnings}

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


# def stake_calc(coin, symbol, currency, price, staking, min_reward, max_reward, compound, duration_select, duration=1):
#     url = f'https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies={currency}'
#     response = requests.get(url)
#     response_json = response.json()
#     coin_price = response_json[coin][currency]
#     min_reward_decimal = min_reward / 100
#     max_reward_decimal = max_reward / 100
#     compound_interest_decimal = 1 + (max_reward_decimal - min_reward_decimal) / 2
#     duration_in_days = 0
#     if duration_select == 'num_weeks':
#         duration_in_days = 7 * duration
#     elif duration_select == 'num_months':
#         duration_in_days = 30 * duration
#     elif duration_select == 'num_years':
#         duration_in_days = 365 * duration
#     stake_value = float(price) * float(staking)
#     total_staked_value = stake_value * coin_price
#     compound_times_per_year = 0
#     if compound == 'D':
#         compound_times_per_year = 365
#     elif compound == 'W':
#         compound_times_per_year = 52
#     elif compound == 'M':
#         compound_times_per_year = 12
#     compound_interest_rate = compound_interest_decimal ** (1 / compound_times_per_year)
#     staked_amount_after_duration = total_staked_value * (compound_interest_rate ** (compound_times_per_year * (duration_in_days / 365)))
#     return staked_amount_after_duration