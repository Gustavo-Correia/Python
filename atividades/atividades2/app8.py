#Escreva um programa que receba o raio (R) de uma esfera e forneça:

#O volume da esfera, sabendo que: Volume Esfera = (4πR3)/3

#bservação: Considere π como tendo o valor 3.1416.
pi = 3.1416
a = float(input())
triang = ((4 * pi) * a **3)/3



print("{0:.2f}".format(triang))