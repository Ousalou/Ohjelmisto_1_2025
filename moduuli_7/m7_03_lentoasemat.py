#Kirjoita ohjelma lentoasematietojen hakemiseksi ja tallentamiseksi.
# Ohjelma kysyy käyttäjältä, haluaako tämä syöttää uuden lentoaseman,
# hakea jo syötetyn lentoaseman tiedot vai lopettaa.
# Jos käyttäjä valitsee uuden lentoaseman syöttämisen, ohjelma kysyy käyttäjältä
# lentoaseman ICAO-koodin ja nimen.
# Jos käyttäjä valitsee haun, ohjelma kysyy ICAO-koodin ja tulostaa sitä vastaavan lentoaseman nimen.
# Jos käyttäjä haluaa lopettaa, ohjelman suoritus päättyy.
# Käyttäjä saa valita uuden toiminnon miten monta kertaa tahansa aina siihen asti,
# kunnes hän haluaa lopettaa. (ICAO-koodi on lentoaseman yksilöivä tunniste.)
# Esimerkiksi Helsinki-Vantaan lentoaseman ICAO-koodi on EFHK. Löydät koodeja helposti selaimen avulla.)

lentokentta_sanakirja = {"EFHK": "Helsinki-Vantaa", "JFK": "John F. Kennedyn kansainvälinen lentoasema"}

while True:
    valinta = input("----------------\nKirjoita 'HAE' hakeaksesi lentoaseman nimen, tai\nkirjoita 'UUSI' lisätäksesi lentoaseman, tai\nkirjoita 'LOPETA' ohjelman loettamiseksi:\n").upper()
    if valinta == "HAE":
        haku = input("----------------\nKirjoita haettavan lentokentän ICAO-koodi: ").upper()
        if haku in lentokentta_sanakirja:
            print(f"Lentoaseman nimi on '{lentokentta_sanakirja[haku]}'")
        else:
            print("Lentokenttää ei löytynyt! Voit syöttää lentokentän valitsemalla 'UUSI'.")
    elif valinta == "UUSI":
        uusi_koodi = input("----------------\nSyötä uuden lentokentän ICAO-koodi: ").upper()
        if uusi_koodi in lentokentta_sanakirja:
            print("Tämän niminen kenttä löytyy jo! Valitse 'HAE' aloitusvalikosta hakeaksesi sen.")
        uusi_nimi = input("Syötä uuden lentokentän nimi: ")
        lentokentta_sanakirja[uusi_koodi] = uusi_nimi
    elif valinta == "LOPETA":
        print("----------------\nOhjelma on lopetettu.")
        break






