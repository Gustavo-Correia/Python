'''
Escreva um programa que receba como entrada dois números inteiros e retorne a soma dos números positivos no intervalo definido por eles, considerando inclusive os extremos.

Obs: o intervalo pode ser crescente ou decrescente'''

m = int(input())
n = int(input())
total = 0
maximo = max(m,n)
minimo = min(m,n)

while minimo <= maximo:
    if minimo >= 0:
        total += minimo
    
    minimo += 1
print(total)