class OperacionesAritmeticas:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def suma(self):
        print(self.a + self.b)

    def potencia(self):
        print(self.a ** self.b)

op = OperacionesAritmeticas(2, 2)
op.suma()

potencia = int(input("Ingrese valor para a: "))
potencia = int(input("Ingrese valor para b: "))

print("La potencia de a es", potencia ** potencia)

op.potencia()

