'''
Uma corretora de seguros cobra mais barato se o principal condutor do veículo é mulher e se tem mais de 40 anos. Caso contrário, o valor do seguro fica caro.

Faça um programa que leia um valor inteiro (0 ou 1) que indica se o condutor é homem e outro valor inteiro (0 ou 1) que indica se o condutor tem mais de 40 anos. Com base nos valores lidos, o programa deve indicar, utilizando 0 ou 1, se o seguro vai ficar barato (verdadeiro - 1) ou caro (falso - 0).
'''



a1 = int(input())
a2 = int(input())  
  
if a1 == 0 and a2 == 1:
        print("1")
else:
    print("0")