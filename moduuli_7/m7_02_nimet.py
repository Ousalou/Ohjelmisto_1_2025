#Kirjoita ohjelma, joka kysyy käyttäjältä nimiä siihen saakka,
# kunnes käyttäjä syöttää tyhjän merkkijonon.
# Kunkin nimen syöttämisen jälkeen ohjelma tulostaa
# joko tekstin Uusi nimi tai Aiemmin syötetty nimi sen mukaan,
# syötettiinkö nimi ensimmäistä kertaa.
# Lopuksi ohjelma luettelee syötetyt nimet yksi kerrallaan allekkain mielivaltaisessa järjestyksessä.
# Käytä joukkotietorakennetta nimien tallentamiseen.

nimet = set()

while True:
    nimi = input("Anna nimi tai paina enter ohjelman lopettamiseksi: ")
    if nimi == "":
        break
    elif nimi not in nimet:
        print("Uusi nimi, lisätään.")
        nimet.add(nimi)
    elif nimi in nimet:
        print("Aiemmin syötetty nimi.")

print("")
print(f"Tässä kaikki syöttämäsi nimet:")
for nimi in nimet:
    print(nimi)

#for-in jos muuttujat allekkain! Järkkä silti satunnainen.