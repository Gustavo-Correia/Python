#Este mês ocorre o Mundial de Tiro Ao Alvo e as competições ocorrem em duas etapas. Para se classificar para a segunda etapa, cada competidor precisa somar pelo menos 100 pontos ao longo de 6 partidas. Escreva um programa que receba como entrada os pontos feitos por um competidor em cada uma das partidas da primeira etapa, e exiba uma mensagem informando se ele foi classificado ou não.

a1 = int(input())
a2 = int(input())
a3 = int(input())
a4 = int(input())
a5 = int(input())
a6 = int(input())

som = a1+a2+a3+a4+a5+a6

if som >= 100:
      print("Classificado")
else:
    print("Eliminado")  