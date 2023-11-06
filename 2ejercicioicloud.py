class InstrumentosMusicales:
    def __init__(self, nombre):
        self.nombre = nombre

    def tocar(self):
        pass

    def afinar(self):
        pass
    
        

class InstruOrquesta(InstrumentosMusicales):
    def __init__(self, nombre, seccion, afinacion):
        super().__init__(nombre)
        self.seccion = seccion
        self.afinacion = afinacion

    def tocar(self):
        print(f'Se esta tocando el instrumento: {self.nombre}')

    def afinar(self):
        print(f'El instrumento se afina de esta forma:  {self.afinacion}')

    def ritmos(self):
        print(f'Estos son los ritmos musicales mas usados en {self.nombre}: {self.seccion}')


instrumento = InstruOrquesta('saxofon','re mi fa sol', 'en una app')


instrumento.tocar()
instrumento.afinar()
instrumento.ritmos()
