from Proveedor import Proveedor
from Producto import Producto
from Categoria import Categoria
from Bodega import Bodega
from flask import Flask, render_template, redirect

#aplicación
app = Flask(__name__)

#Creación de instancias de productos
Lista_Proveedores = [Proveedor("Maderas Anita", 3105916884, "maderas_anita@gmail.com"), 
                    Proveedor("Lupita_Baldosas", 3127167148, "LupitaBaldosas@hotmail.com"), 
                    Proveedor("Casa Bonita", 3106172961, "CasaBonita@gmail.com"), 
                    Proveedor("Hogares de confianza", 3017263829, "HogaresConfianza34@hotmail.com"),
                    Proveedor("Cersei Castillo", 3728192678, "CerseiCas7000@gmail.com")]

Lista_Productos = [Producto(1, "Silla Reclinable", "Espectacular silla amoblada para una persona la cual se reclina y cuenta con garantía de 12 meses.", 960000 ),
                                    Producto(2, "Sofá Cama", "Sofá Cama con 3 posiciones, modo cama, reclinado o TV y modo sofá", 1200000),
                                    Producto(3, "Silla Computador", "Silla para escritorio hecha en tela y con soporte hasta de 80kg", 125000 ),
                                    Producto(4, "Biblioteca Horizontal", "Biblioteca horizontal multiusos color madera oscura, cuenta con seis espacios para almacenar", 560000 ),
                                    Producto(5, "Set de Herramientas Manuales de 250 Piezas", "Juego completo de herramientas que cuenta con 250 piezas", 209900)]

Lista_Categorias = [Categoria("Construccion y Ferreteria"), 
                   Categoria("Pisos.Pinturas y Terminaciones"), 
                   Categoria("Herramientas y maquinaria"), 
                   Categoria("Baño. Cocina"),
                   Categoria("Muebles"),
                   Categoria("Decoración. Menaje E Iluminacion"),
                   Categoria("Aire libre")]

#rutas (editar sele)
@app.route("/")
def ruta_raiz():
    return render_template("index.html", productos = Lista_Productos)

#@app.route("/producto/<int:pid>")
#def ruta_producto(pid):
    #for producto in :
        #if pid == producto["id"]:
            #return render_template("producto.html", producto=producto)
    #return redirect("/")
    
#programa principal
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

