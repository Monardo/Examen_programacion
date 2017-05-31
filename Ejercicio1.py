def devuelveDivisores(a, b):
    divisores = []
    if a == "" or a <= 0:
        return divisores
    else:
        for i in b:
            if a % i == 0:
                divisores.append(i)
    return divisores