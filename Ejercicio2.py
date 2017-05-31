def verificaExtension(a, b):
    nuevab = []
    for i in b:
        i = i.lower()
        nuevab.append(i)
    a = a.split(".")
    nuevaa = []
    for y in a:
        y = y.lower()
        nuevaa.append(y)

    for x in nuevaa:
        if x in nuevab:
            salida = True
        else:
            salida = False
    return salida

