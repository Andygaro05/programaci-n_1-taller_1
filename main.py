import os
from proveedor import Proveedor, proveedores
from producto import Producto, productos
from categoria import Categoria, categorias
from bodega import Bodega, bodegas
from flask import Flask, render_template, redirect, request, flash, url_for

#aplicación
app = Flask(__name__)
app.secret_key = 'supersecretkey'

#Configuración de la librería para guardar las imágenes que se suban en la página de registro de productos
UPLOAD_FOLDER = 'static/fotos'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

#Rutas de la app
@app.route("/")
def ruta_raiz():
    return render_template("index.html", productos = productos, proveedores = proveedores)

#Menú principal para las opciones de los productos
@app.route("/productos")
def menu_productos():
    return render_template("menu_productos.html") #botones: listado de productos, registrar producto, retirar producto y valor total de stock

#Página con todos los productos
@app.route("/listado_productos")
def lista_productos():
    return render_template("listado_productos.html", productos=productos)

#Página de producto
@app.route("/producto/<int:pid>")
def ruta_producto(pid):
    for producto in productos:
        if pid == producto.id:
            return render_template("producto.html", producto=producto)
    return redirect("/")

"""@app.route("/proveedores")
def menu_proveedores():
    return render_template("menu_proveedores.html")"""

@app.route("/proveedores/listado_proveedores")
def lista_proveedores():
    return render_template("listado_proveedores.html", proveedores = proveedores)

#Página de proveedor individual
@app.route("/proveedor/<int:pid>")
def ruta_proveedor(pid):
    for proveedor in proveedores:
        if pid == proveedor.id:
            return render_template("proveedor.html", proveedor=proveedor)
    return redirect("/")

@app.route("/categorias")
def menu_categorias():
    return render_template("menu_categorias.html")

@app.route("/categorias/listado_categorias")
def lista_categorias():
    return render_template("listado_categorias.html", categorias = categorias)

#Página de categoria individual
@app.route("/categoria/<int:pid>")
def ruta_categoria(pid):
    for categoria in categorias:
        if pid == categoria.id:
            return render_template("categoria.html", categoria = categoria)
    return redirect("/")

@app.route("/bodegas")
def menu_bodegas():
    return render_template("menu_bodegas.html")

@app.route("/bodegas/listado_bodegas")
def lista_bodegas():
    return render_template("listado_bodegas.html", bodegas = bodegas)

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

@app.route("/registrar_categoria", methods = ["POST"])
def registro_categoria():
    nombre = request.form.get("nombre")
    descripcion = request.form.get("descripcion")

    nueva_categoria = Categoria(nombre_categoria= nombre, descripcion= descripcion)
    categorias.append(nueva_categoria)

    return redirect("/")

@app.route("/registro_proveedor")
def registro_proveedor_form():
    return render_template("registro_proveedor.html", productos=productos)

@app.route("/registrar_proveedor", methods=["POST"])
def registrar_proveedor():
    nombre = request.form.get("nombre")
    telefono = request.form.get("telefono")
    direccion = request.form.get("direccion")
    productos_ids = request.form.getlist("productos")

    productos_suministrados = [producto for producto in productos if str(producto.id) in productos_ids]

    nuevo_proveedor = Proveedor(nombre=nombre, telefono=telefono, direccion=direccion)
    nuevo_proveedor.productos = productos_suministrados
    proveedores.append(nuevo_proveedor)

    return redirect(url_for('lista_proveedores'))

@app.route("/proveedores")
def menu_proveedores():
    return render_template("menu_proveedores.html", proveedores=proveedores)

@app.route("/bodegas/registro_bodega", methods=["POST"])
def registro_bodega():
    nombre = request.form.get("nombre")
    ubicacion = request.form.get("ubicacion")
    capacidad_maxima = request.form.get("capacidad")
    productos_seleccionados = request.form.getlist("productos[]")

    # Crea una nueva instancia de Bodega
    nueva_bodega = Bodega(nombre_bodega=nombre, direccion_bodega=ubicacion, capacidad_maxima=capacidad_maxima)

    # Agrega los productos seleccionados a la lista de productos de la bodega
    for producto_id in productos_seleccionados:
        producto = next((p for p in productos if p.id == int(producto_id)), None)
        if producto:
            nueva_bodega.productos.append(producto)

    # Agrega la nueva bodega a la lista de bodegas
    bodegas.append(nueva_bodega)

    return redirect("/")

@app.route("/bodegas/gestion_stock_bodega", methods=["GET", "POST"])
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

#MANEJO DE STOCK
# Ruta para mostrar formularios de agregar y retirar stock
@app.route("/gestion_stock/<int:producto_id>", methods=["GET"])
def mostrar_formulario_stock(producto_id):
    producto = next((p for p in productos if p.id == producto_id), None)
    if producto:
        return render_template("gestion_stock.html", producto=producto)
    else:
        flash("Producto no encontrado", "error")
        return redirect("/")

