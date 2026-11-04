def add_task(lista_zadan):
    zadanie = input("Podaj treść zadania: ").strip().lower()
    
    if zadanie:
        lista_zadan.append(zadanie)
        print(f"Zadanie '{zadanie}' zostało dodane do listy.")
    else:
        print("Zadanie nie może być puste")