from random import randint


def guess_number():
    rand = randint(1, 100)
    flag = True
    while flag:
        number = input("Zgadnij liczbę: ")
        try:
            number = int(number)
        except (ValueError, TypeError):
            print("To nie jest liczba")
            continue
        if number < rand:
            print("Za mało!")
        elif number > rand:
            print("Za dużo!")
        else:
            print("Zgadłeś!")
            flag = False
            while True:
                once_again = input("Czy chcesz zagrać jeszcze raz (T/N)?")
                if once_again in ('T', 't'):
                    guess_number()
                    break
                elif once_again in ('N', 'n'):
                    return False

guess_number()
