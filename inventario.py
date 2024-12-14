class Inventario:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, nombre, cantidad):
        self.productos[nombre] = self.productos.get(nombre, 0) + cantidad
        print(f"Se agregaron {cantidad} unidades de '{nombre}'.")

    def actualizar_producto(self, nombre, cantidad):
        if nombre in self.productos:
            self.productos[nombre] = cantidad
            print(f"'{nombre}' actualizado a {cantidad} unidades.")
        else:
            print(f"'{nombre}' no existe en el inventario.")

    def eliminar_producto(self, nombre):
        if nombre in self.productos:
            del self.productos[nombre]
            print(f"'{nombre}' eliminado del inventario.")
        else:
            print(f"'{nombre}' no encontrado.")

    def mostrar_inventario(self):
        if self.productos:
            print("\nInventario actual:")
            for nombre, cantidad in self.productos.items():
                print(f"- {nombre}: {cantidad} unidades")
        else:
            print("El inventario está vacío.")

def main():
    inventario = Inventario()

    while True:
        print("\nOpciones:")
        print("1. Agregar producto")
        print("2. Actualizar producto")
        print("3. Eliminar producto")
        print("4. Mostrar inventario")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre del producto: ")
            try:
                cantidad = int(input("Cantidad: "))
                inventario.agregar_producto(nombre, cantidad)
            except ValueError:
                print("Por favor, ingrese un número válido para la cantidad.")
        elif opcion == "2":
            nombre = input("Nombre del producto: ")
            try:
                cantidad = int(input("Nueva cantidad: "))
                inventario.actualizar_producto(nombre, cantidad)
            except ValueError:
                print("Por favor, ingrese un número válido para la cantidad.")
        elif opcion == "3":
            nombre = input("Nombre del producto: ")
            inventario.eliminar_producto(nombre)
        elif opcion == "4":
            inventario.mostrar_inventario()
        elif opcion == "5":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
