from tienda import Tienda
from producto import Producto
from tienda import Restaurante, Farmacia, Supermercado

def main():
    print("Bienvenido al sistema")
    nombre_tienda = input("Ingrese el nombre de la tienda: ")
    costo_delivery = float(input("Ingrese el costo de delivery: "))

    print("Tipos de tienda: 1) Restaurante  2) Farmacia  3) Supermercado")
    tipo = input("Seleccione el tipo de tienda (1/2/3): ")

    if tipo == "1":
        mi_tienda = Restaurante(nombre_tienda, costo_delivery)
    elif tipo == "2":
        mi_tienda = Farmacia(nombre_tienda, costo_delivery)
    elif tipo == "3":
        mi_tienda = Supermercado(nombre_tienda, costo_delivery)
    else:
        print("Tipo de tienda inválido.")
        return

   
    print(f"Tienda {mi_tienda.nombre} creada con costo de delivery {mi_tienda.costo_delivery}")

    while True:
        opcion_ingresar_producto = input("¿Desea ingresar un producto? (s/n): ").lower()
        if opcion_ingresar_producto not in ["s", "n"]:
            print("Opción no válida. Por favor, ingrese 's' o 'n'.")
            continue                
        if opcion_ingresar_producto == "s":
            nombre_producto = input("Ingrese el nombre del producto: ")
            while True:
                precio_producto = float(input("Ingrese el precio del producto: "))
                if precio_producto < 0:
                     print("El precio no puede ser negativo. Intente nuevamente.")
                else:
                     break
            while True:
                stock_producto = input("Ingrese el stock del producto (deje en blanco si no aplica): ")
                if stock_producto == "":
                    stock_producto = 0
                    break
                try:
                    stock_producto = int(stock_producto)
                    if stock_producto < 0:
                        print("El stock no puede ser negativo. Intente nuevamente.")
                    else:
                        break
                except ValueError:
                    print("Entrada inválida. Por favor, ingrese un número entero para el stock.")
            mi_tienda.ingresar_producto(nombre_producto, precio_producto, stock_producto)
        else:
            print("No se ingresará ningún producto.")
            break

    while True:
        print("\nOpciones de la Tiendas:")
        print("1. Listar productos")
        print("2. Realizar venta")
        print("3. Salir")
        opcion = input("Seleccione una opción (1-3): ")
        
        if opcion == "1":
            listado_productos = mi_tienda.listar_producto()
            print(listado_productos)
        elif opcion == "2":
            nombre_producto = input("Ingrese el nombre del producto a vender: ")
            while True:
                try:
                    cantidad = int(input("Ingrese la cantidad a vender: "))
                    if cantidad < 0:
                        print("La cantidad no puede ser negativa. Intente nuevamente.")
                    else:
                        break
                except ValueError:
                    print("Entrada inválida. Por favor, ingrese un número entero para la cantidad.")
            mi_tienda.realizar_venta(nombre_producto, cantidad)
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción entre 1 y 3.") 

main()            
       