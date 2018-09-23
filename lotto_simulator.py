from random import randint, shuffle


def get_random():
    rand = [r for r in range(1, 50)]
    shuffle(rand)
    return rand[:6]


def get_numbers():
    while True:
        numbers = input("Podaj 6 liczb oddzielonych spacją: ")
        numbers = numbers.split()
        try:
            numbers = [int(n) for n in numbers]
        except (TypeError, ValueError):
            print("Nieprawidłowe liczby!")
            continue
        if len(numbers) != 6:
            print("Należy podać 6 liczb!")
            continue
        for n in numbers:
            if numbers.count(n) > 1:
                print("Liczby nie mogą się powtarzać!")
                break
            elif n not in range(1, 50):
                print("Liczba spoza zakresu 1\u201449")
                break
        else:
            return(numbers)
        continue


def lotto():
    user_numbers = get_numbers()
    rand_numbers = get_random()
    strike = len([1 for n in user_numbers if n in rand_numbers])

    user_numbers.sort()
    user_numbers = [str(n) for n in user_numbers]
    print("Skreślone liczby:", " ".join(user_numbers))

    rand_numbers.sort()
    rand_numbers = [str(r) for r in rand_numbers]
    print("Wylosowane liczby:", " ".join(rand_numbers))

    if strike > 2:
        print("Trafiłeś ", strike)
    else:
        print("Nie trafiłeś nawet \"trójki\".")


lotto()
