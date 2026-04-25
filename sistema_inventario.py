class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def __str__(self):
        return f"nombre: {self.nombre}, precio: {self.precio}, disponible: {self.cantidad}"

    def actualizar_precio(self, nuevoPrecio):
        if(isinstance(nuevoPrecio, int) and nuevoPrecio > 0):
            self.precio = nuevoPrecio

    def actualizar_cantidad(self, nuevaCantidad):
        if(isinstance(nuevaCantidad, int) and nuevaCantidad > 0):
            self.cantidad = nuevaCantidad

    def calcular_valor_total(self):
        return self.precio * self.cantidad
    
class Inventario:
    def agregar_producto(self, producto):
        pass

    def buscar_producto(self, nombre):
        pass

    def calcular_valor_inventario():
        pass

    def listar_productos():
        pass
    