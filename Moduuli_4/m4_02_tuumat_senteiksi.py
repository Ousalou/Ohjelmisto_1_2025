#Kirjoita ohjelma, joka muuntaa tuumia senttimetreiksi niin kauan
# kunnes käyttäjä antaa negatiivisen tuumamäärän.
# Sen jälkeen ohjelma lopettaa toimintansa. 1 tuuma = 2,54 cm

tuuma = 0

while tuuma >= 0:
    tuuma = float(input("Monta tuumaa? "))
    if tuuma < 0:
        break
    sentti = tuuma * 2.54
    print(f"{tuuma} on {sentti}cm.")

#huom! if-break ENNEN konversiota ja printtiä,
#muuten ohjelma printtaa viimeisen neg. konversion ENNEN printtiä