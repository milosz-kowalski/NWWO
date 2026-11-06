# Zasady Współpracy
Dokument opisuje zasady współpracy przy projekcie, aby zapewnić spójność, wysoką jakość kodu oraz efektywną komunikację w zespole. Prosimy o zapoznanie się z poniższymi wytycznymi przed rozpoczęciem pracy

## Przygotowanie projektu
- Upewnij się, że masz zainstalowane wszystkie wymagane narzędzia opisane w README
- Wykonaj git clone repozytorium oraz git pull, aby pracować na najnowszej wersji
- Zainstaluj zależności
- Uruchom testy lokalnie, aby upewnić się, że środowisko działa poprawnie
- Przed rozpoczęciem pracy zapoznaj się z architekturą projektu i konwencjami kodu
1. Sklonuj repo na swój komputer
```bash
git clone https://github.com/USER/REPO.git
```

2. Przejdź do katalogu projektu
```bash
cd REPO
```
3. Utwórz wirtualne środowisko
```bash
python -m venv .venv
```

4. Aktywuj środowisko i zainstaluj zależności, jeżeli projekt zawiera plik requirments.txt
```bash
..venv\Scripts\Activate.ps1
pip install -r requirments.txt
```

## Praca z gałęźiami
- **NIE WPROWADZAJ** zmian bezpośrednio na gałęzi *main*
- Do każdego zadania utwórz osobną gałąź
- Stosuj czytelne nazwy gałęzi:
  - feature\add-task - nowa funkcjonalność
  - docs/update-readme - zmiany w dokumentacji
- Główna gałąź: **main** — stabilna, zawsze działająca wersja projektu

## Zasady pisania kodu
- Stosuj jednolity styl kodu (formatowanie, nazewnictwo, struktura plików).
- Używaj lintera i formattera (np. ESLint, Prettier, Black, Flake8).
- Kod powinien być czytelny i zrozumiały — komentarze tylko tam, gdzie to konieczne.
- Funkcje powinny być krótkie i robić jedną rzecz.
- Unikaj duplikacji kodu — stosuj DRY.
- Dodawaj testy jednostkowe do nowych funkcji.
- Każda zmiana powinna być możliwa do prześledzenia i zrozumienia przez innych.
- nie pisz kodu na zapas
- **przed wysłaniem zmian sprawdź, czy program działa poprawnie**

## Commity
- Commity powinny być krótkie, konkretne i opisowe.
- Unikaj commitów typu „poprawki”, „update”, „zmiany” — nie mówią nic o zawartości
- Jeden commit = jedna logiczna zmiana
```bash
git commit -m"feat: dodaj zadanie..."
git commit -m"fix: popraw element input"
git commit -m"docs: zaktualizuj readme.md"
```

## Zgłoszenia (Issues)
Przed utworzeniem zgłoszenia sprawdź, czy podobne już istnieje.

Każde zgłoszenie powinno zawierać:
- jasny tytuł,
- opis problemu lub propozycji,
- kroki do odtworzenia (jeśli to bug),
- oczekiwane zachowanie,
- zrzuty ekranu lub logi (jeśli dostępne),
- priorytet lub wpływ na projekt.

**Issues** służą do:
- zgłaszania błędów,
- proponowania funkcji,
- dyskusji technicznych,
- planowania zadań.

## Pull Requests


## Komunikacja w zespole
- Komunikujemy się jasno, rzeczowo i z szacunkiem.
- Używamy ustalonych kanałów (Teams).
- Zgłaszamy problemy wcześnie — nie czekamy do ostatniej chwili.
- Informujemy o postępach prac i blokadach.
- W dyskusjach technicznych argumentujemy merytorycznie, nie personalnie.
- Współpracujemy — celem jest jakość projektu, nie wygranie dyskusji.

**Dziękujemy za współpracę i wkład w rozwój projektu!**
