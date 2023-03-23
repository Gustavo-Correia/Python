'''
Escreva um programa que calcule os N termos da série S  abaixo:

 S = (1/3) + (2/6) + (3/9) + (4/12) + …

O seu programa deve imprimir na saída padrão tanto os termos da série quanto o valor da soma com precisão de 2 casas decimais.'''

n = int(input())

soma = 0.0
for i in range(1, n+1):
    numerador = i
    denominador = 3 * i
    termo = numerador / denominador
    soma += termo
    if i == n:
        print(f"{numerador}/{denominador}", end="")
    else:
        print(f"{numerador}/{denominador} + ", end="")

print(f"\n{soma:.2f}")