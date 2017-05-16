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

def ejercicio2(var1,var2):
    return verificaExtension(var1,var2)
print(ejercicio2('/home/user/listado.txt',['mp3','wav','mpeg'])) # False
print(ejercicio2('/home/user/listado.txt',['mp3','wav','mpeg','txt'])) # True
print(ejercicio2('/home/user/listado.txt',['mp3','wav','mpeg','TXT'])) # True
print(ejercicio2('/home/user/listado.tXt',['mp3','wav','mpeg','TXT'])) # True
print(ejercicio2('/home/user/listado.txt',['txt'])) # True
print(ejercicio2('/home/user/listado',['mp3','wav','mpeg','txt'])) # False
print(ejercicio2('/home/user/listado',[])) # False
print(ejercicio2('',[])) # False
