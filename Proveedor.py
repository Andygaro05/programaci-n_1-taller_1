#proveedor.py
class Proveedor:
    def __init__(self, nombre_proveedor, telefono_proveedor, email_proveedor):
        self.nombre_proveedor = nombre_proveedor
        self.telefono_proveedor = telefono_proveedor
        self.email_proveedor = email_proveedor
        self.productos = []

    def agregar_producto(self, producto):
        if producto not in self.productos:
            self.productos.append(producto)

    def eliminar_producto(self, producto):
        if producto in self.productos:
            self.productos.remove(producto)

    def consultar_categoria(self, categoria):
        productos_categoria = []
        for producto in self.productos:
            if producto.categoria == categoria:
                productos_categoria.append(producto)
        return productos_categoria

    def mostrar_producto(self, producto):
        print(f"Nombre: {producto.nombre}")
        print(f"Descripción: {producto.descripcion}")
        print(f"Precio: {producto.precio}")

    def mostrar_informacion(self):  #describe los datos del proveedor
      print(f"**Proveedor:** {self.nombre_proveedor}")
      print(f"Teléfono: {self.telefono_proveedor}")
      print(f"Correo electrónico: {self.email_proveedor}")

    def mostrar_producto(self, producto):
      if producto not in self.productos:    #verifica que el producto exista
        raise ValueError(f"El producto {producto.nombre} no se encuentra en la lista de productos del proveedor {self.nombre_proveedor}")

      print(f"**Producto:** {producto.nombre}")
      print(f"Descripción: {producto.descripcion}")
      print(f"Precio: {producto.precio}")