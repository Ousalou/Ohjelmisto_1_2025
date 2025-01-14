# Kirjoita ohjelma, joka kysyy kolme kokonaislukua.
# Ohjelma tulostaa lukujen summan, tulon ja keskiarvon.

luku1 = int(input("Luku 1: "))
luku2 = int(input("Luku 2: "))
luku3 = int(input("Luku 3: "))
summa = luku1 + luku2 + luku3
tulo = luku1 * luku2 * luku3
keskiarvo = float(summa / 3)

print(f"Lukujen summa on {summa}, tulo {tulo} ja keskiarvo {keskiarvo:.2f}.")

#huom. kokonaislukujenkin keskiarvo (jako) on float ja .2f ettei tule metrilukua :D