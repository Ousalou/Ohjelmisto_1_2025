# Kirjoita ohjelma, joka kysyy kalastajalta kuhan pituuden senttimetreinä.
# Jos kuha on alamittainen, ohjelma käskee laskea kuhan takaisin järveen
# ilmoittaen samalla käyttäjälle, montako senttiä alimmasta sallitusta pyyntimitasta puuttuu.
# Kuha on alamittainen, jos sen pituus on alle 37 cm.

kuha_str = input("Mikä on kuhan pituus senttimetreinä? ")
kuha = float(kuha_str)

while kuha < 0
    kuha_str = input("Mikä on kuhan pituus senttimetreinä? ")
    kuha = float(kuha_str)
# Selvitä: miten tähän saa kuhalle määritelmän, että ei ole numero?

if kuha >= 37:
    print("Voit pitää kalasi!")

if kuha < 37:
    print(f"Heitä kuha takaisin järveen. Se on {37-kuha}cm alamittainen!")