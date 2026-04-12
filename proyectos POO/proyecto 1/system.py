class System:
  def __init__(self, name):
    self.name = name
    self.Inventario = []

  def item_stats(self):
      if not self.Inventario:
        print("NO HAY OBJETOS (actualmente xd)")

      for Objeto in self.Inventario: 
        print(f" Nombre:  {Objeto.name} , Precio: {Objeto.precio},  Stock: {Objeto.stock}")
      return None
  
  def inventory_stats(self):
    total_articulos = len(self.Inventario)

    print(f"Resumen de {self.name}")
    print(f"Total de artículos: {total_articulos}")

  def add_object_to_inventory(self,object_to_add):
    self.Inventario.append(object_to_add)
    print(f"Objeto {object_to_add.name} en la lista")
    return self.Inventario[-1]

  def remove_object(self, item):
    self.Inventario.remove(item)

  def get_object(self,nombre):
    for item in self.Inventario:
      if item.name == nombre:
        return item
    
      print(f"Object still not found (mucho ingles lol)")
      return None
    

  def search_object(self, name):
    for item in self.Inventario:
      if item.name == name:
        return item
    return None
