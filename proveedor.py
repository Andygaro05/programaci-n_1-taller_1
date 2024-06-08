from producto import productos

class Proveedor:
    id_counter = 1

    def __init__(self, nombre, telefono, direccion):
        self.id = Proveedor.id_counter
        Proveedor.id_counter += 1
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion
        self.productos = []

    def __repr__(self):
        return f"Proveedor({self.nombre}, {self.telefono}, {self.direccion}, {self.productos})"

    def agregar_producto(self, producto):
        if producto not in self.productos:
            self.productos.append(producto)

    def eliminar_producto(self, producto):
        if producto in self.productos:
            self.productos.remove(producto)

#Creación de los proveedores
proveedores = [Proveedor("Maderas Anita", 3123800910, "maderas_anita@gmail.com"), 
                    Proveedor("Lupita Baldosas", 3127167148, "LupitaBaldosas@hotmail.com"), 
                    Proveedor("Casa Bonita", 3106172961, "CasaBonita@gmail.com"), 
                    Proveedor("Hogares de confianza", 3017263829, "HogaresConfianza34@hotmail.com"),
                    Proveedor("Cersei Castillo", 3728192678, "CerseiCas7000@gmail.com")]

#Asignación de productos a proveedores
proveedores[0].agregar_producto(productos[3])
proveedores[2].agregar_producto(productos[1])
proveedores[2].agregar_producto(productos[0])
proveedores[3].agregar_producto(productos[2])
proveedores[4].agregar_producto(productos[4])