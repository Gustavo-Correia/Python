#Faça um programa que leia um número inteiro e imprima a tabuada de multiplicação deste número. Suponha que o número lido da entrada é maior que zero.
num = int(input())
x = 1

while (x < 10):
    resul = num * x
    print ("{0} X {1} = {2}".format(num,x,resul))
    x = x + 1
    