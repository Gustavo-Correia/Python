'''
Poliana resolveu economizar dinheiro para comprar um carro.

Ela traçou como meta depositar um valor X em seu cofrinho no primeiro dia da semana, e ir guardando a cada manhã o valor do dia anterior acrescido de pelo menos R$ 0,50. Mas será que ela vai conseguir fazer isso todos os dias?

Para saber se o plano de Poliana vai dar certo, escreva um programa que receba como entrada o valor inicial depositado, e em seguida os valores depositados a cada dia. Ao final, exiba o total poupado e quantas vezes Poliana conseguiu cumprir sua meta.

Dica: é preciso sempre comparar o valor do dia com o do dia anterior
'''

n = 0
t = 0
vitoria = 0
total = 0.0
while t < 7:
    k = n
    n = float(input())
    if t > 0:
        if n >= k + 0.5:
            vitoria += 1
    total = total + n
    t = t + 1
print("R$ {0:.2F}".format(total))
print(vitoria)
