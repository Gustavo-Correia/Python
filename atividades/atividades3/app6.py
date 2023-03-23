'''
A companhia aérea Easy Jet oferece passagens baratas para várias cidades européias e é muito procurada por turistas de todo o mundo. Entretanto, ela tem regras muito rígidas para o tamanho da bagagem de mão de cada cliente: para ser aceita, a mala deve ter no máximo 45 cm de largura, 56 cm de comprimento e 25 cm de altura.

Escreva um programa que receba como entrada as dimensões de uma mala e exiba uma mensagem informando se a mala será aceita ou não.
'''

a = float(input())
b = float(input())
c = float(input())

const_a = 45.0
const_b = 56.0    
const_c = 25.0

if a <= const_a and b <= const_b and c <= const_c:
    print("PERMITIDA")
else:
    print("PROIBIDA")