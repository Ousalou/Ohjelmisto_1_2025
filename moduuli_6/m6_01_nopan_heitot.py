#Kirjoita parametriton funktio, joka palauttaa paluuarvonaan satunnaisen nopan silmäluvun väliltä 1..6.
# Kirjoita pääohjelma, joka heittää noppaa niin kauan kunnes tulee kuutonen.
# Pääohjelma tulostaa kunkin heiton jälkeen saadun silmäluvun.

import random

def nopan_heitto ():
    tulos = random.randint(1,6)
    return tulos

while True:
    tulos = nopan_heitto()
    print(f"Heitetään noppaa: {tulos}")
    if tulos == 6:
        break

