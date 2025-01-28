# Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka,
# kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
# Lopuksi ohjelma tulostaa saaduista luvuista viisi suurinta suuruusjärjestyksessä suurimmasta alkaen.
# Vihje: listan alkioiden lajittelujärjestyksen voi kääntää antamalla sort-metodille argumentiksi reverse=True.

luvut = []

while True:
    luku = (input("Anna luku tai paina enter lopettaaksesi ohjelman: "))
    if luku == "":
         break
    try:
        luku = int(luku)
        luvut.append(luku)
    except ValueError:
        print("Virheellinen luku. Anna luku tai paina enter ohjelman lopettamiseksi:")

luvut.sort(reverse=True)
print(luvut)

