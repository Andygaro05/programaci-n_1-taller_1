class Categoria:
    id = 0
    def __init__(self, nombre_categoria, descripcion):
        self.nombre_categoria = nombre_categoria
        self.descripcion = descripcion
        self.productos = []  # Lista de productos asociados a la categoría pq producto no conoce de categoria
        self.id = Categoria.id
        Categoria.id += 1

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

    def ver_id(self):
        print(f"{self.nombre_categoria}: ID {self.id}")

categorias = [Categoria("Construccion y Ferreteria", "La categoría de productos de Construcción y Ferretería incluye una amplia variedad de materiales, herramientas y suministros necesarios para la construcción, reparación y mantenimiento de edificaciones e infraestructuras. "), 
              Categoria("Pisos, Pinturas y Terminaciones", "La categoría de productos de Pisos, Pinturas y Terminaciones engloba una gama de materiales y productos diseñados para el acabado y embellecimiento de espacios interiores y exteriores"), 
              Categoria("Herramientas y maquinaria", "La categoría de Herramientas y Maquinaria abarca una extensa variedad de equipos esenciales para realizar tareas de construcción, reparación, mantenimiento y proyectos de bricolaje. "), 
              Categoria("Baño y Cocina", "La categoría de Baño y Cocina incluye una amplia gama de productos y accesorios diseñados para equipar y embellecer estos espacios esenciales del hogar. "),
              Categoria("Muebles", "La categoría de Muebles abarca una variedad de piezas diseñadas para amueblar y decorar espacios interiores y exteriores de hogares, oficinas y otros entornos."),
              Categoria("Decoración, Menaje E Iluminacion", "La categoría de Decoración, Menaje e Iluminación incluye una amplia gama de productos destinados a embellecer, equipar y dar vida a los espacios interiores y exteriores."),
              Categoria("Aire libre", "La categoría de Aire Libre incluye una variedad de productos diseñados para disfrutar y optimizar los espacios exteriores. ")]
