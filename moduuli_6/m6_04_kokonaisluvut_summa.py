#Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja.
# Ohjelma palauttaa listassa olevien lukujen summan.
# Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota ja tulostat sen palauttaman summan.

def numeroiden_summaus (kokonaisluku):
    summa = sum(kokonaisluku)
    return summa

kokonaisluku = [1,4,5,10] #pitäs olla =20
print(numeroiden_summaus(kokonaisluku))

#Huom! Funktion voi laittaa printin sisään, ei tarvitse määrittää summa = funktio, ja print(summa) erikseen