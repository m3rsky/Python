import os


def read_reviews(dir_path):
    
    reviews = []                                # inicjujemy słownik komentarzy
    words_count = []                            # inicjujemy licznik wyrazów
    sum = 0                                     # inicjujemy sumę wyrazów
    count = 0                                   # inicjujemy licznik plików
    num_files = 1200                            # ilość plików do sprawdzenia

    for filename in os.listdir(dir_path):
        if filename.endswith(".txt"):
            with open(os.path.join(dir_path, filename), "r", encoding="utf-8") as f:
                review = f.read().replace("<br /><br />", " ")
                # print(review)
                review_words = review.split()
                reviews.append(review_words)

                words_count.append(len(review_words))
                for w_count in words_count:
                    sum += int(w_count)

            count += 1 # zwiększamy licznik
        if count == num_files: # warunek kończący pętlę
            print(sum)
            break
    return reviews


pos_reviews = read_reviews("C:\\M03\\data\\aclImdb\\train\\pos")

neg_reviews = read_reviews("C:\\M03\\data\\aclImdb\\train\\neg")

while True:
    comment = input("\nEnter a comment to analyze (or 'q' to quit):\n>>>UserInput: ")

    if comment.lower() == 'q':break

    comment_words = comment.split()


    positive_counts = {}
    negative_counts = {}
    total_counts = {}

    for word in comment_words:
        positive_counts[word] = 0
        negative_counts[word] = 0
        total_counts[word] = 0

    for review in pos_reviews:
        for word in set(review):
            if word in comment_words:
                positive_counts[word] += 1
                total_counts[word] += 1

    for review in neg_reviews:
        for word in set(review):
            if word in comment_words:
                negative_counts[word] += 1
                total_counts[word] += 1

    sentiments = []
    for word in comment_words:
        sentiment = (positive_counts[word] - negative_counts[word]) / total_counts[word] if total_counts[word] != 0 else 0
        sentiments.append(sentiment)

    overall_sentiment = 0
    overall_sentiment = sum(sentiments) / len(sentiments)
    print('\nUserInput: ', comment)
    print('Sentiment: ', round(sentiment, 2), 'Overall: ', round(overall_sentiment, 2))

    if overall_sentiment > 0:
        print("\nThe sentiment of the comment is positive!")
    elif overall_sentiment < 0:
        print("\nThe sentiment of the comment is negative!")
    else:
        print("\nThe sentiment of the comment is neutral.")









"""

Ten kod wykonuje analizę sentymentalną komentarza w oparciu o wcześniej wczytane recenzje z dwóch kategorii: pozytywnej (pos) i negatywnej (neg). Komentarz jest wprowadzany przez użytkownika, a następnie program ocenia, czy jest on pozytywny, negatywny czy neutralny, korzystając z wcześniej zebranych danych.

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