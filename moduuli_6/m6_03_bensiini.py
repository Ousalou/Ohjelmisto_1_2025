# Kirjoita funktio, joka saa parametrinaan bensiinin määrän Yhdysvaltain nestegallonoina ja
# palauttaa paluuarvonaan vastaavan litramäärän.
# Kirjoita pääohjelma, joka kysyy gallonamäärän käyttäjältä ja muuntaa sen litroiksi.
# Muunnos on tehtävä aliohjelmaa hyödyntäen. Muuntamista jatketaan siihen saakka,
# kunnes käyttäjä syöttää negatiivisen gallonamäärän.
# Yksi gallona on 3,785 litraa.

def litramuunnos (gallonat):
    litrat = 3.758 * gallonat
    return litrat

while True:
    gallonat = int(input("Monta gallonaa? "))
    if gallonat < 0:
        print("Annoit negatiivisen määärän. Ohjelma päättyy.")
        break
    litrat = litramuunnos(gallonat)
    print(f"{gallonat} gallonaa on {litrat:.3f} litraa.")