from time import sleep


def try_2_cheat():
    print("Pomyśl liczbę od 0 do 1000, a ja ją zgadnę w maximum. 10 próbach")
    sleep(3)
    minimum = 0
    maximum = 1000
    answer = ""
    while answer != "z":
        guess = int((maximum-minimum)/2) + minimum
        print("Zgaduję: ", guess)
        answer = input("Wskaż odpowiedź: m - za mało; d - za dużo; z - zgadłem\n")
        if answer == "z":
            print("Wygrałem!")
        elif answer == "d":
            if (guess - minimum == 1) and (maximum - guess == 1):
                print("Czyżby?")
            else:
                maximum = guess
        elif answer == "m":
            if (guess - minimum == 1) and (maximum - guess == 1):
                print("Czyżby?")
            else:
                minimum = guess
        else:
            print("Nie oszukuj!")


try_2_cheat()
