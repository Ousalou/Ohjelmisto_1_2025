#Kirjoita ohjelma, joka kysyy käyttäjältä käyttäjätunnuksen ja salasanan.
# Jos jompikumpi tai molemmat ovat väärin, tunnus ja salasana kysytään uudelleen.
# Tätä jatketaan kunnes kirjautumistiedot ovat oikein tai väärät tiedot on syötetty viisi kertaa.
# Edellisessä tapauksessa tulostetaan
# Tervetuloa ja jälkimmäisessä Pääsy evätty. (Oikea käyttäjätunnus on python ja salasana rules).

tunnus = str("python")
salasana = str("rules")
kerrat = int(5)

while True:
    if kerrat < 0:
        print("Pääsy evätty.")
        break
    k_tunnus = str(input("Syötä käyttäjätunnus: "))
    if k_tunnus != tunnus:
        kerrat = kerrat - 1
        if kerrat >= 0:
            print(f"Väärä käyttäjätunnus. Sinulla on {kerrat} yritystä jäljellä.")
    elif k_tunnus == tunnus:
        k_salasana = input("Syötä salasana: ")
        if k_salasana != salasana:
            kerrat = kerrat - 1
            if kerrat >= 0:
                print(f"Väärä salasana. Sinulla on {kerrat} yritystä jäljellä.")
        elif k_salasana == salasana:
                break