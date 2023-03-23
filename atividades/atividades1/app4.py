#Faça um programa que leia um valor representando o gasto realizado por um cliente do restaurante COMABEM e imprima o valor total a ser pago, considerando os 10% do garçom.

a = float(input())

desc = (a * 0.1)

a = a + desc
print("{0:.2f}".format(a))