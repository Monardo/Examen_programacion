def devuelveMatrizTriangular(n):
    import random
    matriz = []
    matrizB = []
    if n <= 1 or n == str(n) or n != int(n):
        return matriz
    for i in range(n):
        matriz = []
        for h in range(n):
            if h < i:
                matriz.append(0)
            else:
                x = random.randint(1, 9)
                matriz.append(x)
        matrizB.append(matriz)
    return matrizB

def ejercicio3(var1):
    return devuelveMatrizTriangular(var1)


print(ejercicio3(-1)) # []
print(ejercicio3(0)) # []
print(ejercicio3(1)) # []
print(ejercicio3(2)) # [[x,x],[0,x]]
print(ejercicio3(3)) # [[x,x,x],[0,x,x],[0,0,x]]
print(ejercicio3(4)) # [[x,x,x,x],[0,x,x,x],[0,0,x,x],[0,0,0,x]]
print(ejercicio3("4")) #[]
print(ejercicio3("PEPE")) #[]
print(ejercicio3(2.5)) #[]
