

from abc import ABC,abstractmethod
from producto import Producto

class Tienda(ABC):
    def __init__(self, nombre , costo_delivery):
        self.__nombre = nombre
        self.__costo_delivery = costo_delivery
        self._productos = []
    @property
    def nombre(self):
        return self.__nombre
    @property
    def costo_delivery(self):
        return self.__costo_delivery
    
    ## metodos abstractos para las 3 tiendas
    
    @abstractmethod
    def ingresar_producto(self, nombre, precio, stock = 0):
        pass
    
    
    
    @abstractmethod
    def listar_producto(self):
        pass

    

    @abstractmethod
    def realizar_venta(self, nombre_producto,cantidad):
        pass


    ## Clases para cada tipo de tienda

class Restaurante(Tienda):
    def __init__(self, nombre, costo_delivery):
        super().__init__(nombre, costo_delivery)
    
    def ingresar_producto(self, nombre, precio, stock=0):
        for p in self._productos:
            if p.nombre ==
        nuevo_producto = Producto(nombre, precio, 0) ## restorante siempre con stock cero
        self._productos.append(nuevo_producto)

    def listar_producto(self):
        listado = " Productos en el restaurante:\n"
        for producto in self._productos:
            listado += f"Nombre: {producto.nombre}, Precio: {producto.precio}\n"
        return listado
    def realizar_venta(self, nombre_producto, cantidad):
        print(f"Venta de {nombre_producto} por {cantidad} unidades en el restaurante {self.nombre}.")



class Supermercado(Tienda):
    def __init__(self, nombre, costo_delivery):
        super().__init__(nombre, costo_delivery)
    
    def ingresar_producto(self, nombre, precio, stock=0):
        nuevo_producto = Producto(nombre, precio, stock)
        for i,producto in enumerate(self._productos):
            if producto == nuevo_producto:
                self._productos[i] += nuevo_producto
                print(f"Stock de {nombre} actualizado en el supermercado a {self._productos[i].stock}.")
                return
        self._productos.append(nuevo_producto)
        print(f"Producto {nombre} agregado al supermercado con un stock de {stock} unidades.")
        
    def listar_producto(self):
        listado = "Productos en el supermercado:\n"
        if not self._productos:
            listado += "No hay productos disponibles.\n"
        else:
            for producto in self._productos:
                stock_info = f" Stock: {producto.stock}"
                if producto.stock <10:
                    stock_info += " quedan menos de 10 productos"
                listado += f"Nombre: {producto.nombre}, Precio: {producto.precio}{stock_info}\n"
                

        return listado
          

        
    def realizar_venta(self, nombre_producto, cantidad):
        producto_encontrado = None  ## para definir esta variable, como nada o no encontrado  
        for producto in self._productos:
            if producto.nombre == nombre_producto:
                producto_encontrado = producto
                break
        if not producto_encontrado:
            print(f"Producto {nombre_producto} no encontrado en el supermercado {self.nombre}.")
            return
        if producto_encontrado.stock == 0:
            print(f"Producto {nombre_producto} no disponible en el supermercado {self.nombre}.")
            return
        cantidad_vender = min(cantidad, producto_encontrado.stock)
        producto_encontrado.stock -= cantidad_vender
        print(f"Venta de {cantidad_vender} unidades de {nombre_producto} realizada en el supermercado {self.nombre}.Stock restante : {producto_encontrado.stock}")

class Farmacia(Tienda):
    def __init__(self, nombre, costo_delivery):
        super().__init__(nombre, costo_delivery)
    def ingresar_producto(self, nombre, precio, stock=0):
        nuevo_producto = Producto(nombre, precio, stock)
        for i,producto in enumerate(self._productos):
            if producto == nuevo_producto:
                self._productos[i] += nuevo_producto
                print(f"Stock de {nombre} actualizado en la farmacia a {self._productos[i].stock}.")
                return
        self._productos.append(nuevo_producto)
        print(f"Producto {nombre} agregado a la farmacia con un stock de {stock} unidades.")

    def listar_producto(self):
        listado = "Productos en la farmacia:\n"
        if not self._productos:
            listado += "No hay productos disponibles.\n"
        else:
            for producto in self._productos:
                precio_info = f" Precio: {producto.precio}"
                if producto.precio > 15000:
                    precio_info += " Envío gratis al solicitar este producto"
                listado += f"Nombre: {producto.nombre}, {precio_info}\n"
        return listado

    def realizar_venta(self, nombre_producto, cantidad):
        if cantidad >3:
            print(f"En la farmacia {self.nombre} no se pueden vender más de 3 unidades del producto {nombre_producto}.")
            return 

        producto_encontrado = None
        for p in self._productos:
            if p.nombre == nombre_producto:
                producto_encontrado = p
                break
        if not producto_encontrado:
            print(f"Producto {nombre_producto} no encontrado en la farmacia {self.nombre}.")
            return  
        if producto_encontrado.stock == 0:
            print(f"Producto {nombre_producto} no disponible en la farmacia {self.nombre}.")
            return
        cantidad_vender = min(cantidad, producto_encontrado.stock)
        producto_encontrado.stock -= cantidad_vender
        print(f"Venta de {cantidad_vender} unidades de {nombre_producto} realizada en la farmacia {self.nombre}.stock restante : {producto_encontrado.stock}") 