#Currency Converter System
#Take amount as string input
#Convert into float
#Apply exchange rate
#Use round() for precision
#Print:
#original amount
#rate
#converted amount

string_currency = "1000"
# convert string to float
string_currency = float(string_currency)
exchange_rate = 0.011  # Example exchange rate from Rupees to USD
converted_amount = round(string_currency * exchange_rate,2)
print(f"Original amount: {string_currency} Rupees")
print(f"Exchange rate: {exchange_rate} USD/Rupee")
print(f"Converted amount: {converted_amount} USD")



