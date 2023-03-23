'''
Escreva um programa que transforme o computador numa urna eletrônica para eleição, em segundo turno, para presidente de um país chamado Ambrolândia. Nessas eleições concorrem os candidatos 83-Alibabá e 93-Alcapone. Cada voto deve ser dado pelo número do candidato, permitindo-se ainda o voto 0 para voto em branco. Qualquer voto diferente dos já citados é considerado nulo. No final da eleição o programa deve emitir um relatório contendo a votação de cada candidato, a quantidade votos em branco, a quantidade de votos nulos e o candidato eleito e os respectivos percentuais.

Em Ambrolândia, o percentual de votos é calculado considerando os votos válidos. O voto nulo não é considerado um voto válido. Entretanto, o voto em branco é considerado um voto válido.
''' 
x = 0
y = 0
z = 0
w = 0
k = 0
a = 0.0
b = 0.0
total = 0
v = 0
while v != -1:
    v = int(input())
    #testa os votos
    if v == 83:
        x += 1
    elif v == 93:
        y += 1
    elif v == 0:
        z += 1
    elif v != 0 and v != 83 and v != 93:
        w += 1
        total -= 1
    total += 1
#quem ganhou    
w -= 1
if x > y:
    k = 83
else:
    k = 93  
a = (x/total) * 100
b = (y/total) * 100

print(x)
print(y)
print(z)
print(w)
print(k)
print("{0:.2f}".format(a))
print("{0:.2f}".format(b))