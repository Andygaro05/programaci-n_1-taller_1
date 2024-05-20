from categoria import categorias

class Producto:
    id = 1
    def __init__(self, nombre, descripcion, precio, categoria=None):
        self.id = Producto.id
        Producto.id += 1
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

productos = [Producto("Silla Reclinable", "Espectacular silla amoblada para una persona la cual se reclina y cuenta con garantía de 12 meses.", 960000, categorias[4] ),
                Producto("Sofá Cama", "Sofá Cama con 3 posiciones, modo cama, reclinado o TV y modo sofá", 1200000, categorias[4]),
                Producto("Silla Computador", "Silla para escritorio hecha en tela y con soporte hasta de 80kg", 125000, categorias[4]),
                Producto("Biblioteca Horizontal", "Biblioteca horizontal multiusos color madera oscura, cuenta con seis espacios para almacenar", 560000, categorias[4]),
                Producto("Set de Herramientas Manuales de 250 Piezas", "Juego completo de herramientas que cuenta con 250 piezas", 209900, categorias[2])]

#Definimos qué productos pertenecerán a las categorias
categorias[2].agregar_producto(productos[4])
categorias[4].agregar_producto(productos[0])
categorias[4].agregar_producto(productos[1])
categorias[4].agregar_producto(productos[2])
categorias[5].agregar_producto(productos[3])