from Proveedor import Proveedor
from Producto import Producto
from Categoria import Categoria
from Bodega import Bodega
from flask import Flask, render_template, redirect

#aplicación
app = Flask(__name__)

#rutas (editar sele)
#@app.route("")
#def ruta_raiz():
    #return render_template("",)

#@app.route("/producto/<int:pid>")
#def ruta_producto(pid):
    #for producto in :
        #if pid == producto["id"]:
            #return render_template("producto.html", producto=producto)
    #return redirect("/")
    
#programa principal
#if __name__ == "__main__":
    #app.run(host="0.0.0.0", debug=True)
