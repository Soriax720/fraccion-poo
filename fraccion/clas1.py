class Fraccion(object):
    def __init__(self,numerador,denominador):
        self.numerador = numerador
        self.denominador = denominador
    def __add__(self, other):
        numerador = self.numerador + other.numerador
        denominador = self.denominador
        return Fraccion(numerador,denominador)



