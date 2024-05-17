from Categoria import Lista_Categorias

class Producto:
    def __init__(self, id, nombre, descripcion, precio, categoria=None):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.cantidad = 0  # Cantidad inicial en bodega (por defecto 0)
        self.categoria = categoria
    def __repr__(self):
        return f"{self.nombre}"

    def mostrar_informacion(self):
        print(f"**Producto:** {self.nombre}")
        print(f"Descripción: {self.descripcion}")
        print(f"Precio: ${self.precio}")
        print(f"Cantidad en bodega: {self.cantidad}")
        if self.categoria:
            print(f"Categoría: {self.categoria.nombre_categoria}")

Lista_Productos = [Producto(1, "Silla Reclinable", "Espectacular silla amoblada para una persona la cual se reclina y cuenta con garantía de 12 meses.", 960000, Lista_Categorias[4] ),
                                    Producto(2, "Sofá Cama", "Sofá Cama con 3 posiciones, modo cama, reclinado o TV y modo sofá", 1200000, Lista_Categorias[4]),
                                    Producto(3, "Silla Computador", "Silla para escritorio hecha en tela y con soporte hasta de 80kg", 125000, Lista_Categorias[4]),
                                    Producto(4, "Biblioteca Horizontal", "Biblioteca horizontal multiusos color madera oscura, cuenta con seis espacios para almacenar", 560000, Lista_Categorias[4]),
                                    Producto(5, "Set de Herramientas Manuales de 250 Piezas", "Juego completo de herramientas que cuenta con 250 piezas", 209900, Lista_Categorias[2])]