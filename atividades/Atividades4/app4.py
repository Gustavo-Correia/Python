# Ache a soma de todos números naturais múltiplos de 3 ou 5 menores que n.n = 0
t = 0
total = 0
n = int(input())
while t < n:    
    if t % 3 == 0:
        total += t
    elif t % 5 == 0:
        total += t
    t += 1    
    
    
    
print(total)
