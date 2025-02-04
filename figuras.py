import math

def calculoPerimetro(numLados, lado):
    perimetro = numLados * lado
    return perimetro

def calculoArea(numLados, lado):
    if numLados == 3:
        area = (lado ** 2) * (math.sqrt(3) / 4) 
    elif numLados == 4:
        area = lado ** 2 
    elif numLados == 5:
        area = (5 / 4) * lado ** 2 * (1 / math.tan(math.pi / 5))
    else:
        area = 0  
    return area


def mostrarResultado(numLados, perimetro, area):
    print("El perímetro de una figura de",numLados,"lados es igual a",perimetro,"y el área es igual a",area)

numLados = int(input("Ingrese el número de lados de la figura: "))
lado = int(input("Ingrese el tamaño del lado: "))

perimetro = calculoPerimetro(numLados, lado)
area = calculoArea(numLados, lado)

mostrarResultado(numLados, perimetro, area)
