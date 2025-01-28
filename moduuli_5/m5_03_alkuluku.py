#Kirjoita ohjelma, joka kysyy käyttäjältä kokonaisluvun ja ilmoittaa, onko se alkuluku.
# Tässä tehtävässä alkulukuja ovat luvut, jotka ovat jaollisia vain ykkösellä ja itsellään.

#Esimerkiksi luku 13 on alkuluku, koska se voidaan jakaa vain luvuilla 1 ja 13 siten, että jako menee tasan.
#Toisaalta esimerkiksi luku 21 ei ole alkuluku, koska se voidaan jakaa tasan myös luvulla 3 tai luvulla 7.

jaollisuudet = [2,3,4,5,6,7,8,9]

luku = int(input("Anna luku: "))

try: jaollisuudet.remove(luku)
except ValueError: pass

on_alkuluku = True

for i in jaollisuudet:
    if luku % i == 0:
        on_alkuluku = False
        break

if True:
    print("Luku on alkuluku.")
else:
    print("Luku ei ole alkuluku.")




