#Faça um programa que imprima todos os números ímpares entre dois números dados.

n = int(input())
m = int(input())
contador = 0
    
while n <= m:    
    if n % 2 != 0:
        print(n)
    n+= 1