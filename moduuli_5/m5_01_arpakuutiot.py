# Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän.
# Ohjelma heittää kerran kaikkia arpakuutioita ja tulostaa silmälukujen summan.
# Käytä for-toistorakennetta.

import random
from operator import index

silma_luvut = []

nopat = int(input("Monta noppaa heitetään? "))

for i in range(nopat):
    luku = random.randint(1,6)
    silma_luvut.append(luku)

for i in silma_luvut:
        print(f"Heitetään noppaa: {i}")

print(f"Lukujen summa on: {sum(silma_luvut)}")






