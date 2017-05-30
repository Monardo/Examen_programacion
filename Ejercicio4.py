import unittest
def devuelveGanador(n):
    ganador = []
    if n == []:
        ganador = ('""')
        return ganador
    for x in n:
        lista = list(x)
        if lista[1] > lista[3]:
            ganador = lista[0]
        elif lista[3] > lista[1]:
            ganador = lista[2]
        elif lista[1] == lista[3]:
            ganador = lista[0]
    return ganador

class tester (unittest.TestCase):
    def test_1(self):
        self.assertEqual('""', devuelveGanador([]))
        self.assertEqual('a', devuelveGanador([("a", 1, "b", 0)]))
        self.assertEqual('c', devuelveGanador([("a",1,"b",0),("a",1,"c",2),("c",3,"b",0)]))
        self.assertEqual('c', devuelveGanador([("a",1,"b",1),("a",1,"c",1),("c",1,"b",1)]))
        self.assertEqual('a', devuelveGanador([("a",1,"b",-2),("a",1,"c",1),("c",1,"b",1),("d",1,"a",9)]))
"""
def ejercicio4(var1):
    return devuelveGanador(var1)
campeonato = []
1 print(ejercicio4(campeonato)) # ""
campeonato = [("a",1,"b",0)]
2 print(ejercicio4(campeonato)) # a
campeonato = [("a",1,"b",0),("a",1,"c",2),("c",3,"b",0)]
3 print(ejercicio4(campeonato)) # c
campeonato = [("a",1,"b",1),("a",1,"c",1),("c",1,"b",1)]
4 print(ejercicio4(campeonato)) # a  b  c (cualquiera de las 3)
campeonato = [("a",1,"b",-2),("a",1,"c",1),("c",1,"b",1),("d",1,"a",9)]
5 print(ejercicio4(campeonato)) # a 
"""