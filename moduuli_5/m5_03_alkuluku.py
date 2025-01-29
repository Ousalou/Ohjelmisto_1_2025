#Kirjoita ohjelma, joka kysyy käyttäjältä kokonaisluvun ja ilmoittaa, onko se alkuluku.
#Tässä tehtävässä alkulukuja ovat luvut, jotka ovat jaollisia vain ykkösellä ja itsellään.
#   Esimerkiksi luku 13 on alkuluku, koska se voidaan jakaa vain luvuilla 1 ja 13 siten, että jako menee tasan.
#   Toisaalta esimerkiksi luku 21 ei ole alkuluku, koska se voidaan jakaa tasan myös luvulla 3 tai luvulla 7.

#Omaa selvitystä alkuluvun tarkistuksesta:
#   Vähintään toinen tekijä on aina pienempi kuin itse luvun neliöjuuri
#   Jos tekijälle ei siis löydetä 0-jakojäännöksen jättävää jakajaa väliltä 2 ja luvun neliöjuuri
#   >> on alkuluku
# + HUOM !! :'D +1 rangeen, koska range EI käy viimeistä lukua läpi (eli se luku minkä ALLE neliöjuuren pitäisi olla)

import math
on_alkuluku = True
luku_str = str(input("Anna luku: "))

try: luku = int(luku_str)
except ValueError:
    print("Ole hyvä ja anna luku numeroina.")
    exit()

nelio_juuri = int(math.sqrt(luku))

for i in range (2, nelio_juuri + 1):
   if luku % i == 0:
    on_alkuluku = False
    break

if on_alkuluku:
    print("Luku on alkuluku.")
if not on_alkuluku:
    print("Luku ei ole alkuluku.")




