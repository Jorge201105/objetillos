

class Producto:
    def __init__(self, nombre,precio,stock):
        self.__nombre = nombre
        self.__precio = precio
        if stock < 0:
            self.__stock = 0
        else:
            self.__stock = stock

    @property
    def nombre(self):
        return self.__nombre

    @property
    def precio(self):
        return self.__precio

    @property
    def stock(self):
        return self.__stock

    @stock.setter
    def stock(self,nuevo_stock):
        if nuevo_stock<0:
            self.__stock = 0
        else:
            self.__stock = nuevo_stock

    def __eq__(self, other):
        return isinstance(other, Producto) and self.nombre == other.nombre

"""
p1=Producto("lapiz",20,-20)        
print(p1.nombre)
print(p1.precio)
print(p1.stock)
"""

