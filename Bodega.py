from Producto import Lista_Productos

class Bodega:
    def __init__(self, nombre_bodega, direccion_bodega, capacidad_maxima):
        self.nombre_bodega = nombre_bodega
        self.direccion_bodega = direccion_bodega
        self.capacidad_maxima = capacidad_maxima
        self.productos = []

    def agregar_producto(self, producto, cantidad): # Agrega un producto a la bodega, especificando la cantidad a ingresar.

        if cantidad <= 0:
            raise ValueError("La cantidad debe ser un número positivo")

        if len(self.productos) + cantidad > self.capacidad_maxima:
            raise ValueError(f"No se puede agregar la cantidad solicitada, se excede la capacidad máxima de la bodega ({self.capacidad_maxima})")

        if producto not in self.productos:
            self.productos.append(producto)

        producto_existente = self.obtener_producto(producto)
        producto_existente.cantidad += cantidad

    def retirar_producto(self, producto, cantidad): #Retira un producto de la bodega, especificando la cantidad a retirar.
      if cantidad <= 0:
          raise ValueError("La cantidad debe ser un número positivo")

      producto_existente = self.obtener_producto(producto)
      if producto_existente is None:
          raise ValueError(f"El producto {producto.nombre} no se encuentra en la bodega")

      if cantidad > producto_existente.cantidad:
          raise ValueError(f"No se puede retirar la cantidad solicitada, la bodega solo tiene {producto_existente.cantidad} unidades de {producto.nombre}")

      producto_existente.cantidad -= cantidad

      if producto_existente.cantidad == 0:
          self.productos.remove(producto)

    def consultar_categoria(self, categoria):
        productos_categoria = []
        for producto in self.productos:
            if producto.categoria == categoria:
                productos_categoria.append(producto)
        return productos_categoria

    def obtener_producto(self, producto):
      for producto_bodega in self.productos:
        if producto_bodega == producto:
            return producto_bodega
      return None

    def tiene_productos_categoria(self, categoria):
        for producto in self.productos:
            if producto.categoria == categoria:
                return True
        return False

    def mostrar_productos(self):
       if not self.productos:
            print("La bodega no tiene productos registrados.")
            return
       else:
          print("**Productos en bodega:**")
          for producto in self.productos:
              print(f"- {producto.nombre} ({producto.cantidad} unidades)")

    def mostrar_informacion(self): # Muestra la información de la bodega.
        print(f"**Bodega:** {self.nombre_bodega}")
        print(f"Dirección: {self.direccion_bodega}")
        print(f"Capacidad máxima: {self.capacidad_maxima} unidades")
        print(f"Cantidad actual de productos: {len(self.productos)}")

#Creación de bodegas
Lista_bodega = [Bodega("MaximBog", "Cali, Calle 104 #90-88", 30), 
                Bodega("Sin Limites", "Cali, Cra 13 #45-52", 50), 
                Bodega("Orenta", "Cali, Calle 50 #106-99", 20),
                Bodega("De Norte a Sur", "Cali, Cra 17 #10-20", 13),
                Bodega("Samelene", "Cali Cra 25 #11-25", 40)]

#Adición de productos en la bodega
Lista_bodega[0].agregar_producto(Lista_Productos[0], 5)
Lista_bodega[1].agregar_producto(Lista_Productos[1], 12)
Lista_bodega[2].agregar_producto(Lista_Productos[2], 10)
Lista_bodega[3].agregar_producto(Lista_Productos[3], 2)
Lista_bodega[4].agregar_producto(Lista_Productos[4], 17)