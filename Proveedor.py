#proveedor.py
from Producto import Lista_Productos
class Proveedor:
    def __init__(self, nombre, telefono, email):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email
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
      print(f"**Proveedor:** {self.nombre}")
      print(f"Teléfono: {self.telefono}")
      print(f"Correo electrónico: {self.email}")

    def mostrar_producto(self, producto):
      if producto not in self.productos:    #verifica que el producto exista
        raise ValueError(f"El producto {producto.nombre} no se encuentra en la lista de productos del proveedor {self.nombre}")

      print(f"**Producto:** {producto.nombre}")
      print(f"Descripción: {producto.descripcion}")
      print(f"Precio: {producto.precio}")

#Creación de los proveedores
Lista_Proveedores = [Proveedor("Maderas Anita", 3105916884, "maderas_anita@gmail.com"), 
                    Proveedor("Lupita Baldosas", 3127167148, "LupitaBaldosas@hotmail.com"), 
                    Proveedor("Casa Bonita", 3106172961, "CasaBonita@gmail.com"), 
                    Proveedor("Hogares de confianza", 3017263829, "HogaresConfianza34@hotmail.com"),
                    Proveedor("Cersei Castillo", 3728192678, "CerseiCas7000@gmail.com")]

#Asignación de productos a proveedores
Lista_Proveedores[0].agregar_producto(Lista_Productos[3])
Lista_Proveedores[2].agregar_producto(Lista_Productos[1])
Lista_Proveedores[2].agregar_producto(Lista_Productos[0])
Lista_Proveedores[3].agregar_producto(Lista_Productos[2])
Lista_Proveedores[4].agregar_producto(Lista_Productos[4])