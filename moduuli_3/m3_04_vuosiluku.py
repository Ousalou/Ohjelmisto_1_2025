# Kirjoita ohjelma, joka kysyy vuosiluvun ja ilmoittaa, onko annettu vuosi karkausvuosi.
# Vuosi on karkausvuosi, jos se on jaollinen neljällä.
# Sadalla jaolliset vuodet ovat karkausvuosia vain jos ne ovat jaollisia myös neljälläsadalla.

vuosiluku = int(input("Anna mikä tahansa vuosiluku: "))

#jakojäännöksellä jaollisuus + if-elif-else rakenne

if vuosiluku % 100 == 0:
    if vuosiluku % 400 == 0:
        print("Vuosi on karkausvuosi.")
    else:
        print("Vuosi ei ole karkausvuosi.")

elif vuosiluku % 4 == 0:
    print("Vuosi on karkausvuosi.")

else: print("Vuosi ei ole karkausvuosi.")
