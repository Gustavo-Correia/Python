#Faça um programa que receba o salário de um funcionário e o percentual de aumento.

#Calcule e mostre o valor do aumento e o novo salário com as seguintes mensagens

#Entrada: (um por linha, sem mensagem)
#Salario
#Percentual de aumento


#Saída

#Seu salario teve aumento de <x> %, passando de R$ <x> para R$ <x>

a = float(input())
b = float(input())

if b != 0:
    tot = (a * b) / 100
    print("Seu salario teve aumento de {0:.1f} %, passando de R$ {1:.1f} para R$ {2:.1f}".format(b,a,tot + a))
else:
    print("Seu salario teve aumento de {0:.1f} %, passando de R$ {1:.1f} para R$ {2:.1f}".format(b,a,a))