from math import sqrt
from math import pi
from math import tan

def calculoPerimetro(numLados, lado):
    perimetro = numLados * lado
    return perimetro

def calculoArea(numLados, lado,):
    theta = pi / numLados
    apotema = lado / (2 * tan(theta))
    area = (perimetro * apotema)/2
    return area

def mostrarResultado(numLados, perimetro, area):
    if numLados <= 1:
        print("No existen poligonos de un solo lado")
    else:
        print("El perímetro de una figura de",numLados,"lados es igual a",perimetro,"y el área es igual a",area,"unidades")

numLados = int(input("Ingrese el número de lados de la figura: "))
lado = float(input("Ingrese el tamaño del lado: "))

perimetro = calculoPerimetro(numLados, lado)
area = calculoArea(numLados, lado)

mostrarResultado(numLados, perimetro, area)
