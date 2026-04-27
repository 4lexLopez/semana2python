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

    def agregar_producto(self):
        while True: #Input de nombre del producto
            nombre = input("Digite el nombre del producto: ")
            if len(nombre):
                break
        while True: #Input de cantidad del producto
            try:
                cantidad = int(input("Digite la cantidad del producto: "))
                if(cantidad) > 0:
                    break  
            except ValueError:
                print("cantidad invalida, intente nuevamente.")
        while True: #Input de precio del producto
            try:
                precio = int(input("Digite el precio del producto: "))
                if(precio) > 0:
                    break  
            except ValueError:
                print("precio invalido, intente nuevamente.")
        producto = Producto(nombre, precio, cantidad)
        self.productos.append(producto)
        print("Producto agregado al inventario.")

    def buscar_producto(self, nombre_item):
        return next((item.nombre for item in self.productos if item.nombre == nombre_item), None)

    def calcular_valor_inventario(self):
        total = 0
        for item in self.productos:
            total += item.precio * item.cantidad
        return total

    def listar_productos(self):
        for item in self.productos:
            print(item)

def menu_principal(inventario: Inventario):
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
            if (opcion >0 and opcion <= 5):
                if opcion == 1:
                    inventario.agregar_producto()
                if opcion == 2:
                    buscar = input("Digite el nombre del producto a buscar: ")
                    print("Producto no encontrado\n") if inventario.buscar_producto(buscar) is None else print("Producto existente en el inventario\n")
                if opcion == 3:
                    print("\nInventario de productos:\n")
                    inventario.listar_productos()
                if opcion == 4:
                    print(f"Valor total de inventario es {inventario.calcular_valor_inventario()}")
                if opcion == 5:
                    break
            else:
                print("opcion no valida, intente nuevamente")
if __name__ == "__main__":
    inventario = Inventario()
    menu_principal(inventario)

    