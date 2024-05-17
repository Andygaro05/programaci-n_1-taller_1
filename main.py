from Proveedor import Proveedor, Lista_Proveedores
from Producto import Producto, Lista_Productos
from Categoria import Categoria, Lista_Categorias
from Bodega import Bodega
from flask import Flask, render_template, redirect

#aplicación
app = Flask(__name__)

#Rutas
@app.route("/")
def ruta_raiz():
    return render_template("index.html", productos = Lista_Productos, proveedores = Lista_Proveedores)


@app.route("/producto/<int:pid>")
def ruta_producto(pid):
    for producto in Lista_Productos:
        if pid == producto.id:
            return render_template("producto.html", producto=producto)
    return redirect("/")
    

@app.route("/proveedor/<name>")
def ruta_proveedor(name):
    for proveedor in Lista_Proveedores:
        if name == proveedor.nombre:
            return render_template("proveedor.html", proveedor=proveedor)
    return redirect("/")

@app.route("/registrar_producto", methods=["POST"])
def registrar_producto():
    nombre = request.form.get("nombre")
    descripcion = request.form.get("descripcion")
    precio = float(request.form.get("precio"))
    stock = int(request.form.get("stock"))
    categoria_nombre = request.form.get("categoria")
    
    # Buscar la categoría por su nombre
    categoria = next((c for c in Lista_Categorias if c.nombre_categoria == categoria_nombre), None)
    
    if categoria is None:
        return "Error: La categoría no existe"
    
    # Generar un nuevo ID para el producto
    nuevo_id = len(Lista_Productos) + 1
    
    # Crear una nueva instancia de Producto y agregarla a la lista de productos
    nuevo_producto = Producto(nuevo_id, nombre, descripcion, precio, stock, categoria)
    Lista_Productos.append(nuevo_producto)
    
    return redirect("/") 


# Otras importaciones y configuraciones...
# Otras importaciones y configuraciones...

# Ruta para mostrar la página de registro de productos
@app.route("/registrar_producto", methods=["GET"])
def mostrar_formulario_registro_producto():
    return render_template("registro_producto.html")

# Ruta para mostrar la página de registro de categorías
@app.route("/registrar_categoria", methods=["GET"])
def mostrar_formulario_registro_categoria():
    return render_template("registro_categoria.html")

# Ruta para mostrar la página de registro de proveedores
@app.route("/registrar_proveedor", methods=["GET"])
def mostrar_formulario_registro_proveedor():
    return render_template("registro_proveedor.html")

# Ruta para mostrar la página de registro de bodegas
@app.route("/registrar_bodega", methods=["GET"])
def mostrar_formulario_registro_bodega():
    return render_template("registro_bodega.html")

# Otras rutas y configuraciones...


# Otras importaciones y configuraciones...

# Ruta para agregar stock a un producto existente
@app.route("/agregar_stock/<int:producto_id>", methods=["POST"])
def agregar_stock(producto_id):
    cantidad = int(request.form["cantidad"])

    # Buscar el producto por su ID
    for producto in Lista_Productos:
        if producto.id == producto_id:
            producto.cantidad += cantidad
            # Redirigir a la página de producto con un mensaje de éxito
            return redirect(f"/producto/{producto_id}")

    # Si el producto no se encuentra, redirigir a la página principal con un mensaje de error
    flash("Producto no encontrado", "error")
    return redirect("/")

# Ruta para retirar stock de un producto existente
@app.route("/retirar_stock/<int:producto_id>", methods=["POST"])
def retirar_stock(producto_id):
    cantidad = int(request.form["cantidad"])

    # Buscar el producto por su ID
    for producto in Lista_Productos:
        if producto.id == producto_id:
            if producto.cantidad >= cantidad:
                producto.cantidad -= cantidad
                # Redirigir a la página de producto con un mensaje de éxito
                return redirect(f"/producto/{producto_id}")
            else:
                # Si no hay suficiente stock, mostrar un mensaje de error
                flash("Cantidad insuficiente en stock", "error")
                return redirect(f"/producto/{producto_id}")

    # Si el producto no se encuentra, redirigir a la página principal con un mensaje de error
    flash("Producto no encontrado", "error")
    return redirect("/")

# Ruta para calcular el valor total del stock
@app.route("/valor_total_stock", methods=["GET"])
def calcular_valor_total_stock():
    valor_total = sum(producto.precio * producto.cantidad for producto in Lista_Productos)
    return render_template("valor_total_stock.html", valor_total=valor_total)

# Otras rutas y configuraciones...



#Programa principal
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)