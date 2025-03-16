#Kirjoita ohjelma, joka kysyy käyttäjältä lentoaseman ICAO-koodin.
# Ohjelma hakee ja tulostaa koodia vastaavan lentokentän nimen ja sen sijaintikunnan kurssilla käytettävästä lentokenttätietokannasta.
# ICAO-koodi on tallennettuna airport-taulun ident-sarakkeeseen.

import mysql.connector

yhteys = mysql.connector.connect(
         host='localhost',
         port= 3306,
         database='flight_game',
         user='keltanokat',
         password='lentopeli',
         autocommit=True
         )

icao = input("What is the icao code for your airport? ")
sql = f"select name, municipality from airport where ident = '{icao}'"
cursor = yhteys.cursor()
cursor.execute(sql)
airport_and_name = cursor.fetchall()
print(airport_and_name)


