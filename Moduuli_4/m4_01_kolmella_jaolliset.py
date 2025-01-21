#Kirjoita while-toistorakennetta käyttävä ohjelma,
# joka tulostaa kolmella jaolliset luvut väliltä 1..1000.

# kolmella jaolliset voidaan laskea  0 + 3 + 3...

luku = int(0)

while luku <= 999:
    luku += 3
    print(luku)

#tiedämme, että 1000 ei ole jaollinen 3:lla - jos rajan laittaisi 1000:een, ohjelma printtaa 1002