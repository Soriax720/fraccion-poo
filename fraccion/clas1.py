class Fraccion(object):
    def __init__(self,numerador,denominador):
        self.numerador = numerador
        self.denominador = denominador
    def __add__(self, other):
        numerador = self.numerador + other.numerador
        denominador = self.denominador
        return Fraccion(numerador,denominador)
    def __str__(self):
        return f"{self.numerador}/{self.denominador}"
    def __sub__(self, other):
        numerador = self.numerador - other.numerador
        denominador = self.denominador
        return Fraccion(numerador,denominador)
    def __mul__(self, other):
        numerador = self.numerador * other.numerador
        denominador = self.denominador
        return Fraccion(numerador,denominador)

"""

"""
f = Fraccion(2,3)
e = Fraccion(5,3)
print(f * e)