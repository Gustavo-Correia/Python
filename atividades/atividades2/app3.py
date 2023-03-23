#Leia um valor inteiro, que é o tempo de duração em segundos de um determinado evento em uma fábrica e informe-o expresso no formato horas:minutos:segundos.

d = int(input())

hours = d // 3600
minutes = (d % 3600) // 60
seconds = d % 60

print("{0:.0f}:{1:.0f}:{2:.0f}".format(hours,minutes,seconds))
