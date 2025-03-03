# Python
Python_projects

M03_project_GUI.py
"""

Ten skrypt wykonuje analizę sentymentalną komentarza w oparciu o wcześniej wczytane recenzje z dwóch kategorii: pozytywnej (pos) i negatywnej (neg). Komentarz jest wprowadzany przez użytkownika, a następnie program ocenia, czy jest on pozytywny, negatywny czy neutralny, korzystając z wcześniej zebranych danych.

Oto główne kroki kodu:

1. Funkcja read_reviews(dir_path):

- Ta funkcja przyjmuje ścieżkę do katalogu (dir_path), w którym znajdują się pliki tekstowe recenzji.
- Iteruje przez pliki tekstowe w danym katalogu, wczytuje zawartość każdego pliku, zastępuje fragmenty tekstu (".<br />") i dzieli recenzję na słowa.
- Dodaje listę słów recenzji do listy reviews.
- Funkcja zwraca listę recenzji.

2. Wczytanie recenzji:

- Funkcja read_reviews jest używana do wczytania recenzji z dwóch katalogów: "C:\M03\data\aclImdb\train\pos" (pozytywne recenzje) i "C:\M03\data\aclImdb\train\neg" (negatywne recenzje).

3. Analiza sentymentalna wprowadzonego komentarza:

- Użytkownik jest proszony o wprowadzenie komentarza do analizy.
- Komentarz jest dzielony na słowa.
- Inicjowane są trzy słowniki (positive_counts, negative_counts, total_counts), aby śledzić ilość wystąpień słów w pozytywnych, negatywnych i ogólnie wszystkich recenzjach.
- Iteracja przez recenzje pozytywne (pos_reviews) i negatywne (neg_reviews) oraz zliczanie wystąpień każdego słowa w odpowiednich słownikach.
- Obliczane są sentymenty dla każdego słowa na podstawie różnicy ilości wystąpień słowa w recenzjach pozytywnych i negatywnych.
- Obliczany jest ogólny sentyment komentarza na podstawie średniej ważonej sentymentów poszczególnych słów.
- Wyniki są wyświetlane na ekranie, wraz z informacją, czy komentarz jest pozytywny, negatywny czy neutralny.
- Kod ten używa prostego modelu sentymentalnego, który bazuje na częstości występowania słów w recenzjach pozytywnych i negatywnych. Warto jednak zauważyć, że taka metoda ma swoje ograniczenia i nie uwzględnia kontekstu czy skomplikowanych zależności między słowami. To bardziej demonstracyjny przykład niż zaawansowany model analizy sentymentu.

"""
