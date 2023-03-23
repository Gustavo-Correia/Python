'''
A Subindo Bem Confortavelmente (SBC) é uma empresa tradicional, com mais de 50 anos de experiência na fabricação de elevadores. Todos os projetos da SBC seguem as mais estritas normas de segurança, mas infelizmente uma série de acidentes com seus elevadores manchou a reputação da empresa. Ao estudar os acidentes, os engenheiros da companhia concluíram que, em vários casos, o acidente foi causado pelo excesso de passageiros no elevador. 

Por isso, a SBC decidiu fiscalizar com mais rigor o uso de seus elevadores: foi instalado um sensor em cada porta que detecta a quantidade de pessoas que saem e entram em cada andar do elevador. A SBC tem os registros do sensor de todo um dia de funcionamento do elevador (que sempre começa vazio). 

Eles sabem que as pessoas são educadas e sempre deixam todos os passageiros que irão sair em um andar saírem antes de outros passageiros entrarem no elevador, mas ainda assim eles têm tido dificuldade em decidir se a capacidade máxima do elevador foi excedida ou não.

Escreva um programa que, dada uma sequência de leituras do sensor e a capacidade máxima do elevador, determina se a capacidade máxima do elevador foi excedida em algum momento. 
'''

t = 0
total = 0
n,c = map(int,input().split())
while t < n:    
    s,e = map(int,input().split())
    total -= s
    if total < 0:
        total = 0
    total += e
    if total > c:
        print("S")
        break
    t += 1    
if t == n:
    print("N")  