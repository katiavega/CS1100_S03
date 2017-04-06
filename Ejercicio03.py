#Sabiendo que la Discriminante es B**2 -4AC

import math
A = float(input("Ingrese A: "))
B = float(input("Ingrese B: "))
C = float(input("Ingrese C: "))
discriminante = +B**2 - 4*A*C
if discriminante > 0:
    raiz1 = (+B + math.sqrt(discriminante))/2*A
    raiz2 = (-B - math.sqrt(discriminante))/2*A
    print("Las raíces son:", raiz1, " y ", raiz2 )
else:
    print ("Raíces imaginarias")

