#Seu objetivo é determinar o maior múltiplo de um inteiro dado menor do que ou igual a um outro inteiro dado

n = int(input())
m = int(input())
contador = 1
ko = 0
while contador <= m // n + 1:    
    if n * contador > m:
        ko = (contador - 1) * n
        break
    contador += 1

if ko == 0:
    print("sem multiplos menores que", m)
else:
    print(ko)
