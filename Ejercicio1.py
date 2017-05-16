def devuelveDivisores(a, b):
    divisores = []
    if a == "" or a <= 0:
        return divisores
    else:
        for i in b:
            if a % i == 0:
                divisores.append(i)
    return divisores

def ejercicio1(var1, var2):
    return devuelveDivisores(var1,var2)

print(ejercicio1("",[1,2,3])) # []
print(ejercicio1(-1,[1,2,3])) # []
print(ejercicio1(0,[1,2,3])) # []
print(ejercicio1(0,[])) # []
print(ejercicio1(1,[1,2])) # [1]
print(ejercicio1(2,[1,-2])) # [1,-2]
print(ejercicio1(8,[1,7,2,-4,6,9])) # [1,2,-4]
print(ejercicio1(331,[1,2,3,7,147,331,518])) # [1,331]