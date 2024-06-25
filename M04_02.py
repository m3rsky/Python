'''
Importowanie modułów

requests do wykonywania zapytań HTTP do API.
sys do obsługi argumentów wiersza poleceń.
dateutil.parser do parsowania dat w różnych formatach.

'''

import requests
import sys
import dateutil.parser


# 'get_currency_value' Pobiera kurs wymiany waluty z API NBP.
def get_currency_value(currency, date):
    """
    Pobiera kurs wymiany waluty z API Narodowego Banku Polskiego (NBP) dla podanej waluty i daty.

    Args:
        currency (str): Kod waluty w formacie trzyliterowym (np. 'USD' dla dolara amerykańskiego).
        date (str): Data w formacie 'YYYY-MM-DD'.

    Returns:
        float: Kurs wymiany waluty w formacie liczby zmiennoprzecinkowej.
        None: Jeśli nie uda się pobrać danych z API.

    Example:
        exchange_rate = get_currency_value('USD', '2023-12-20')
        if exchange_rate is not None:
            print(f'Kurs USD z dnia 2023-12-20 to: {exchange_rate}')
        else:
            print("Błąd przy pobieraniu danych z API NBP!")
    """
    url = f'https://api.nbp.pl/api/exchangerates/rates/a/{currency}/{date}/?format=json'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        exchange = data['rates'][0]['mid']
        return exchange
    else:
        return None


# 'get_user_input' Pobiera dane od użytkownika w formacie waluta data.
def get_user_input(prompt):
    """
    Pobiera dane od użytkownika w formacie waluta data.

    Args:
        prompt (str): Tekst wyświetlany użytkownikowi jako instrukcja.

    Returns:
        tuple: Krotka zawierająca dwa elementy: waluta (str) i data (str).

    Example:
        currency, date_str = get_user_input('Podaj Walutę i datę (np. USD 2023-12-20):\n')
    """
    while True:
        input_txt = input(prompt)
        parts = input_txt.split()
        if len(parts) != 2:
            print("Nieprawidłowy format wejścia. Użyj formatu waluta i data")
        else:
            return parts[0], parts[1]


# 'parse_date' Parsuje podaną datę do formatu YYYY-MM-DD.
def parse_date(date_str):
    """
    Parsuje podaną datę do formatu 'YYYY-MM-DD'.

    Args:
        date_str (str): Data w formacie tekstowym.

    Returns:
        str: Data w formacie 'YYYY-MM-DD'.
        None: Jeśli format daty jest nieprawidłowy.

    Example:
        date = parse_date('2023-12-20')
        if date is not None:
            print(f'Przekonwertowana data: {date}')
        else:
            print("Nieprawidłowy format daty!")
    """
    try:
        date = dateutil.parser.parse(date_str).strftime('%Y-%m-%d')
        return date
    except ValueError:
        return None


# 'get_exchange_rate' Sprawdza i przetwarza datę, a następnie pobiera kurs waluty.
def get_exchange_rate(currency, date_str):
    """
    Sprawdza poprawność formatu daty i pobiera kurs wymiany waluty.

    Args:
        currency (str): Kod waluty w formacie trzyliterowym.
        date_str (str): Data w formacie tekstowym.

    Returns:
        None
    """
    date = parse_date(date_str)
    if date is None:
        print("Nieprawidłowy format daty!")
        while date is None:
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
    """
    Główna funkcja programu, która obsługuje argumenty wiersza poleceń i wywołuje odpowiednie funkcje.

    Returns:
        None
    """
    try:
        currency = sys.argv[1]
        date_str = sys.argv[2]
    except IndexError:
        currency, date_str = get_user_input('Podaj Walutę i datę. (np. USD 2023-05-05)\n')

    get_exchange_rate(currency, date_str)


if __name__ == "__main__":
    main()
