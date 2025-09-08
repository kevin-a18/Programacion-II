import math

class Circulo2D:
    def __init__(self, x=0, y=0, radio=1):
        self.x = x
        self.y = y
        self.radio = radio

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getRadio(self):
        return self.radio

    def getArea(self):
        return math.pi * self.radio ** 2

    def getPerimetro(self):
        return 2 * math.pi * self.radio

    # Punto dentro del círculo
    def contiene(self, px, py):
        distancia = math.sqrt((px - self.x) ** 2 + (py - self.y) ** 2)
        return distancia <= self.radio

    # Círculo dentro de otro
    def contieneCirculo(self, otro):
        distancia = math.sqrt((otro.x - self.x) ** 2 + (otro.y - self.y) ** 2)
        return distancia + otro.radio <= self.radio

    # Círculos que se sobreponen
    def sobrepone(self, otro):
        distancia = math.sqrt((otro.x - self.x) ** 2 + (otro.y - self.y) ** 2)
        return distancia < (self.radio + otro.radio)

# Programa de prueba
if __name__ == "__main__":
    c1 = Circulo2D(2, 0, 1)
    
    print("Área:", c1.getArea())
    print("Perímetro:", c1.getPerimetro())
    print("c1.contiene(2.5, 0):", c1.contiene(2.5, 0))
    print("c1.contiene(Circulo2D(2, 0, 0.5)):", c1.contieneCirculo(Circulo2D(2, 0, 0.5)))
    print("c1.sobrepone(Circulo2D(0, 0, 2)):", c1.sobrepone(Circulo2D(0, 0, 2)))
