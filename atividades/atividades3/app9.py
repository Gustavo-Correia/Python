#Dados três números em ponto flutuante queremos saber quantos deles estão acima da média aritmética.

a = float(input())
b = float(input())
c = float(input())

media = (a+b+c)/3

quant = 0

if b>media:
   quant = quant + 1
   
if a > media:
    quant = quant + 1
    
if c > media:
    quant = quant + 1
    
print (quant)