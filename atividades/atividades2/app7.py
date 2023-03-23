#Sabe-se que o Kwh de uma residência custa R$ 1,50. Faça um programa em Python que receba a quantidade de KWh consumidos, calcule e mostre:a) O valor a ser pago pela residência

#b) O valor a ser pago com desconto de 15%
a = float(input())
triang = (a * 1.5)
tri = triang - (triang * 0.15) 


print("Valor a ser pago: R$ {0:.2f} reais".format(triang))
print("Valor a ser pago com desconto: R$ {0:.2f} reais".format(tri))