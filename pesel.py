
"""
Zadanie 1 - Weryfikacja numeru PESEL

Opis zadania:
- Użytkownik wprowadza numer PESEL (ciąg 11 znaków, zakładamy, że długość jest poprawna).
- Program sprawdza, czy ostatnia cyfra (cyfra kontrolna) jest prawidłowa.
- Reguła: znaleźć w internecie.
- Jeśli ostatnia cyfra zgadza się z obliczoną wartością, funkcja ma zwrócić 1, w przeciwnym wypadku 0.

Przykładowe wejście:
    "97082123152"
Przykładowe wyjście:
    0

Wymagania:
- Implementacja funkcji `verify_pesel(pesel: str) -> int`.
- Użycie algorytmu weryfikacji opisanej powyżej.
"""


def verify_pesel(pesel: str) -> int:
    """
    Weryfikuje numer PESEL.

    Args:
        pesel (str): Numer PESEL w postaci ciągu 11 znaków.

    Returns:
        int: 1 jeśli numer jest poprawny, 0 jeśli nie.
    """
    # Sprawdzenie czy numer ma 11 cyfr i wszystkie znaki są cyframi
    if len(pesel) != 11 or not pesel.isdigit():
        return 0  # Numer PESEL musi składać się z 11 cyfr

    # Wagi cyfr numeru PESEL
    wagi = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    suma = sum(int(pesel[i]) * wagi[i] for i in range(10))

    # Obliczanie cyfry kontrolnej
    cyfra_kontrolna = (10 - suma % 10) % 10

    # Sprawdzamy, czy cyfra kontrolna zgadza się z ostatnią cyfrą PESEL
    return 1 if cyfra_kontrolna == int(pesel[10]) else 0

# Przykładowe wywołanie:
if __name__ == "__main__":
    try:
        # Pobieranie numeru PESEL od użytkownika
        pesel_input = input("Podaj numer PESEL: ").strip()

        # Sprawdzenie numeru PESEL
        wynik = verify_pesel(pesel_input)

        if wynik == 1:
            print("Numer PESEL jest poprawny.")
        else:
            print("Numer PESEL jest niepoprawny.")
    
    except Exception as e:
        print(f"Wystąpił błąd: {e}")

