#Kirjoita peli, jossa tietokone arpoo kokonaisluvun väliltä 1..10.
# Kone arvuuttelee lukua pelaajalta siihen asti, kunnes tämä arvaa oikein.
# Kunkin arvauksen jälkeen ohjelma tulostaa tekstin Liian suuri arvaus, Liian pieni arvaus tai Oikein.
# Huomaa, että tietokone ei saa vaihtaa lukuaan arvauskertojen välissä.

import random
luku = random.randint(1,10)
Arvaus = 0

while True:
    arvaus_str = input("Arvaa luku 1 ja 10 välillä: ")
    try: arvaus = float(arvaus_str) and arvaus > 10 and
    except ValueError:
        "Anna "