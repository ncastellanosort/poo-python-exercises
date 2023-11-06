class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def acelerar(self):
        print(f'el carro: {self.marca} esta acelerando')

    def frenar(self):
        print(f'el carro: {self.marca} esta frenando')

class Auto(Vehiculo):
    def __init__(self,marca, modelo, tipo, velocidad):
        super().__init__(marca, modelo)
        self.tipo = tipo
        self.velocidad = velocidad

    def acelerar(self):
        if self.velocidad > 50 and self.velocidad < 80:
            print(f'el carro: {self.marca} debe acelerar')
    
    def frenar(self):
        if self.velocidad >= 80:
            print(f'el carro: {self.marca} debe frenar')


velocidad = int(input('Dime la velocidad: '))
carro = Auto('mercedes', 2023, 'sedan', velocidad)

carro.acelerar()
carro.frenar()
        
