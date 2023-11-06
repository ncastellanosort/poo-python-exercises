class Pelicula:
    def __init__(self, titulo, director, genero):
        self.titulo = titulo
        self.director = director
        self.genero = genero

    def __repr__titulo__(self):
        return f'Titulo: {self.titulo}\n'

    def __repr__peliculas__(self):
        return f'\nTitulo: {self.titulo}\nDirector: {self.director}\nGenero: {self.genero}'

def agregarPelicula():
    titulo = input('Dime el titulo de la pelicula: ')
    director = input('Dime el director de la pelicula: ')
    genero = input('Dime el genero de la pelicula: ')
    return Pelicula(titulo, director, genero)


def mostrarTitulos():
    for n, peli in enumerate(peliculas):
        print(f'{n + 1}. {peli.__repr__titulo__()}')

def mostrarPelicula():
    for n, peli in enumerate(peliculas):
        print(f'{n + 1}. {peli.__repr__peliculas__()}')

peliculas = []

while True:
    print('\n1. Agregar pelicula')
    print('2. Buscar pelicula por genero')
    print('3. Mostrar informacion de una pelicula en particular')
    print('4. Salir\n')

    txt = input('Selecciona una opcion: ')

    match txt:
        case '1':
            nuevaPeli = agregarPelicula()
            peliculas.append(nuevaPeli)
            print('\nPelicula agregada!')

        case '2':
            pass

        case '3':
            print('\nPeliculas agregadas: \n')
            mostrarTitulos()

            txt = int(input('Selecciona el indice de la pelicula: '))

            print(peliculas[txt - 1].__repr__peliculas__()) 

        case '4':
            print('Finalizado')
            break







