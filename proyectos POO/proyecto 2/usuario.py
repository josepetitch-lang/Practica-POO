class Usuario:
    def __init__(self, nombre, edad, ci, correo):
        self.nombre = nombre
        self.edad = edad
        self.ci = ci
        self.correo = correo
        self.favoritos = []

   
    def agregar_favorita(self,pelicula):
      for p in self.favoritos:
         if p.id_peli == pelicula.id_peli:
            return f"Error, ese ID {pelicula.id_peli} ya existe"

      if pelicula not in self.favoritos:
         self.favoritos.append(pelicula)
         print(f"{pelicula.titulo} agregada a favoritos (mucho titulo pa tan poco exito)")
      else:
         print(f"{pelicula.titulo} ya está en favoritos")


    def listar_favoritas(self):
       print(f" Favoritos de {self.nombre}")
       if not self.favoritos:
          print("No hay nada") #le paso la peli a mis ganas de vivir (uy para así no)
       for du in self.favoritos:
          print(du)  # nombre tomado por trauma (lol, ya le tiene miedo a un diferencial) 

    def eliminar_pelicula(self, nombre_pelicula):
       for peli in self.favoritos:
         if peli.titulo == nombre_pelicula:
            self.favoritos.remove(peli)
            print("Y esa película?... No he oido de ella") # si lo has hecho 
         