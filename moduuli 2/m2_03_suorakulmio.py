# Kirjoita ohjelma, joka kysyy suorakulmion kannan ja korkeuden.
# Ohjelma tulostaa suorakulmion piirin ja pinta-alan.
# Suorakulmion piiri tarkoittaa sen neljän sivun yhteispituutta.

kanta = float(input("Mikä on suorakulmion kanta? "))
korkeus = float(input("Mikä on suorakulmion korkeus? "))
PA = kanta * korkeus
Piiri = 2*kanta + 2*korkeus
print(f"Suorakulmiosi pinta-ala on {PA:.2f} ja piiri {Piiri:.2f}. :)")