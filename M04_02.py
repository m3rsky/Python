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


def get_user_input(prompt):
    while True:
        input_txt = input(prompt)
        parts = input_txt.split()
        if len(parts) != 2:
            print("Nieprawidłowy format wejścia. Użyj formatu waluta i data")
        else:
            return parts[0], parts[1]


def parse_date(date_str):
    try:
        date = dateutil.parser.parse(date_str).strftime('%Y-%m-%d')
        return date
    except ValueError:
        return None


def get_exchange_rate(currency, date_str):
    date = parse_date(date_str)
    if date is None:
        print("Nieprawidłowy format daty!")
        currency, date_str = get_user_input(f'Podaj poprawny format daty (np. {currency} 2023-12-20):\n')
        date = parse_date(date_str)
        if date is None:
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
        currency, date_str = get_user_input('Podaj Walutę i datę. (np. USD 2023-05-05)\n')

    get_exchange_rate(currency, date_str)


if __name__ == "__main__":
    main()
