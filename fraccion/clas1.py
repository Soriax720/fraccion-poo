class Fraccion(object):
    def __init__(self,numerador,denominador):
        self.numerador = numerador
        self.denominador = denominador

    def __add__(self, other):
        numerador = self.numerador + other.numerador
        denominador = self.denominador
        return Fraccion(numerador,denominador)
    
    
    
    def __sub__(self, other):
        numerador = self.numerador - other.numerador
        denominador = self.denominador
        return Fraccion(numerador,denominador)
    
    def __mul__(self, other):
        numerador = self.numerador * other.numerador
        denominador = self.denominador
        return Fraccion(numerador,denominador)
    
    def __truediv__(self,other):
        numerador = self.numerador / other.numerador
        denominador = self.denominador
        return Fraccion(numerador,denominador)
    def __str__(self):
        if self.denominador == 1:
            return f"{self.numerador}"
        else:
            f"{self.numerador}/{self.denominador}"
"""
f = Fraccion(10,1)
e = Fraccion(5,1)
print(f + e)
"""