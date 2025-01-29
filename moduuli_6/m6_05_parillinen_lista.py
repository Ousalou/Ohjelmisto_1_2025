#Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja.
# Ohjelma palauttaa toisen listan, joka on muuten samanlainen kuin parametrina saatu lista

# paitsi että siitä on karsittu pois kaikki parittomat luvut. Kirjoita testausta varten pääohjelma,
# jossa luot listan, kutsut funktiota ja tulostat sen jälkeen sekä alkuperäisen että karsitun listan.

def karsija (kokolista):
    parillinen_lista = []
    for i in kokolista:
        if i % 2 == 0:
            parillinen_lista.append(i)
    return parillinen_lista

kokolista = [1,9,2,19,2,10,20,8,44,45]
print(kokolista)
print(karsija(kokolista))