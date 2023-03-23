#Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas) no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1. A seguir mostre o valor lido e a relação de notas necessárias.
d = int(input())
valor = d
nota100 = 0
nota50 = 0
nota20 = 0
nota10 = 0
nota5 = 0
nota2 = 0
nota1 = 0
if d >= 0 and d <= 1000000:
    while d != 0:
        if d >= 100:
            d = d - 100
            nota100 = nota100 + 1
        elif d >= 50 and d < 100:
            d = d - 50
            nota50 = nota50+ 1 
        elif d < 50 and d >= 20:
            d = d - 20
            nota20 = nota20 + 1
        elif d < 20 and d >= 10:
            d = d - 10
            nota10 = nota10 + 1       
        elif d < 10 and d >= 5:
            d = d - 5
            nota5 = nota5 + 1 
        elif d < 5 and d >= 2:
            d = d - 2
            nota2 = nota2 + 1
        else:
            d = d - 1
            nota1 = nota1 + 1
print (valor)
print("{0:.0f} nota(s) de R$ 100,00".format(nota100))
print("{0:.0f} nota(s) de R$ 50,00".format(nota50))
print("{0:.0f} nota(s) de R$ 20,00".format(nota20))
print("{0:.0f} nota(s) de R$ 10,00".format(nota10))
print("{0:.0f} nota(s) de R$ 5,00".format(nota5))
print("{0:.0f} nota(s) de R$ 2,00".format(nota2))
print("{0:.0f} nota(s) de R$ 1,00".format(nota1))