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

