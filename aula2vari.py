data = 12
contador = 0
while contador <= 100:
    mult = contador * data
    
    while mult >= 1000:
        print ("Maior que mil")
        break
    contador += 1 
    print (mult)
