from babel.numbers import format_currency, get_currency_symbol
import json
import requests
import re

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
            print(f"Coin '{coin}' not found.")
      
      url_data = f'https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies={currency}' 
      response = requests.get(url_data)
      data = json.loads(response.text)
      price = data[coin][currency.lower()]
      
      # Convert the duration t
      if time_period_comp == "W":
          time = time / 52
      elif time_period_comp == "M":
          time = time / 30
      elif time_period_comp == "Y":
          time = time * 1
      
      #find n
      if compound_repitition == 'D':
            compound = 365 * compound
      elif compound_repitition == 'W':
            compound = 52 * compound
      elif compound_repitition == 'M':
            compound = 12 * compound
      elif compound_repitition == 'Y':
            compound = 1 * compound
      elif compound_repitition == 'Q':
            compound = 0.25 * compound
      elif compound_repitition == 'B':
            compound = 0.5 * compound
      
      
      min_compound_interest = staking * ((1 + (min_reward/compound))**(compound*time))
      max_compound_interest = staking * ((1 + (max_reward/compound))**(compound*time))
      min_compound_interest_currency = price * min_compound_interest
      max_compound_interest_currency = price * max_compound_interest
      min_earnings_currency = min_compound_interest_currency + price
      max_earnings_currency = max_compound_interest_currency + price
      min_earnings_coin = min_compound_interest - staking
      max_earnings_coin = max_compound_interest - staking
      

      def replace_currency_symbols_and_spaces(input_string):
          # Define a regular expression to match currency symbols and the non-breaking space character
          pattern = r'[\$\€\£\¥\₹\₽\s\u00A0]+'
          # Replace the matched pattern with a space
          output_string = re.sub(pattern, ' ', input_string)
          return output_string


      currency_to_locale = {'USD': 'en_US', 'EUR': 'de_DE', 'GBP': 'en_GB', 'AFN': 'ps_AF',
      'ALL': 'sq_AL', 'DZD': 'ar_DZ', 'AOA': 'pt_AO', 'ARS': 'es_AR', 'AMD': 'hy_AM',
      'AWG': 'nl_AW', 'AUD': 'en_AU', 'AZN': 'az_Latn_AZ', 'BSD': 'en_BS',
      'BHD': 'ar_BH', 'BDT': 'bn_BD', 'BBD': 'en_BB', 'BYR': 'be_BY',
      'BEF': 'fr_BE', 'BZD': 'en_BZ', 'BMD': 'en_BM', 'BTN': 'dz_BT',
      'BOB': 'es_BO', 'BAM': 'bs_Latn_BA', 'BWP': 'en_BW', 'BRL': 'pt_BR',
      'BND': 'ms_BN', 'BGN': 'bg_BG', 'BIF': 'fr_BI', 'KHR': 'km_KH',
      'CAD': 'en_CA', 'CVE': 'pt_CV', 'KYD': 'en_KY', 'XOF': 'fr_XOF',
      'XAF': 'fr_XAF', 'XPF': 'fr_XPF', 'CLP': 'es_CL', 'CNY': 'zh_CN',
      'COP': 'es_CO', 'KMF': 'fr_KM', 'CDF': 'fr_CD', 'CRC': 'es_CR',
      'HRK': 'hr_HR', 'CUC': 'es_CU', 'CZK': 'cs_CZ', 'DKK': 'da_DK',
      'DJF': 'fr_DJ', 'DOP': 'es_DO', 'XCD': 'en_XC', 'EGP': 'ar_EG',
      'ERN': 'ti_ER', 'EEK': 'et_EE', 'ETB': 'am_ET', 'FKP': 'en_FK',
      'FJD': 'en_FJ', 'GMD': 'en_GM', 'GEL': 'ka_GE', 'DEM': 'de_DE', 
      'GHS': 'ak_GH', 'GIP': 'en_GI', 'GRD': 'el_GR'} 

      format_var = [price, min_compound_interest_currency, max_compound_interest_currency, 
                    min_earnings_currency, max_earnings_currency]
      
      formatted_var = []
      for var in format_var:
            if isinstance(var, str):
                  var = var.upper()
            elif isinstance(var, (int, float)):
                        currency = currency.upper()
                        #currency_symbol = get_currency_symbol(currency_code, locale='en_US')
                        #currency_symbol = get_currency_symbol(currency, locale='en_US')
                        # Get the currency symbol associated with the currency code
                        #formatted_var.append(format_currency(var, currency, locale='en_US', format=f'{currency_symbol} #,##0.00'))
                        print(currency_to_locale[currency])
                        #print(locale_currency)
                        formatted_var.append(format_currency(var, currency=currency, locale=currency_to_locale[currency]))
      
      coin = coin.capitalize()
      symbol = symbol.upper()
      return {'coin': coin, 'symbol': symbol, 'price': formatted_var[0], 'currency': currency, 
         'staking': [staking, symbol],
         'min_reward': [min_reward, symbol], 'max_reward': [max_reward, symbol], 'time':time, 
         'time_period_comp': time_period_comp, 
         'compound': compound, 'compound_repitition': compound_repitition, 
         'min_compound_interest': [min_compound_interest, symbol],
         'max_compound_interest': [max_compound_interest, symbol],
         'min_compound_interest_currency' : formatted_var[1],
         'max_compound_interest_currency' : formatted_var[2],
         'min_earnings_currency' : formatted_var[3], 'max_earnings_currency' : formatted_var[4],
         'min_earnings_coin':min_earnings_coin, 'max_earnings_coin': max_earnings_coin}

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