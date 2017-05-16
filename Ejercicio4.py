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

def ejercicio4(var1):
    return devuelveGanador(var1)

campeonato = []
print(ejercicio4(campeonato)) # ""
campeonato = [("a",1,"b",0)]
print(ejercicio4(campeonato)) # a
campeonato = [("a",1,"b",0),("a",1,"c",2),("c",3,"b",0)]
print(ejercicio4(campeonato)) # c
campeonato = [("a",1,"b",1),("a",1,"c",1),("c",1,"b",1)]
print(ejercicio4(campeonato)) # a  b  c (cualquiera de las 3)
campeonato = [("a",1,"b",-2),("a",1,"c",1),("c",1,"b",1),("d",1,"a",9)]
print(ejercicio4(campeonato)) # a