#Você deve implementar uma calculadora que calcule as 4 operações básicas, dados 2 números reais, e imprima os 4 resultados.

a = float(input())
b = float(input())
soma = a + b
sub = a - b
mult = a * b
div = a/b
print("{0:.2f}".format(soma))
print("{0:.2f}".format(sub))
print("{0:.2f}".format(mult))
print("{0:.2f}".format(div))