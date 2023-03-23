#Considere as expressões abaixo para cálculo das médias aritmética (A), harmônica (H) e geométrica (G).

dR = (input())


ar = float(input())
br = float(input())
cr = float(input())

if dR == 'A':
    mediaar= (ar+br+cr)/3
    print("{0:.3f}".format(mediaar))   
elif dR == 'H':
    mediaarm= 3/(1/ar + 1/br + 1/cr)
    print("{0:.3f}".format(mediaarm))       
elif dR == 'G':
    mediageo = (ar*br*cr)**0.333333333333
    print("{0:.3f}".format(mediageo)) 
