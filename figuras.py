from math import sqrt, pi, tan

class Figura:
    def __init__(self, num_lados, lado):
        self.num_lados = num_lados
        self.lado = lado
        self.perimetro = self.calculo_perimetro()
        self.area = self.calculo_area()

    def calculo_perimetro(self):
        return self.num_lados * self.lado

    def calculo_area(self):
        theta = pi / self.num_lados
        apotema = self.lado / (2 * tan(theta))
        area = (self.perimetro * apotema) / 2
        return area

    def mostrar_resultado(self):
        if self.num_lados <= 1:
            print("No existen poligonos de un solo lado")
        else:
            print(f"El perímetro de una figura de {self.num_lados} lados es igual a {self.perimetro} y el área es igual a {self.area} unidades")

num_lados = int(input("Ingrese el número de lados de la figura: "))
lado = float(input("Ingrese el tamaño del lado: "))

poligono = Figura(num_lados, lado)
poligono.mostrar_resultado()