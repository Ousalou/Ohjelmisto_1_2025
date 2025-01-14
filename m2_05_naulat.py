#Kirjoita ohjelma, joka kysyy käyttäjältä massan keskiaikaisten mittojen mukaan
# leivisköinä, nauloina ja luoteina.
# Ohjelma muuntaa syötteen täysiksi kilogrammoiksi ja grammoiksi sekä ilmoittaa tuloksen käyttäjälle.
# Yksi leiviskä on 20 naulaa.
# Yksi naula on 32 luotia.
# Yksi luoti on 13,3 grammaa.

luoti = 13.3
naula = 32 * 13.3
leiviska = 20 * 32 * 13.3

kayt_luoti = int(input("Monta luotia sinulla on? "))*luoti
kayt_naula = int(input("Monta naulaa sinulla on? "))*naula
kayt_leiviska = int(input("Monta leiviskää sinulla on? "))*leiviska

paino = float(kayt_luoti + kayt_naula + kayt_leiviska)
paino_kg = paino // 1000
#integerin // käyttö !
paino_g = paino - paino_kg*1000
#miinustetaan kilot kerrattuna grammoilla :D

print(f"Massa nykymittojen mukaan: {paino_kg:.0f} kiloa ja {paino_g:.1f} grammaa.")
#kiloja aina tasamäärä joten 0f, luotien alkuperäinen paino on 13.3 grammaa joten grammoihin .1f


