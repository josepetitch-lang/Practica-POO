class Pelicula:
    def __init__(self, titulo,id_peli, año, genero):
        self.titulo = titulo
        self.id_peli = id_peli
        self.año = año
        self.genero = genero
       

    def __str__(self):
      return f"Nombre: {self.titulo}, ID: {self.id_peli}, Año: {self.año}, Género: {self.genero}"
         