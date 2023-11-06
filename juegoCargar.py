from abc import ABC, abstractmethod
import time

class TestInterface(ABC):
    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def cargando(self):
        pass

    @abstractmethod
    def ingresado(self):
        pass

class Juego(TestInterface):
    def __init__(self, nombre):
        super().__init__(nombre)

    def cargando(self):
        return f'Cargando...'

    def ingresado(self):
        return f'Ingresaste al juego, {self.nombre}'

while True:
    print('\n1. Serpiente')
    print('2. Solitario')
    print('3. Buscaminas')
    print('4. Salir')

    txt = input('\nIndice del juego: ')

    match txt:
        case '1':
            juego = Juego('Serpiente')
        case '2':
            juego = Juego('Solitario')
        case '3':
            juego = Juego('Buscaminas')
        case '4':
            print('\nFinalizado!')
            break

    if juego:

        print(juego.cargando())
        time.sleep(2)
        print(juego.ingresado())

        while True:
            print('1. Si')
            txt2 = input('\nDeseas salir?: ')
            if txt2 == '1':
                print('Saliendo...')
                time.sleep(2)
                break
