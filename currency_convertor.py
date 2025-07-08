# import requests
# response = requests.get('https://api.freecurrencyapi.com/v1/latest?apikey=fca_live_xy9J3MlXHiCHuUWSTwKYvrAnrbRXJwMxuIbaZPJK')
# data = response.json()




# COMMAND-LINE ARGUMENT VERSION
# """
# py currency_convertor.py FROM to TO VALUE
# example: USD to TRY 15.3
# """
# import sys

# currencies = {'AUD': 1.5413801912, 
#               'AZN': 1.7,
#               'BGN': 1.8076801868, 
#               'BRL': 5.055120531, 
#               'CAD': 1.357240232, 
#               'CHF': 0.9050301382, 
#               'CNY': 7.2286510038, 
#               'CZK': 23.5470443465, 
#               'DKK': 6.9461410996, 
#               'EUR': 0.9311701753, 
#               'GBP': 0.7970401019, 
#               'HKD': 7.8235515093, 
#               'HRK': 6.7472911041, 
#               'HUF': 367.0530030818, 
#               'IDR': 15868.093842386, 
#               'ILS': 3.6844104643, 
#               'INR': 83.3252404706, 
#               'ISK': 140.0749357622, 
#               'JPY': 151.5817479605, 
#               'KRW': 1351.7715737989, 
#               'MXN': 16.6114927538, 
#               'MYR': 4.7240807764, 
#               'NOK': 10.9603513218, 
#               'NZD': 1.6799402664, 
#               'PHP': 56.249876704, 
#               'PLN': 3.9980607319, 
#               'RON': 4.628760899, 
#               'RUB': 92.2735534207, 
#               'SEK': 10.7983915331, 
#               'SGD': 1.3525401583, 
#               'THB': 36.5871048698, 
#               'TRY': 32.1970360414, 
#               'USD': 1, 
#               'ZAR': 18.9456830987}


# FROM, TO, VALUE = sys.argv[1], sys.argv[3], sys.argv[4]

# print(f'{VALUE} {FROM} = {round((int(VALUE)/currencies[FROM.upper()]*currencies[TO.upper()]), 2)} {TO}')





# APPLICATION VERSION
currencies = {'AUD': 1.5413801912, 
              'AZN': 1.7,
              'BGN': 1.8076801868, 
              'BRL': 5.055120531, 
              'CAD': 1.357240232, 
              'CHF': 0.9050301382, 
              'CNY': 7.2286510038, 
              'CZK': 23.5470443465, 
              'DKK': 6.9461410996, 
              'EUR': 0.9311701753, 
              'GBP': 0.7970401019, 
              'HKD': 7.8235515093, 
              'HRK': 6.7472911041, 
              'HUF': 367.0530030818, 
              'IDR': 15868.093842386, 
              'ILS': 3.6844104643, 
              'INR': 83.3252404706, 
              'ISK': 140.0749357622, 
              'JPY': 151.5817479605, 
              'KRW': 1351.7715737989, 
              'MXN': 16.6114927538, 
              'MYR': 4.7240807764, 
              'NOK': 10.9603513218, 
              'NZD': 1.6799402664, 
              'PHP': 56.249876704, 
              'PLN': 3.9980607319, 
              'RON': 4.628760899, 
              'RUB': 92.2735534207, 
              'SEK': 10.7983915331, 
              'SGD': 1.3525401583, 
              'THB': 36.5871048698, 
              'TRY': 32.1970360414, 
              'USD': 1, 
              'ZAR': 18.9456830987}

print('\nFROM to TO VALUE\nexample: USD to TRY 15.3\n')

while True:
    try:
        FROM, _,TO, VALUE = input('Convert: ').split(' ')
    except ValueError:
        print("Invalid input. Please enter in the format: 'FROM to TO VALUE'")
        continue

    print(f'{VALUE} {FROM} = {round((int(VALUE)/currencies[FROM.upper()]*currencies[TO.upper()]), 2)} {TO}')