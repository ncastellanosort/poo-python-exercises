from abc import ABC, abstractclassmethod

class Universidad(ABC):
    @abstractclassmethod
    def consultarInfo(self):
        pass

class Persona:
    def __init__(self, nroId, tipoId, nombres, apellidos, direccion):
        self.nroId = nroId
        self.tipoId = tipoId
        self.nombres = nombres
        self.apellidos = apellidos
        self.direccion = direccion

class Docente(Persona, Universidad):
    def __init__(self,nroId,tipoId, nombres, apellidos, direccion, escalafon):
        super().__init__(nroId, tipoId, nombres, apellidos, direccion)
        self.escalafon = escalafon
    
    def consultarInfo(self):
        print(f'\nNumero id: {self.nroId}\nTipo id: {self.tipoId}\nNombres: {self.nombres}\nApellidos: {self.apellidos}\nDireccion: {self.direccion}\nEscalafon: {self.escalafon}')

    def __repr__(self):
        return f'\nNumero id: {self.nroId}\nTipo id: {self.tipoId}\nNombres: {self.nombres}\nApellidos: {self.apellidos}\nDireccion: {self.direccion}\nEscalafon: {self.escalafon}'


class Estudiante(Persona, Universidad):
    def __init__(self,nroId,tipoId, nombres, apellidos, direccion, codigo):
        super().__init__(nroId, tipoId, nombres, apellidos, direccion)
        self.codigo = codigo

    def consultarInfo(self):
        print(f'\nNumero id: {self.nroId}\nTipo id: {self.tipoId}\nNombres: {self.nombres}\nApellidos: {self.apellidos}\nDireccion: {self.direccion}\nCodigo: {self.codigo}')


    def __repr__(self):
        return f'\nNumero id: {self.nroId}\nTipo id: {self.tipoId}\nNombres: {self.nombres}\nApellidos: {self.apellidos}\nDireccion: {self.direccion}\nCodigo: {self.codigo}'

class Administrativo(Persona, Universidad):
    def __init__(self,nroId,tipoId, nombres, apellidos, direccion, salario):
        super().__init__(nroId, tipoId, nombres, apellidos, direccion)
        self.salario = salario

#hacer el repr para administrativos, matricula y mostrar lista estudiantes para admin

estudiantesLista = []
docentesLista = []
adminsLista = []

def ingresarEstu():
    numid = input('Dime el numero de id: ')
    tpid = input('Dime el tipo del id: ')
    nombre = input('Dime el nombre del Estudiante: ')
    apel = input('Dime los apellidosdel Estudiante: ')
    direc = input('Dime la direccion: ')
    cod = input('Dime el codigo del Estudiante: ')
    return Estudiante(numid, tpid, nombre, apel, direc, cod)

def mostrarEstu():
    for n, estudi in enumerate(estudiantesLista):
        print(f'{n + 1}. {estudi}')

def ingresarDoc():
    numid = input('Dime el numero de id: ')
    tpid = input('Dime el tipo del id: ')
    nombre = input('Dime el nombre del Docente: ')
    apel = input('Dime los apellidos del Docente: ')
    direc = input('Dime la direccion: ')
    esc = input('Dime el escalafon del Docente: ')
    return Docente(numid, tpid, nombre, apel, direc, esc)

def mostrarDoc():
    for n, docen in enumerate(docentesLista):
        print(f'{n + 1}. {docen}')


def ingresarAdm():
    numid = input('Dime el numero de id: ')
    tpid = input('Dime el tipo del id: ')
    nombre = input('Dime el nombre del Administrativo: ')
    apel = input('Dime los apellidos del Administrativo: ')
    direc = input('Dime la direccion: ')
    sal = input('Dime el salario del Administrativo: ')
    return Administrativo(numid, tpid, nombre, apel, direc, sal)

def mostrarAdmi():
    for n, adm in enumerate(adminsLista):
        print(f'{n + 1}. {adm}')

while True:

    print('1. Ingresar Estudiantes')
    print('2. Ingresar Docentes')
    print('3. Ingresar Administrativos')
    print('4. Ver lista Estudiantes')
    print('5. Ver lista Docentes')
    print('6. Ver lista Administrativos')
    print('7. Salir')

    txt = input('Selecciona lo que quieres hacer: ')

    match txt:
        case '1':
            nuevoEst = ingresarEstu()
            estudiantesLista.append(nuevoEst)
            print('Estudiante agregado!')

        case '2':
            nuevoDoc = ingresarDoc()
            docentesLista.append(nuevoDoc)
            print('Docente agregado!')

        case '3':
            nuevoAdm = ingresarAdm()
            adminsLista.append(nuevoAdm)
            print('Administrativo agregado!')
           
        case '4':
            if len(estudiantesLista) == 0:
                print('Debes agregar estudiantes.')
            else:
                mostrarEstu()
        
        case '5':
            if len(docentesLista) == 0:
                print('Debes agregar docentes.')
            else: 
                mostrarDoc()

        case '6':
            if len(adminsLista) == 0:
                print('Debes agregar administrativos.')
            else:
                mostrarAdmi()

        case '7':
            print('Finalizado')
            break
        
