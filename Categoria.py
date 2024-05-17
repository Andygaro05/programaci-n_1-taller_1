class Categoria:
    def __init__(self, nombre_categoria):
        self.nombre_categoria = nombre_categoria
        self.productos = []  # Lista de productos asociados a la categoría pq producto no conoce de categoria

    def __repr__(self):
        return f"{self.nombre_categoria}"

    def agregar_producto(self, producto):
        if producto not in self.productos:
            self.productos.append(producto)

    def eliminar_producto(self, producto):
        if producto in self.productos:
            self.productos.remove(producto)

    def mostrar_productos(self):
        if not self.productos:
            print(f"La categoría {self.nombre_categoria} no tiene productos asociados.")
            return

        print(f"**Productos en la categoría {self.nombre_categoria}:**")
        for producto in self.productos:
            print(f"- {producto.nombre}")

    def mostrar_informacion(self):  #da los datos de la categoria y cuantos productos contiene
      print(f"**Categoría:** {self.nombre_categoria}")
      print(f"Cantidad de productos asociados: {len(self.productos)}")

Lista_Categorias = [Categoria("Construccion y Ferreteria"), 
                   Categoria("Pisos.Pinturas y Terminaciones"), 
                   Categoria("Herramientas y maquinaria"), 
                   Categoria("Baño. Cocina"),
                   Categoria("Muebles"),
                   Categoria("Decoración. Menaje E Iluminacion"),
                   Categoria("Aire libre")]