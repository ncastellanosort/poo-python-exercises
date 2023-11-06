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

def mostrarPeliculas():
    for n, peli in enumerate(peliculas):
        print(f'{n + 1}. {peli.__repr__peliculas__()}')

peliculas = []

while True:
    print('\n1. Agregar pelicula')
    print('2. Mostrar titulos de peliculas')
    print('3. Mostrar informacion de una pelicula en particular')
    print('4. Salir\n')

    txt = input('Selecciona una opcion: ')

    if txt == '1':
        nuevaPeli = agregarPelicula()
        peliculas.append(nuevaPeli)
        print('\nPelicula agregada!')

    elif txt == '2':
        print('\nTítulos de películas:\n')
        mostrarTitulos()

    elif txt == '3':
        print('\nPeliculas disponibles:\n')
        mostrarTitulos()

        indice = int(input('Selecciona el índice de la película: '))
        if 1 <= indice <= len(peliculas):
            print(peliculas[indice - 1].__repr__peliculas__())
        else:
            print('Índice no válido.')

    elif txt == '4':
        print('Finalizado')
        break
