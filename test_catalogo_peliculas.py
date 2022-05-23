#Importacion de clases
from dominio.Class_Pelicula import *
from servicio.Class_Catalogo_pelicula import Catalogo_Peliculas

opcion = None
while opcion != 4:
    try:
        print('Opciones:')
        print('1. Agregar pelicula')
        print('2. Leer pelicula')
        print('3. Eliminar pelicula')
        print('4. Salir pelicula')
        opcion=int(input("Escribe tu opcion (1-4) "))

        if opcion == 1:
            nombre_pelicula = input('Proporciona el nombre de la pelicula :')
            pelicula = Pelicula(nombre_pelicula)
            Catalogo_Peliculas.agregar_pelicula(pelicula)

        elif opcion ==2:
            Catalogo_Peliculas.listar_peliculas()

        elif opcion ==3:
            Catalogo_Peliculas.eliminar_peliculas()

    except Exception as e:
        print(f'Error {e}')
        opcion = None
 
else:
    print('Salimos del programa')