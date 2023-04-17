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


def test_stake_calc(coin, symbol, currency):
    return 42

def stake_calc(coin, symbol, currency, time_period, price, staking, min_reward, max_reward, ):
    #replace input lines and place in arguments
    # coin = input("Enter name of the coin: ")
    # symbol = input("Enter coin Symbol: ")
    # currency = input('Enter Currency: ')
    url = f'https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies={currency}'#input('Enter - ') #ask for url
    response = requests.get(url)
    print('response.text: ', response.text)
    data = json.loads(response.text)
    print('data: ', data)
    price = data[coin][currency]
    print(coin, price)
    #url_symbol = f'https://api.coingecko.com/api/v3/coins/list'

#     price_input = float(input("Enter current price of coin USD: "))
#     price = float(price_input)
#    try:
# staking = float(input("Enter how many coins are being staked: "))
#    except:
#        staking = int(input("Enter how many coins are being staked: "))    
#    min_reward_input = float(input("Enter minimuim reward percentage, e.g. 12: "))
#    # fstring converts to percentage
#    min_reward = float(f'{min_reward_input / 100}')


    def max_reward(max):
        if max == 'None' or 'none' or 0:
            return None
        else:
            return max

    # max = input(
    #     "Enter maximuim reward percentage (If there is only one, simply write 'none'): ")
    # try: #Should there not be a max percentage, the program will pass over
    #     max_reward = float(max) / 100
    # except:
    #     pass
    #print("Enter time period you would like to compound")
    #time_period = input("Enter either Y M W: ")
    #a = p*(1 + (r/n))**(n*t)
    # def convert_time_period(time_period):  # t in the equation // amount of times in a period
    #     #Choose a time period
    #     if time_period.upper() == 'Y':
    #         years = int(input("Enter amount of years: "))
    #         time_period = int(years)
    #     elif time_period.upper() == 'M':
    #         months = int(input("Enter amount of months: "))
    #         time_period = int(months)  # find for different months
    #     elif time_period.upper() == 'W':
    #         weeks = int(input("Enter amount of weeks: "))
    #         time_period = int(weeks)
    #     else:
    #         print("Not a valid time period.")
    #         quit()
    #     return time_period

    # time_conversion = int(convert_time_period(time_period))
    # #a = p*(1 + (r/n))**(n*t)
    # print("Enter number of times interest is compounded: ") #find n - number of times the compound will be invested
    # num_times_interest_compounded_n = input(
    #     "Daily 'D' Weekly 'W' Monthly 'M' Yearly 'Y' or any number: ")  # Daily Weekly Monthly Yearly
    # # create flexibility in amount of time to compound (e.g. 2 times a week)
    # def find_num_of_compound(num_times_interest_compounded_n):
    #     if num_times_interest_compounded_n.isnumeric():
    #         return float(num_times_interest_compounded_n)

    #     char = num_times_interest_compounded_n.upper()
    #     if char == 'D' or char == 'DAILY':
    #         return 365 * time_conversion
    #     elif char == 'W' or char == 'WEEKLY':
    #         return 52 * time_conversion
    #     elif char == 'M' or char == 'Monthly':
    #         return 12 * time_conversion
    #     elif char == 'Y' or char == 'Yearly':
    #         return 1 * time_conversion

    # num_of_compound = int(find_num_of_compound(num_times_interest_compounded_n))
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
    #min_compound_interest = (min_reward + staking) * num_of_compound
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

    result = {
        'coin_capitalize': coin_capitalize,
        'symbol': symbol_upper,
        'price': '${:.2f}'.format(price),
        'staking': staking,
        'staking_USD': "${:.2f}".format(staking_USD),
        'min_reward_percent': min_reward_percent,
        "min_compound_interest": min_compound_interest,
        "min_compound_interest_USD" : "${:.2f}".format(min_compound_interest_USD),
        "min_USD_gains": "${:.2f}".format(min_USD_gains)
    }

    if max_compound_interest:
        result['max_compound_interest'] = max_compound_interest
    if max_reward_percent:
        result['max_reward_percent'] = max_reward_percent
    if max_compound_interest_USD:
        result['max_compound_interest_USD'] = max_compound_interest_USD
    if max_USD_gains:
        result['max_USD_gains'] = max_USD_gains
    
    return result

    try:
        return print('Coin: ', coin_capitalize, "\n"
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
        return print('Coin: ', coin_capitalize, "\n"
        'Symbol: ', symbol_upper, '\n'
        'Price: ', '${:.2f}'.format(price), '\n'
        'Staking: ', staking, '\n'
        'Staking in USD: ', "${:.2f}".format(staking_USD), '\n'
        'Minimuim Reward: ', min_reward_percent, '\n'
        "Minimuim Compound Staking Interest: ", min_compound_interest, symbol_upper, '\n'
        "Min USD interest: ", "${:.2f}".format(min_compound_interest_USD), '\n'
        "Min USD Gains: ", "${:.2f}".format(min_USD_gains), '\n')

                    <option value="EUR">EUR - Euro - €</option>
            <option value="GBP">GBP - British Pound Sterling - £</option>
            <option></option>
            <option value="AFN">AFN - Afghan Afghani - ؋</option>
            <option value="ALL">ALL - Albanian Lek - Lek</option>
            <option value="DZD">DZD - Algerian Dinar - دج</option>
            <option value="AOA">AOA - Angolan Kwanza - Kz</option>
            <option value="ARS">ARS - Argentine Peso - $</option>
            <option value="AMD">AMD - Armenian Dram - ֏</option>
            <option value="AWG">AWG - Aruban Florin - ƒ</option>
            <option value="AUD">AUD - Australian Dollar - $</option>
            <option value="AZN">AZN - Azerbaijani Manat - m</option>
            <option value="BSD">BSD - Bahamian Dollar - B$</option>
            <option value="BHD">BHD - Bahraini Dinar - .د.ب</option>
            <option value="BDT">BDT - Bangladeshi Taka - ৳</option>
            <option value="BBD">BBD - Barbadian Dollar - Bds$</option>
            <option value="BYR">BYR - Belarusian Ruble - Br</option>
            <option value="BEF">BEF - Belgian Franc - fr</option>
            <option value="BZD">BZD - Belize Dollar - $</option>
            <option value="BMD">BMD - Bermudan Dollar - $</option>
            <option value="BTN">BTN - Bhutanese Ngultrum - Nu.</option>
            <option value="BOB">BOB - Bolivian Boliviano - Bs.</option>
            <option value="BAM">BAM - Bosnia-Herzegovina Convertible Mark - KM</option>
            <option value="BWP">BWP - Botswanan Pula - P</option>
            <option value="BRL">BRL - Brazilian Real - R$</option>
            <option value="BND">BND - Brunei Dollar - B$</option>
            <option value="BGN">BGN - Bulgarian Lev - Лв.</option>
            <option value="BIF">BIF - Burundian Franc - FBu</option>
            <option value="KHR">KHR - Cambodian Riel - KHR</option>
            <option value="CAD">CAD - Canadian Dollar - $</option>
            <option value="CVE">CVE - Cape Verdean Escudo - $</option>
            <option value="KYD">KYD - Cayman Islands Dollar - $</option>
            <option value="XOF">XOF - CFA Franc BCEAO - CFA</option>
            <option value="XAF">XAF - CFA Franc BEAC - FCFA</option>
            <option value="XPF">XPF - CFP Franc - ₣</option>
            <option value="CLP">CLP - Chilean Peso - $</option>
            <option value="CNY">CNY - Chinese Yuan - ¥</option>
            <option value="COP">COP - Colombian Peso - $</option>
            <option value="KMF">KMF - Comorian Franc - CF</option>
            <option value="CDF">CDF - Congolese Franc - FC</option>
            <option value="CRC">CRC - Costa Rican ColÃ³n - ₡</option>
            <option value="HRK">HRK - Croatian Kuna - kn</option>
            <option value="CUC">CUC - Cuban Convertible Peso - $, CUC</option>
            <option value="CZK">CZK - Czech Republic Koruna - Kč</option>
            <option value="DKK">DKK - Danish Krone - Kr.</option>
            <option value="DJF">DJF - Djiboutian Franc - Fdj</option>
            <option value="DOP">DOP - Dominican Peso - $</option>
            <option value="XCD">XCD - East Caribbean Dollar - $</option>
            <option value="EGP">EGP - Egyptian Pound - ج.م</option>
            <option value="ERN">ERN - Eritrean Nakfa - Nfk</option>
            <option value="EEK">EEK - Estonian Kroon - kr</option>
            <option value="ETB">ETB - Ethiopian Birr - Nkf</option>
            <option value="FKP">FKP - Falkland Islands Pound - £</option>
            <option value="FJD">FJD - Fijian Dollar - FJ$</option>
            <option value="GMD">GMD - Gambian Dalasi - D</option>
            <option value="GEL">GEL - Georgian Lari - ლ</option>
            <option value="DEM">DEM - German Mark - DM</option>
            <option value="GHS">GHS - Ghanaian Cedi - GH₵</option>
            <option value="GIP">GIP - Gibraltar Pound - £</option>
            <option value="GRD">GRD - Greek Drachma - ₯, Δρχ, Δρ</option>
            <option value="GTQ">GTQ - Guatemalan Quetzal - Q</option>
            <option value="GNF">GNF - Guinean Franc - FG</option>
            <option value="GYD">GYD - Guyanaese Dollar - $</option>
            <option value="HTG">HTG - Haitian Gourde - G</option>
            <option value="HNL">HNL - Honduran Lempira - L</option>
            <option value="HKD">HKD - Hong Kong Dollar - $</option>
            <option value="HUF">HUF - Hungarian Forint - Ft</option>
            <option value="ISK">ISK - Icelandic KrÃ³na - kr</option>
            <option value="INR">INR - Indian Rupee - ₹</option>
            <option value="IDR">IDR - Indonesian Rupiah - Rp</option>
            <option value="IRR">IRR - Iranian Rial - ﷼</option>
            <option value="IQD">IQD - Iraqi Dinar - د.ع</option>
            <option value="ILS">ILS - Israeli New Sheqel - ₪</option>
            <option value="ITL">ITL - Italian Lira - L,£</option>
            <option value="JMD">JMD - Jamaican Dollar - J$</option>
            <option value="JPY">JPY - Japanese Yen - ¥</option>
            <option value="JOD">JOD - Jordanian Dinar - ا.د</option>
            <option value="KZT">KZT - Kazakhstani Tenge - лв</option>
            <option value="KES">KES - Kenyan Shilling - KSh</option>
            <option value="KWD">KWD - Kuwaiti Dinar - ك.د</option>
            <option value="KGS">KGS - Kyrgystani Som - лв</option>
            <option value="LAK">LAK - Laotian Kip - ₭</option>
            <option value="LVL">LVL - Latvian Lats - Ls</option>
            <option value="LBP">LBP - Lebanese Pound - £</option>
            <option value="LSL">LSL - Lesotho Loti - L</option>
            <option value="LRD">LRD - Liberian Dollar - $</option>
            <option value="LYD">LYD - Libyan Dinar - د.ل</option>
            <option value="LTL">LTL - Lithuanian Litas - Lt</option>
            <option value="MOP">MOP - Macanese Pataca - $</option>
            <option value="MKD">MKD - Macedonian Denar - ден</option>
            <option value="MGA">MGA - Malagasy Ariary - Ar</option>
            <option value="MWK">MWK - Malawian Kwacha - MK</option>
            <option value="MYR">MYR - Malaysian Ringgit - RM</option>
            <option value="MVR">MVR - Maldivian Rufiyaa - Rf</option>
            <option value="MRO">MRO - Mauritanian Ouguiya - MRU</option>
            <option value="MUR">MUR - Mauritian Rupee - ₨</option>
            <option value="MXN">MXN - Mexican Peso - $</option>
            <option value="MDL">MDL - Moldovan Leu - L</option>
            <option value="MNT">MNT - Mongolian Tugrik - ₮</option>
            <option value="MAD">MAD - Moroccan Dirham - MAD</option>
            <option value="MZM">MZM - Mozambican Metical - MT</option>
            <option value="MMK">MMK - Myanmar Kyat - K</option>
            <option value="NAD">NAD - Namibian Dollar - $</option>
            <option value="NPR">NPR - Nepalese Rupee - ₨</option>
            <option value="ANG">ANG - Netherlands Antillean Guilder - ƒ</option>
            <option value="TWD">TWD - New Taiwan Dollar - $</option>
            <option value="NZD">NZD - New Zealand Dollar - $</option>
            <option value="NIO">NIO - Nicaraguan CÃ³rdoba - C$</option>
            <option value="NGN">NGN - Nigerian Naira - ₦</option>
            <option value="KPW">KPW - North Korean Won - ₩</option>
            <option value="NOK">NOK - Norwegian Krone - kr</option>
            <option value="OMR">OMR - Omani Rial - .ع.ر</option>
            <option value="PKR">PKR - Pakistani Rupee - ₨</option>
            <option value="PAB">PAB - Panamanian Balboa - B/.</option>
            <option value="PGK">PGK - Papua New Guinean Kina - K</option>
            <option value="PYG">PYG - Paraguayan Guarani - ₲</option>
            <option value="PEN">PEN - Peruvian Nuevo Sol - S/.</option>
            <option value="PHP">PHP - Philippine Peso - ₱</option>
            <option value="PLN">PLN - Polish Zloty - zł</option>
            <option value="QAR">QAR - Qatari Rial - ق.ر</option>
            <option value="RON">RON - Romanian Leu - lei</option>
            <option value="RUB">RUB - Russian Ruble - ₽</option>
            <option value="RWF">RWF - Rwandan Franc - FRw</option>
            <option value="SVC">SVC - Salvadoran ColÃ³n - ₡</option>
            <option value="WST">WST - Samoan Tala - SAT</option>
            <option value="SAR">SAR - Saudi Riyal - ﷼</option>
            <option value="RSD">RSD - Serbian Dinar - din</option>
            <option value="SCR">SCR - Seychellois Rupee - SRe</option>
            <option value="SLL">SLL - Sierra Leonean Leone - Le</option>
            <option value="SGD">SGD - Singapore Dollar - $</option>
            <option value="SKK">SKK - Slovak Koruna - Sk</option>
            <option value="SBD">SBD - Solomon Islands Dollar - Si$</option>
            <option value="SOS">SOS - Somali Shilling - Sh.so.</option>
            <option value="ZAR">ZAR - South African Rand - R</option>
            <option value="KRW">KRW - South Korean Won - ₩</option>
            <option value="XDR">XDR - Special Drawing Rights - SDR</option>
            <option value="LKR">LKR - Sri Lankan Rupee - Rs</option>
            <option value="SHP">SHP - St. Helena Pound - £</option>
            <option value="SDG">SDG - Sudanese Pound - .س.ج</option>
            <option value="SRD">SRD - Surinamese Dollar - $</option>
            <option value="SZL">SZL - Swazi Lilangeni - E</option>
            <option value="SEK">SEK - Swedish Krona - kr</option>
            <option value="CHF">CHF - Swiss Franc - CHf</option>
            <option value="SYP">SYP - Syrian Pound - LS</option>
            <option value="STD">STD - São Tomé and Príncipe Dobra - Db</option>
            <option value="TJS">TJS - Tajikistani Somoni - SM</option>
            <option value="TZS">TZS - Tanzanian Shilling - TSh</option>
            <option value="THB">THB - Thai Baht - ฿</option>
            <option value="TOP">TOP - Tongan pa'anga - $</option>
            <option value="TTD">TTD - Trinidad & Tobago Dollar - $</option>
            <option value="TND">TND - Tunisian Dinar - ت.د</option>
            <option value="TRY">TRY - Turkish Lira - ₺</option>
            <option value="TMT">TMT - Turkmenistani Manat - T</option>
            <option value="UGX">UGX - Ugandan Shilling - USh</option>
            <option value="UAH">UAH - Ukrainian Hryvnia - ₴</option>
            <option value="AED">AED - United Arab Emirates Dirham - إ.د</option>
            <option value="UYU">UYU - Uruguayan Peso - $</option>
            <option value="UZS">UZS - Uzbekistan Som - лв</option>
            <option value="VUV">VUV - Vanuatu Vatu - VT</option>
            <option value="VEF">VEF - Venezuelan BolÃ­var - Bs</option>
            <option value="VND">VND - Vietnamese Dong - ₫</option>
            <option value="YER">YER - Yemeni Rial - ﷼</option>
            <option value="ZMK">ZMK - Zambian Kwacha - ZK</option>

def stake_calc(coin, symbol, currency, price, staking, min_reward, max_reward, compound, duration_select):
    url = f'https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies={currency}'
    response = requests.get(url)
    response_json = response.json()
    coin_price = response_json[coin][currency]
    min_reward_decimal = min_reward / 100
    max_reward_decimal = max_reward / 100
    compound_interest_decimal = 1 + (max_reward_decimal - min_reward_decimal) / 2
    duration_in_days = 0
    if duration_select == 'num_weeks':
        duration_in_days = 7 * duration
    elif duration_select == 'num_months':
        duration_in_days = 30 * duration
    elif duration_select == 'num_years':
        duration_in_days = 365 * duration
    stake_value = float(price) * float(staking)
    total_staked_value = stake_value * coin_price
    compound_times_per_year = 0
    if compound == 'D':
        compound_times_per_year = 365
    elif compound == 'W':
        compound_times_per_year = 52
    elif compound == 'M':
        compound_times_per_year = 12
    compound_interest_rate = compound_interest_decimal ** (1 / compound_times_per_year)
    staked_amount_after_duration = total_staked_value * (compound_interest_rate ** (compound_times_per_year * (duration_in_days / 365)))
    return staked_amount_after_duration

def stake_calc(coin, symbol, currency, price, staking, min_reward, max_reward, compound, duration_select, duration=1):
    url = f'https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies={currency}'
    response = requests.get(url)
    response_json = response.json()
    coin_price = response_json[coin][currency]
    min_reward_decimal = min_reward / 100
    max_reward_decimal = max_reward / 100
    compound_interest_decimal = 1 + (max_reward_decimal - min_reward_decimal) / 2
    duration_in_days = 0
    if duration_select == 'num_weeks':
        duration_in_days = 7 * duration
    elif duration_select == 'num_months':
        duration_in_days = 30 * duration
    elif duration_select == 'num_years':
        duration_in_days = 365 * duration
    stake_value = float(price) * float(staking)
    total_staked_value = stake_value * coin_price
    compound_times_per_year = 0
    if compound == 'D':
        compound_times_per_year = 365
    elif compound == 'W':
        compound_times_per_year = 52
    elif compound == 'M':
        compound_times_per_year = 12
    compound_interest_rate = compound_interest_decimal ** (1 / compound_times_per_year)
    staked_amount_after_duration = total_staked_value * (compound_interest_rate ** (compound_times_per_year * (duration_in_days / 365)))
    return staked_amount_after_duration