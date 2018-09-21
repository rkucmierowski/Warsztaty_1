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
            print("Zgadłeś")
            flag = False


guess_number()
