import requests
import sys
import dateutil.parser
from datetime import datetime


def get_currency_value(currency, date):
    url = f'https://api.nbp.pl/api/exchangerates/rates/a/{currency}/{date}/?format=json'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        exchange = data['rates'][0]['mid']
        return exchange
    else:
        return None
    

def get_user_input(text):
    while True:
        input_txt = input(text)
        parts = input_txt.split()
        if len(parts) != 2:
            print("Nieprawidłowy format wejścia. Użyj formatu waluta i data\nprzykład:\nUSD 2023-12-20\n")
        else:
            return parts[0], parts[1]


def get_current_date():
    return datetime.now().strftime('%Y-%m-%d')


def get_exchange_rate(currency, date_str):
    while True:
        try:
            date = dateutil.parser.parse(date_str).strftime('%Y-%m-%d')
            break
        except ValueError:
            print("Nieprawidłowy format daty!")
            user_output = get_user_input(f'Podaj poprawny format daty (np. {currency} 2023-12-20):\n>')
            currency, date_str = user_output
            try:
                date = dateutil.parser.parse(date_str).strftime('%Y-%m-%d')
            except ValueError:
                print("Ponownie nieprawidłowy format daty. Zakończenie programu.")
                sys.exit(1)

    exchange_rate = get_currency_value(currency, date)

    if exchange_rate is not None:
        print(f'Kurs {currency.upper()} z dnia: {date} to: {exchange_rate}')
    else:
        print("Błąd przy pobieraniu danych z API NBP!")


def main():

    try:
        currency = sys.argv[1]
        date_str = sys.argv[2]
    except IndexError:
        user_output = get_user_input('Podaj Walutę i datę. (np. USD 2023-05-05)\n>')
        currency, date_str = user_output

    get_exchange_rate(currency, date_str)


if __name__ == "__main__":
    main()