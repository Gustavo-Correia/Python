#Faça um programa que calcule a área da superfície e o volume de um cilindro. Use pi = 3.14.

#O valor de saída deve ser arredondado usando 2 casas decimais.

import math

a = float(input())
b = float(input())
pi = 3.14
pimi = 6.28
volume = pi * pow(b,2) * a

area = (pimi * b * a) + (pimi * pow(b,2))

print ("{0:.2f}".format(volume))
print ("%.2f" % area)