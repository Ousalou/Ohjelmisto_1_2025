#Kirjoita ohjelma, joka kysyy ympyrän säteen ja tulostaa sen pinta-alan.

import math

sade_str = (input("Mikä on ympyrän säde? "))
sade = float(sade_str)
PA = sade**2 * math.pi
print(f"Ympyrän pinta-ala on {PA:.2f}")

