from random import randint
from unittest import result

narzedzia = ["papier", "kamień", "nożyczki"]
wynik = {("papier", "nożyczki"): "nożyczki", ("papier", "kamień"): "papier", ("kamień", "nożyczki"): "kamień"}

wybor_gracza = input("Papier, kamień czy nożyczki: ")
if wybor_gracza not in narzedzia:
    raise Exception("Nieprawidłowy wybór")

wybor_komputera = narzedzia[randint(0, 2)]
print(wybor_komputera)

if wybor_gracza == wybor_komputera:
    print("Remis")
else:
    for result in wynik:
        if wybor_gracza in result and wybor_komputera in result:
            winner = wynik[result]
            if wybor_gracza == winner:
                print("Wygrana !!")
            else:
                print("Przegrana")
                break
