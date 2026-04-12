from pelicula import Pelicula
from usuario import Usuario 

nombre_usuario = input("Introduce tu nombre:")
edad = int(input("Introduce tu edad:"))
ci = input("Introduce tu cedula: ")
correo = input("Introduce tu gmail (si no teneis solo ponle (no tengo), porfi):")

mi_usuario = Usuario(nombre_usuario, edad, ci, correo)


contador_id = 1

while True:
    print(f"Bienvenido {nombre_usuario} al Menú de peliculas") # mucho titulo, poco exito 
    print("Opciones disponibles")
    print("1. Agregar pelicula")
    print("2. Eliminar pelicula")
    print("3. Ver lista completa")
    print("4. Buscar por ID")
    print("5. Editar Título")
    print("6. Salir")

    option = input("seleccione opcion:")

    if option == "1":
        title = input("Titulo:")
        gender = input("Género:")
        age = input("Año de lanzamiento:")

        nueva_peli = Pelicula(title, contador_id, age, gender)
        mi_usuario.agregar_favorita(nueva_peli)

        contador_id += 1

    elif option == "2":
        name = input("Nombre de la peli:")

        mi_usuario.eliminar_pelicula(name)

    elif option == "3":
        mi_usuario.listar_favoritas()

    elif option == "4":
        print("Buscador por ID ") 
        id_buscado = int(input("Introduzca el ID de la pelicula:")) 
        encontrao = False # pos que vas a encontrar si ni has buscao xd

        for dp in mi_usuario.favoritos:
            if dp.id_peli == id_buscado:
                print(F"SIIIII... Pelicula encontrada: {dp}")
                encontrao = True
                break

        if not encontrao:
            print("Ese ID es más falso que un billete de 3$")

    elif option == "5":
        print("Editar título POR ID")
        id_edicion = int(input("ID de la pelicula a cambiar:"))

        peliculaxd = False

        for dpe in mi_usuario.favoritos:
            if dpe.id_peli == id_edicion:
                nuevo_titulo = input(f"Nuevo titulo para... {dpe.titulo}:")
                dpe.titulo = nuevo_titulo
                peliculaxd = True
                break 

        if not peliculaxd:
            print("Que es ese ID XDDDDD")

    elif option == "6":
        print("Chao we")
        break
    else: 
        print("Opcion no válida")


# producto hecho por mi (si claro xd)