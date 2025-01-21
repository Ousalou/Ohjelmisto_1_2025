#Kirjoita ohjelma, joka kysyy käyttäjältä lukuja
# siihen saakka, kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
# Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman.

#1) pitää luoda "talletus" luvuille
#2) pitää selvittää miten while pyörii kaikilla mahdollisilla luvuilla, vain tyhjä syöte on break
#3) jos käyttäjä syöttää merkkijonon, pitää palata while-rakenteen alkuun, mutta ei break? (!!)

luvut = []

while True:
    luku_str = (input("Anna luku tai paina enter ohjelman lopettamiseksi: "))
    if luku_str == (""):
        print(f"Lukujen pienin on {min(luvut):.2f} ja suurin {max(luvut):.2f}.")
        break
    try:
        luku = float(luku_str)
        luvut.append(luku)
    except ValueError:
        print("Anna luku tai paina enter. Älä kirjoita muuta.")

#Opettelin tähän try-except rakenteen että saan 3. vaiheen toimimaan


