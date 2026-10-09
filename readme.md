# Symulator ruletki

Interaktywny symulator europejskiej ruletki napisany w Pythonie. Program pozwala obstawiać kolor pola, losuje wynik od 0 do 36 i na bieżąco aktualizuje stan konta gracza.

## Funkcje

- europejska ruletka z polami od 0 do 36
- zakłady na kolor czerwony, czarny lub zielony
- animacja kręcenia kołem
- walidacja wybranego koloru i wysokości stawki
- początkowy bankroll w wysokości 1000 zł
- możliwość zakończenia gry w dowolnym momencie

## Wymagania

- Python 3.8 lub nowszy
- Jupyter Notebook albo Visual Studio Code z rozszerzeniem Jupyter

Projekt korzysta wyłącznie ze standardowych bibliotek Pythona (`random` i `time`), dlatego nie wymaga instalowania dodatkowych pakietów.

## Uruchomienie

1. Otwórz plik `fajnyplik.ipynb` w Jupyter Notebook lub Visual Studio Code.
2. Uruchom komórkę zawierającą kod programu.
3. Postępuj zgodnie z instrukcjami wyświetlanymi w konsoli.

Program można również uruchomić po zapisaniu kodu jako pliku Python:

```bash
python fajnyplik.py
```

## Zasady gry

W każdej rundzie wybierz:

| Skrót | Zakład |
|---|---|
| `c` | czerwony |
| `cz` | czarny |
| `z` | zielony, czyli liczba 0 |
| `q` | zakończenie gry |

Zakład na czerwony lub czarny wypłaca dwukrotność stawki. Trafienie zielonego pola wypłaca czternastokrotność stawki. Przegrana pomniejsza konto o wysokość zakładu.

Gra kończy się po wpisaniu `q` albo po utracie całego bankrolla.

## Uwaga

Projekt ma charakter edukacyjny i rozrywkowy. Wynik każdej rundy jest losowany pseudolosowo i nie stanowi podstawy do przewidywania wyników prawdziwej ruletki.