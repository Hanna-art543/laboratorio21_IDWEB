import math

class Figura:
    def calcularPerimetro(self):
        pass
    
    def calcularArea(self):
        pass
        

class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcularPerimetro(self):
        return 2 * (self.base + self.altura)
    
    def calcularArea(self):
        return self.base * self.altura
    

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def calcularPerimetro(self):
        return 2 * math.pi * self.radio
    
    def calcularArea(self):
        return math.pi * self.radio ** 2
    

class Triangulo(Figura):
    def __init__(self, lado1, lado2, lado3, base, altura):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
        self.base = base
        self.altura = altura

    def calcularPerimetro(self):
        return self.lado1 + self.lado2 + self.lado3
    
    def calcularArea(self):
        return self.base * self.altura / 2


lista = [
    Rectangulo(5, 3),    
    Circulo(2),         
    Triangulo(3, 4, 5, 4, 3)  
]

for figura in lista:
    print(f"{figura.__class__.__name__}:")
    print(f"Área: {round(figura.calcularArea(), 2)}")
    print(f"Perímetro: {round(figura.calcularPerimetro(), 2)}")