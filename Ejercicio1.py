import unittest
def devuelveDivisores(a, b):
    divisores = []
    if a == "" or a <= 0:
        return divisores
    else:
        for i in b:
            if a % i == 0:
                divisores.append(i)
    return divisores

class tester (unittest.TestCase):
    def test_1(self):
        self.assertEqual([], devuelveDivisores("", [1, 2, 3]))
        self.assertEqual([], devuelveDivisores(-1, [1, 2, 3]))
        self.assertEqual([], devuelveDivisores(0, [1, 2, 3]))
        self.assertEqual([], devuelveDivisores(0, []))
        self.assertEqual([1], devuelveDivisores(1, [1, 2]))
        self.assertEqual([1, -2], devuelveDivisores(2, [1, -2]))
        self.assertEqual([1, 2, -4], devuelveDivisores(8, [1, 7, 2, -4, 6, 9]))
        self.assertEqual([1, 331], devuelveDivisores(331, [1, 2, 3, 7, 147, 331, 518]))


""""
def ejercicio1(var1, var2):
    return devuelveDivisores(var1,var2)

print(ejercicio1("",[1,2,3])) # []
print(ejercicio1(-1,[1,2,3])) # []
print(ejercicio1(0,[1,2,3])) # []
print(ejercicio1(0,[])) # []
print(ejercicio1(1,[1,2])) # [1]
print(ejercicio1(2,[1,-2])) # [1,-2]
print(ejercicio1(8,[1,7,2,-4,6,9])) # [1,2,-4]
print(ejercicio1(331,[1,2,3,7,147,331,518])) # [1,331]"""