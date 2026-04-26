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
    def __init__(self):
        self.productos = list()

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def buscar_producto(self, nombre):
        return nombre if nombre in self.productos else None

    def calcular_valor_inventario(self):
        return sum(self.productos)

    def listar_productos(self):
        for item in self.productos:
            print(item)

def menu_principal():
    while(True):
        try:
            opcion = int(input("MENU PRINCIPAL\n\n"
            "1. Agregar producto\n" \
            "2. Buscar producto\n" \
            "3. Listar productos\n" \
            "4. Calcular valor total del inventario\n" \
            "5. Salir\n\n" ))
        except ValueError:
            print("opcion no valida, intente nuevamente")
        else:
            if opcion == 5:
                break

if __name__ == "__main__":
    inventario = Inventario()
    menu_principal()

    