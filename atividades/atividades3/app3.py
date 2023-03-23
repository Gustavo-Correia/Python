#Chama-se ano bissexto o ano ao qual é acrescentado um dia extra, ficando ele com 366 dias, um dia a mais do que os anos normais de 365 dias, ocorrendo a cada quatro anos (exceto anos múltiplos de 100 que não são múltiplos de 400).

#Faça um programa que indique se o ano digitado é bissexto.


a1 = int(input())




if a1 % 400 == 0:
    print("BISSEXTO")
elif a1 % 100 == 0:
      print("NAOBISSEXTO")
elif a1 % 4 == 0:
    print("BISSEXTO")      
else:
   print("NAOBISSEXTO")     