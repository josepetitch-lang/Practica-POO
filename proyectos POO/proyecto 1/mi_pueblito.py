from system import System
from object import Object
from inventory import Inventario 
import time

mi_inventario = Inventario(identificador = "Mi Pueblito", objeto = None)
sistema = System("Inventario")
sistema.Inventario = mi_inventario.lista


print(f"Bienvenido a: {mi_inventario.identificador}")
while True: 
  print("1. Agregar objeto ")
  print("2. Ver objetos (stats)")
  print("3. Ver inventario (stats sin terminar)")
  print("4. Buscar objeto ")
  print("5. Eliminar objeto")
  print("6. Salir")
  opcion = input("Seleccione una opcion: ")

  if opcion == "1":
   nombre = input("Nombre del objeto (pon algo que exista o te balatreo [referencia]):")
   precio = int(input("Precio: "))
   tipo = input("¿Que tipo es?:")
   stock = input("¿Stock inicial?:")

   nuevo_item = Object(nombre,tipo,precio,stock)
   mi_inventario.lista.append(nuevo_item)
   print("Tome un cafecito mientras carga")
   time.sleep(2)
   print("Siga esperando")
   time.sleep(2)
   print()
   print(f"\n {nombre} agregado (exitosamente por ahora)")

  elif opcion == "2":
   print("PRODUCTOS:")
   sistema.item_stats()

  elif opcion == "3":
    sistema.inventory_stats()

  elif opcion == "4":
    inter = input("Ingrese el nombre a buscar:")
    encontrado = sistema.search_object(inter)

    if inter in sistema.Inventario:
      print("el objeto está.... (*inserte musicasuspenso.mp4*)")
      time.sleep(5)
      print(f"Resultado: {inter}.... ENCONTRADO")
    else:
         print("el objeto está.... (*inserte musicasuspenso.mp4*)")
         time.sleep(5)
         print("Lo lamento, el producto no fue encontrado")
   
  elif opcion == "5":
    name = input("Nombre del producto a eliminar:")
    item_dele_alli = sistema.search_object(name)

    if item_dele_alli:
      mi_inventario.remove_object(item_dele_alli)
      print(f"{name} ha sido eliminado")
    else:
      print("nisiquiera existe xd")
   
  elif opcion == "6":
    print("Hoy no y mañana menos")
    time.sleep(2)
    break
  else:
    print("Opcion invalida")