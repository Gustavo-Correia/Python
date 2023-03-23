#Faça um programa que receba a quantidade de m3 de água consumidos e o custo por litro de água e calcule:

#a) O valor a ser pago pela água; 

#b) O valor a ser pago pelo esgoto, sabendo que este corresponde a 80% do valor da água consumida;

#c) O valor total da conta, considerando água e esgoto.

#Dica: Lembre-se que 1 m3 = 1.000 litros

a, b= map(float,(input().split()))
triang = (a * 1000) * b
esgo = ((a*1000) *0.8) * b
tot = triang + esgo
print("{0:.2f}".format(triang))
print("{0:.2f}".format(esgo))
print("{0:.2f}".format(tot))