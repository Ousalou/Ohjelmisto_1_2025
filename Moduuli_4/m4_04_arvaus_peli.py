#Kirjoita peli, jossa tietokone arpoo kokonaisluvun väliltä 1..10.
# Kone arvuuttelee lukua pelaajalta siihen asti, kunnes tämä arvaa oikein.
# Kunkin arvauksen jälkeen ohjelma tulostaa tekstin Liian suuri arvaus, Liian pieni arvaus tai Oikein.
# Huomaa, että tietokone ei saa vaihtaa lukuaan arvauskertojen välissä.

import random
luku = random.randint(1,10)
arvaus = float()

while True:
    arvaus_str = input("Arvaa luku 1 ja 10 välillä: ")
    try: arvaus = float(arvaus_str)
    except ValueError:
        print("Ei kelvollinen luku. Anna luku väliltä 1-10.")
#Miksi ohjelma menee tässä heti seuraavaan if-lauseeseen? Tässä kohtaa pitäisi loopata alkuun.

    if arvaus > 10 or arvaus < 1:
        print("Ei kelvollinen luku. Anna luku väliltä 1-10.")
    elif arvaus == luku:
        print("Arvasit luvun oikein!")
        break
    elif arvaus > luku:
        print("Liian suuri arvaus, arvaa uudelleen!")
    else: print("Liian pieni arvaus, arvaa uudelleen!")