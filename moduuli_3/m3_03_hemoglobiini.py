#Kirjoita ohjelma, joka kysyy käyttäjän biologisen sukupuolen ja hemoglobiiniarvon (g/l).
# Ohjelma ilmoittaa, onko hemoglobiiniarvo alhainen, normaali vai korkea.
# Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l.
# Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l.

sukupuoli = input("Onko biologinen sukupuolesi mies vai nainen? ").lower()

while sukupuoli != "mies" and sukupuoli != "nainen":
    sukupuoli = input("Ikävä kyllä se ei ole vaihtoehto tässä ohjelmassa.\nKerro onko biologinen sukupuolesi mies vai nainen, tai kirjoita 'ei kiitos' ohjelman keskeyttämiseksi: \n").lower()
    if sukupuoli == "ei kiitos":
        break

if sukupuoli == "mies":
    hcg = float(input("Mikä on hemoglobiiniarvosi? "))
    if hcg < 134:
        print("Hemoglobiiniarvosi on alhainen.")
    elif hcg > 195:
        print("Hemoglobiiniarvosi on korkea.")

    else: print("Hemoglobiiniarvosi on normaali.")

if sukupuoli == "nainen":
    hcg = float(input("Mikä on hemoglobiiniarvosi? "))
    if hcg < 117:
        (print("Hemoglobiiniarvosi on alhainen."))
    elif hcg > 175:
        print("Hemoglobiiniarvosi on korkea.")
    else: print("Hemoglobiiniarvosi on normaali.")