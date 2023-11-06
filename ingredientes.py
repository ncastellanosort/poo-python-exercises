class Ingrediente:
    def __init__(self, nombreIngr, cantidad, unidad):
        self.__nombreIngr = nombreIngr
        self.__cantidad = cantidad
        self.__unidad = unidad

    @property
    def nombreIngr(self):
        return self.__nombreIngr

    @nombreIngr.setter
    def nombreIngr(self, nuevoNm):
        self.__nombreIngr = nuevoNm

    @property
    def cantidad(self):
        return self.__cantidad

    @cantidad.setter
    def cantidad(self,nuevaCan):
        self.__cantidad = nuevaCan

    @property
    def unidad(self):
        return self.__unidad

    @unidad.setter 
    def unidad(self, nuevaUn):
        self.__unidad = nuevaUn


class pasoPreparacion(Ingrediente):
    def __init__(self,nombreIngr, cantidad, unidad, pasosPrepa):
        super().__init__(nombreIngr, cantidad, unidad)
        self.__pasosPrepa = pasosPrepa

    @property
    def pasosPrepa(self):
        return self.__pasosPrepa

    @pasosPrepa.setter 
    def pasosPrepa(self, nuevoPasosP):
        self.__pasosPrepa = nuevoPasosP


class Receta(pasoPreparacion):
    def __init__(self, nombre, categoria, nombreIngr, cantidad, unidad, pasosPrepa):
        super().__init__(nombreIngr, cantidad, unidad, pasosPrepa)
        self.__nombre = nombre
        self.__categoria = categoria

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter 
    def nombre(self, nuevoNmbre):
        self.__nombre = nuevoNmbre

    @property
    def categoria(self):
        return self.__categoria

    @categoria.setter 
    def categoria(self, nuevaCate):
        self.__categoria = nuevaCate

    def __repr__(self):
        return f'\nNombre de la receta: {self.nombre}\nCategoria: {self.categoria}\nNombre del ingrediente: {self.nombreIngr}\nCantidad: {self.cantidad}\nUnidad: {self.unidad}\nPasos preparacion: {self.pasosPrepa}'
    
    
    def editarReceta(self):
        self.nombre = input('Dime el nuevo nombre: ')
        self.categoria = input('Dime la nueva categoria: ')
        self.nombreIngr = input('Dime el nuevo nombre del ingrediente: ')
        self.cantidad = int(input('Dime la nueva cantidad: '))
        self.unidad = input('Dime la nueva unidad: ')
        self.pasosPrepa = input('Dime los nuevos pasos de preparacion: ')
        
        return Receta(self.nombre, self.categoria, self.nombreIngr, self.cantidad, self.unidad, self.pasosPrepa)


def mostrarReceta():
    for i, receta in enumerate(recetas):
        print(f'{i + 1}. {receta}')


def ingresarReceta():
    nombre = input('Dime el nombre de la receta: ')
    categoria = input('Dime la categoria de la receta: ')
    nombreIngr = input('Dime el nombre del ingrediente: ')
    cantidad = int(input('Dime la cantidad: '))
    unidad = input('Dime la unidad: ')
    pasosPrepa = input('Dime los pasos de preparacion: \n')
    return Receta(nombre,categoria,nombreIngr,cantidad,unidad,pasosPrepa)


recetas = []

while True:
    print('\n')
    print('1. Crear receta')
    print('2. Ver recetas')
    print('3. Editar receta')
    print('4. Salir\n')
    
    txt = input('Selecciona lo que quieres hacer: ')


    match txt:
        case '1':
            nuevaReceta = ingresarReceta()
            recetas.append(nuevaReceta)
            print('Receta creada!')

        case '2':
            if len(recetas) == 0:
                print('Debes ingresar las recetas')
            else:
                mostrarReceta()
    
        case '3':
            print('\nEsta es la lista de recetas:\n')
            mostrarReceta()
            print()
            txt = int(input('Ingresa el indice de la receta a editar: '))
            Receta.editarReceta(recetas[txt-1])

        case '4':
            print('Finalizado')
            break

        case other:
            print('Ingresa un indice valido.')



    






