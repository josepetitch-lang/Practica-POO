class Object():
  def __init__(self, name, tipo, precio, stock):
    self.name = name
    self.tipo = tipo
    self.precio = precio
    self.stock = stock

  def __str__(self):
    return f"Nombre: {self.name}, Precio: {self.price}, clasificacion: {self.clasificacion}"
  
  def _vida_(self):
    return self.name
    