# Ruta para agregar stock a un producto existente
@app.route("/agregar_stock/<int:producto_id>", methods=["POST"])
def agregar_stock(producto_id):
    cantidad = int(request.form["cantidad"])
    producto = next((p for p in productos if p.id == producto_id), None)
    if producto:
        producto.cantidad += cantidad
        flash("Stock agregado exitosamente", "success")
    else:
        flash("Producto no encontrado", "error")
    return redirect(f"/producto/{producto_id}")

# Ruta para retirar stock de un producto existente
@app.route("/retirar_stock/<int:producto_id>", methods=["POST"])
def retirar_stock(producto_id):
    cantidad = int(request.form["cantidad"])
    producto = next((p for p in productos if p.id == producto_id), None)
    if producto:
        if producto.cantidad >= cantidad:
            producto.cantidad -= cantidad
            flash("Stock retirado exitosamente", "success")
        else:
            flash("Cantidad insuficiente en stock", "error")
    else:
        flash("Producto no encontrado", "error")
    return redirect(f"/producto/{producto_id}")

# Rutas para mostrar los formularios de registro
@app.route("/registrar_categoria", methods=["GET"])
def mostrar_formulario_registro_categoria():
    return render_template("registrar_categoria.html")

@app.route("/registrar_producto", methods=["GET"])
def mostrar_formulario_registro_producto():
    return render_template("registro_producto.html", categorias=categorias, bodegas=bodegas)

"""@app.route("/registrar_proveedor", methods=["GET"])
def mostrar_formulario_registro_proveedor():
    return render_template("registro_proveedor.html")"""

@app.route("/bodegas/registro_bodega", methods=["GET"])
def mostrar_formulario_registro_bodega():
    return render_template("registro_bodega.html", productos = productos)

@app.route("/producto/retirar_stock", methods=["GET"])
def mostrar_formulario_retiro_prod():
    return render_template("retirar_producto.html", bodegas=bodegas)

# Ruta para calcular el valor total del stock
@app.route("/valor_total_stock", methods=["GET"])
def calcular_valor_total_stock():
    valor_stock = [producto.precio * producto.cantidad for producto in productos]
    valor_total = sum(valor_stock)
    longitud_lista = len(valor_stock)
    return render_template("valor_total_stock.html", valor_total=valor_total, valor_stock=valor_stock, productos=productos, longitud_lista=longitud_lista)

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

# Ruta para eliminar un producto de una categoría existente
@app.route("/categoria/<int:categoria_id>/eliminar_producto/<int:producto_id>", methods=["POST"])
def eliminar_producto_de_categoria(categoria_id, producto_id):
    categoria = next((c for c in categorias if c.id == categoria_id), None)
    producto = next((p for p in productos if p.id == producto_id), None)
    
    if categoria and producto:
        if producto in categoria.productos:
            categoria.productos.remove(producto)
            flash("Producto eliminado de la categoría", "success")
        else:
            flash("Producto no encontrado en la categoría", "error")
    else:
        flash("Categoría o producto no encontrado", "error")
    
    return redirect(f"/categoria/{categoria_id}")

# Ruta para eliminar un producto de la lista de productos suministrados por un proveedor existente
@app.route("/proveedor/<int:proveedor_id>/eliminar_producto/<int:producto_id>", methods=["POST"])
def eliminar_producto_de_proveedor(proveedor_id, producto_id):
    proveedor = next((p for p in proveedores if p.id == proveedor_id), None)
    producto = next((p for p in productos if p.id == producto_id), None)
    
    if proveedor and producto:
        if producto in proveedor.productos:
            proveedor.productos.remove(producto)
            flash("Producto eliminado del proveedor", "success")
        else:
            flash("Producto no encontrado en la lista del proveedor", "error")
    else:
        flash("Proveedor o producto no encontrado", "error")
    
    return redirect(f"/proveedor/{proveedor_id}")

# Ruta para retirar un producto de la lista de productos almacenados en una bodega
@app.route("/bodega/<int:bodega_id>/retirar_producto/<int:producto_id>", methods=["POST"])
def retirar_producto_de_bodega(bodega_id, producto_id):
    cantidad_a_retirar = int(request.form["cantidad"])
    bodega = next((b for b in bodegas if b.id == bodega_id), None)
    producto = next((p for p in productos if p.id == producto_id), None)
    
    if bodega and producto:
        if producto in bodega.productos:
            stock_actual = producto.cantidad
            if cantidad_a_retirar <= stock_actual:
                bodega.retirar_producto(producto, cantidad_a_retirar)
                flash("Producto retirado de la bodega", "success")
            else:
                flash("Cantidad a retirar excede el stock disponible", "error")
        else:
            flash("Producto no encontrado en la bodega", "error")
    else:
        flash("Bodega o producto no encontrado", "error")
    
    return redirect(f"/bodega/{bodega_id}")

#Programa principal
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
