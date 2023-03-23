'''
A Copa do Mundo de 2010 foi realizada na Africa do Sul. Bolas de futebol são muito fáceis de transportar, já que elas saem das fábricas vazias e só são enchidas somente pelas lojas ou pelos consumidores finais. Infelizmente o mesmo não pode ser dito das bolas de boliche. Como elas são completamente sólidas, elas só podem ser transportadas embaladas uma a uma, em caixas separadas. 

A Ambroliche é uma fábrica de bolas de boliche que trabalha somente através de encomendas e envia todas as bolas por SEDEX. Como as bolas têm tamanhos diferentes, a Ambroliche tem vários tamanhos de caixas diferentes para transportá-las.

Escreva um programa que, dado o diâmetro de uma bola e as 3 dimensões de uma caixa (altura, largura e profundidade), diz se a bola de boliche cabe dentro da caixa ou não. '''

a1 = int(input())

alt, larg, profun = input().split()

alt,larg,profun = int(alt),int(larg),int(profun)

if a1 >= 1 or a1 <= 10000:
    if alt >= 1 or alt <= 10000:
        if larg >= 1 or larg <= 10000:
            if profun >= 1 or profun <= 10000:
                if alt >= a1 and larg >= a1 and profun >= a1:
                    print("S")
                else:
                    print("N")