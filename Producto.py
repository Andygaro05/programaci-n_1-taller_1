class Producto:
    def __init__(self, nombre, descripcion, precio, categoria=None):
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.cantidad = 0  # Cantidad inicial en bodega (por defecto 0)
        self.categoria = categoria

    def mostrar_informacion(self):
        print(f"**Producto:** {self.nombre}")
        print(f"Descripción: {self.descripcion}")
        print(f"Precio: ${self.precio}")
        print(f"Cantidad en bodega: {self.cantidad}")
        if self.categoria:
            print(f"Categoría: {self.categoria.nombre_categoria}")