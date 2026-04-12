class Inventario:
  def __init__(self, identificador,objeto):
    self.identificador = identificador
    self.objeto = objeto
    self.lista = []

  def add_object(self, objeto):
    self.lista.append(objeto)

  def remove_object(self, objeto):
    self.lista.remove(objeto)

  def inventory_list(self):
    return self.lista

  def get_object(self):
     if not self.lista:
       print("No hay objetos a seleccionar")
       return None 
     
     print("Holaaa, seleccione su objeto (por numero)")
     
     for i, obj in enumerate(self.lista):
        print(f"{i}. {obj.name}")
        try:
           opcion = int(input("Ingrese el numero del objeto"))
           o_s = self.lista[opcion]
           return o_s
        except (ValueError, IndexError): 
          print("Seleccion Invalida")
          return None 
      

  def __str__(self):
      return f"Identificador culero: {self.identificador} | Objeto: {self.lista}"