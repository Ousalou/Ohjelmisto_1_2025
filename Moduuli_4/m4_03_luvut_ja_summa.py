#Kirjoita ohjelma, joka kysyy käyttäjältä lukuja
# siihen saakka, kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
# Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman.

#pitää luoda "talletus" luvuille
#pitää selvittää miten while pyörii kaikilla mahdollisilla luvuilla, vain tyhjä syöte on break
#jos käyttäjä syöttää merkkijonon, error mutta ei break? << ?????? Ongelma

luku = float(0)
luvut = []
luvut.append(luku)

while True:
    luku_str = (input("Anna luku tai paina enter ohjelman lopettamiseksi: "))
    if luku_str == (""):
        print(f"Lukujen summa on {sum(luvut):.2f}.")
        break
    #elif luku_str != ("") and (#luku_str on tekstiä, ei ole numero?):
    #   luku_str = (input("Anna luku tai paina enter ohjelman lopettamiseksi: "))
    else: luku = float(luku_str)
    luvut.append(luku)

#miksi float antaa errorin mutta int on ok? entä jos käyttäjä syöttää murtoluvun?




