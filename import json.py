from babel.numbers import format_currency, get_currency_symbol

# Define a currency value and currency code as inputs
value = 1234.56
currency_code = 'EUR'

# Format the value as currency with the symbol using the currency code
formatted_value = format_currency(value, currency_code, locale='en_US')

# Get the currency symbol associated with the currency code
currency_symbol = get_currency_symbol(currency_code, locale='en_US')

print(formatted_value)    # "€1,234.56"
print(currency_symbol)    # "€"
