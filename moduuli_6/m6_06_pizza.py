#Kirjoita funktio, joka saa parametreinaan pyöreän pizzan halkaisijan senttimetreinä sekä pizzan hinnan euroina.
# Funktio laskee ja palauttaa pizzan yksikköhinnan euroina per neliömetri.
# Pääohjelma kysyy käyttäjältä kahden pizzan halkaisijat ja hinnat sekä ilmoittaa, kumpi pizza antaa paremman vastineen rahalle
# (eli kummalla on alhaisempi yksikköhinta). Yksikköhintojen laskennassa on hyödynnettävä kirjoitettua funktiota.

import math

pizza_hinnat = []

def hinta_laskuri (halkaisija, hinta):
    halkaisija = halkaisija / 100
    pinta_ala = (halkaisija/2)**2 * math.pi
    hinta_m2 = hinta/pinta_ala
    pizza_hinnat.append(hinta_m2)
    return hinta_m2

kyselyt = 1

while kyselyt <= 2:
    halkaisija = float(input(f"{kyselyt}:n pizzan halkaisija senttimetreinä: "))
    hinta = float(input(f"{kyselyt}:n pizzan hinta euroina ilman euromerkkiä: "))
    print(f"Pizzan nro {kyselyt} hinta per neliömetri on {hinta_laskuri (halkaisija, hinta):.2f}€")
    kyselyt = kyselyt + 1

halvin = min(pizza_hinnat)
print(f"Parasta vastinetta rahalle tarjoaa pizza numero {pizza_hinnat.index(halvin)+1} :)")
#Jälleen huom. ykkönen = 0 eli +1 että tuele oikea sijainti 1-2


