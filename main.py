import os
from proveedor import Proveedor, proveedores
from producto import Producto, productos
from categoria import Categoria, categorias
from bodega import Bodega, bodegas
from flask import Flask, render_template, redirect, request, flash

#aplicación
app = Flask(__name__)

#Configuración de la librería para guardar las imagenes que se suban en la página de registro de productos
UPLOAD_FOLDER = 'static/fotos'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

#Rutas de la app
@app.route("/")
def ruta_raiz():
    return render_template("index.html", productos = productos, proveedores = proveedores)

#Página de producto
@app.route("/producto/<int:pid>")
def ruta_producto(pid):
    for producto in productos:
        if pid == producto.id:
            return render_template("producto.html", producto=producto)
    return redirect("/")
    
#Página de proveedor
@app.route("/proveedor/<int:pid>")
def ruta_proveedor(pid):
    for proveedor in proveedores:
        if pid == proveedor.id:
            return render_template("proveedor.html", proveedor=proveedor)
    return redirect("/")

#Página de categoria
@app.route("/categoria/<int:pid>")
def ruta_categoria(pid):
    for categoria in categorias:
        if pid == categoria.id:
            return render_template("categoria.html", categoria = categoria)
    return redirect("/")


#Página de bodega
@app.route("/bodega/<int:pid>")
def ruta_bodega(pid):
    for bodega in bodegas:
        if pid == bodega.id:
            return render_template("bodega.html", bodega = bodega, productos = productos)
    return redirect("/")

#Página para registrar productos
@app.route("/registrar_producto", methods=["POST"])
def registrar_producto():
    nombre = request.form.get("nombre")
    descripcion = request.form.get("descripcion")
    precio = float(request.form.get("precio"))
    cantidad = int(request.form.get("stock"))
    categoria_nombre = request.form.get("categoria")
    bodega_asignada = request.form.get("bodega")
    foto = request.files.get("foto")

    if foto and allowed_file(foto.filename):
        filename = foto.filename
        filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        foto.save(filepath)
    else:
        return "Error: El archivo no es válido"

    # Buscar la categoría por su nombre
    categoria = next((c for c in categorias if c.nombre_categoria == categoria_nombre), None)
    
    if categoria is None:
        return "Error: La categoría no existe"
    
    # Crear una nueva instancia de Producto y agregarla a la lista de productos
    nuevo_producto = Producto(nombre=nombre, descripcion=descripcion, precio=precio, categoria=categoria)
    productos.append(nuevo_producto)
    
    #Asignarle a una bodega el producto
    for bodega in bodegas:
        if bodega.nombre_bodega == bodega_asignada:
            bodega.agregar_producto(nuevo_producto, cantidad)

    return redirect("/")

#Página para registrar una categoria
@app.route("/registrar_categoria", methods = ["POST"])
def registro_categoria():
    nombre = request.form.get("nombre")
    descripcion = request.form.get("descripcion")

    nueva_categoria = Categoria(nombre_categoria= nombre, descripcion= descripcion)
    categorias.append(nueva_categoria)

    return redirect("/")

#registro proveedor
@app.route("/registrar_proveedor", methods= ["POST"])
def registro_proveedor():
    nombre = request.form.get("nombre")
    telefono = request.form.get("telefono")
    direccion = request.form.get("email")

    nuevo_proveedor = Proveedor(nombre= nombre, telefono= telefono, direccion= direccion)
    proveedores.append(nuevo_proveedor)

    return redirect("/")

#registro bodega
@app.route("/registrar_bodega", methods = ["GET"])
def registro_bodega():
    nombre = request.form.get("nombre")
    direccion = request.form.get("ubicacion")
    capacidad = request.form.get("capacidad_maxima")

    nueva_bodega = Bodega(nombre_bodega= nombre, direccion_bodega= direccion, capacidad_maxima= capacidad)
    bodegas.append(nueva_bodega)
    return redirect("/")

# Gestionar stock route
@app.route("/gestionar_stock", methods=["GET", "POST"])
def gestionar_stock():
    if request.method == "GET":
        # Renderiza la página inicial del formulario
        return render_template("stock_bodega.html", bodegas=bodegas, productos=productos)

    bodega_asignada_nombre = request.form.get("bodega")
    producto_nombre = request.form.get("producto")

    bodega_asignada = next((b for b in bodegas if b.nombre_bodega == bodega_asignada_nombre), None)

    if bodega_asignada:
        producto = next((p for p in bodega_asignada.productos if p.nombre == producto_nombre), None)
        if producto is not None:
            cantidad = producto.cantidad
            return render_template("gestion_stock_bodega.html", bodega=bodega_asignada, producto=producto, cantidad=cantidad)
        return "Error: El producto no existe en esta bodega"
    else:
        return redirect("/")



@app.route("/stock_bodega", methods=["GET"])
def stock_bodega():
    # Renderiza la página inicial del formulario
    return render_template("stock_bodega.html", bodegas=bodegas, productos=productos)


# Ruta para mostrar la página de registro de categorías
@app.route("/registrar_categoria", methods=["GET"])
def mostrar_formulario_registro_categoria():
    return render_template("registrar_categoria.html")

# Ruta para mostrar la página de registro de productos
@app.route("/registrar_producto", methods=["GET"])
def mostrar_formulario_registro_producto():
    return render_template("registro_producto.html", categorias = categorias, bodegas = bodegas)

# Ruta para mostrar la página de registro de proveedores
@app.route("/registrar_proveedor", methods=["GET"])
def mostrar_formulario_registro_proveedor():
    return render_template("registro_proveedor.html")

# Ruta para mostrar la página de registro de bodegas
@app.route("/registrar_bodega", methods=["GET"])
def mostrar_formulario_registro_bodega():
    return render_template("registro_bodega.html")

@app.route("/producto/retirar_stock", methods=["GET"])
def mostrar_formulario_retiro_prod():
    return render_template("retirar_producto.html", bodegas=bodegas)

#MANEJO DE STOCK
# Ruta para agregar stock a un producto existente
@app.route("/agregar_stock/<int:producto_id>", methods=["POST"])
def agregar_stock(producto_id):
    cantidad = int(request.form["cantidad"])

    # Buscar el producto por su ID
    for producto in productos:
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
    for producto in productos:
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
    valor_stock = [producto.precio * producto.cantidad for producto in productos]
    valor_total = sum(valor_stock)
    longitud_lista = len(valor_stock)
    return render_template("valor_total_stock.html", valor_total=valor_total, valor_stock = valor_stock, productos = productos, longitud_lista = longitud_lista)

@app.route("/retiro_stock", methods=["POST"])
def retirar_producto():
    bodega_escogida = request.form.get("bodega")
    nombre_producto = request.form.get("nombre")
    cantidad = int(request.form.get("cantidad"))

    for bodega in bodegas:
        if bodega.nombre_bodega == bodega_escogida:
            producto = next((p for p in bodega.productos if p.nombre == nombre_producto), None)
            if producto:
                try:
                    bodega.retirar_producto(producto, cantidad)
                    print(f"Producto {nombre_producto} retirado")
                except ValueError as e:
                    print(e)
            break

    return redirect("/")

#Programa principal
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)