import unittest
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

class tester (unittest.TestCase):
    def test_1(self):
        self.assertEqual([], devuelveMatrizTriangular(-1))
        self.assertEqual([], devuelveMatrizTriangular(0))
        self.assertEqual([], devuelveMatrizTriangular(1))
        #self.assertEqual([[2,3],[0,5]], devuelveMatrizTriangular(2))
        #self.assertEqual([[x,x,x],[0,x,x],[0,0,x]], devuelveMatrizTriangular(3))
        #self.assertEqual([[x,x,x,x],[0,x,x,x],[0,0,x,x],[0,0,0,x]], devuelveMatrizTriangular(4))
        self.assertEqual([], devuelveMatrizTriangular("4"))
        self.assertEqual([], devuelveMatrizTriangular("PEPE"))
        self.assertEqual([], devuelveMatrizTriangular(2.5))


"""
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
"""