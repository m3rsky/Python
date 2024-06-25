import requests
import sys
import dateutil.parser


def get_currency(currency, date):

    url = f'https://api.nbp.pl/api/exchangerates/rates/a/{currency}/{date}/?format=json'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        kurs = data['rates'][0]['mid']
        return kurs
    else:
        return None
    

def user_input(text):
    input_txt = input(text)
    currency = input_txt.split()[0]
    date = input_txt.split()[1]
    return currency, date


try:
    currency = sys.argv[1]
    date = sys.argv[2]

    try:
        date = dateutil.parser.parse(date)

        exchange_rate = get_currency(currency, date)

        if exchange_rate is not None:
            print(f'Kurs {currency.upper()} z dnia: {date} to: {exchange_rate}')
        else:
            print("Błąd! ")
        
    except ValueError:
        print("Nieprawidłowy format daty!\nSpróbuj np: USD 2023-12-20")
        user_output = user_input('\n>')
        exchange_rate = get_currency(user_output[0], user_output[1])

        if exchange_rate is not None:
            print(f'Kurs {currency.upper()} z dnia: {user_output[1]} to: {exchange_rate}')
        else:
            print("Błąd! ")


except:
    text = 'Podaj Walutę i datę. (np. USD 2023-05-05)\n>'
    user_output = user_input(text)
    exchange_rate = get_currency(user_output[0], user_output[1])

    if exchange_rate is not None:
        print(f'Kurs {currency.upper()} z dnia: {user_output[1]} to: {exchange_rate}')
    else:
        print("Błąd! ")

