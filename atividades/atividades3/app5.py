#Faça um programa que leia 3 números inteiros e imprima o menor deles.
a = int(input())
b = int(input())
c = int(input())
maior = 0
if a < b and a < c:
    menor = a
elif b < c:
    menor = b
else:
    menor = c
    
print (menor)