#Muokkaa edellistä funktiota siten,
# että funktio saa parametrinaan nopan tahkojen yhteismäärän.
# Muokatun funktion avulla voit heitellä esimerkiksi 21-tahkoista roolipelinoppaa.
# Edellisestä tehtävästä poiketen
# nopan heittelyä jatketaan pääohjelmassa kunnes saadaan nopan maksimisilmäluku,
# joka kysytään käyttäjältä ohjelman suorituksen alussa.

import random

def nopan_heitto (noppa):
    tulos = random.randint(1,noppa)
    return tulos

noppa = int(input("Monta tahkoa nopassa on? "))

while True:
    tulos = nopan_heitto(noppa)
    print(f"Heitetään noppaa: {tulos}")
    if tulos == noppa:
        break
