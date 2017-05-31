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
