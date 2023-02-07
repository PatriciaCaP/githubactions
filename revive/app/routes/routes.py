from app import db
from flask import Flask, render_template, request, redirect, url_for, Blueprint

from app.data.infoUsuarios  import Usuario
from app.data.infoProductos import Producto  # PARA PODER ACCEDER A LOS DIRECTORIOS DE UNA MANERA FÁCIL 


rutas_usuarios = Blueprint("routes", __name__)

@rutas_usuarios.route('/')  # ESTO ES LA RUTA PRINCIPAL DE NUESTRA APP SE PONE CON LA BARRA
def home():
    infoUsuarios : Usuario = Usuario(db)
    return render_template('index.html', data=infoUsuarios.dameTodos())  # PARA QUE SALGA NUESTRO INDEX AL INICIO #DATA=INSERTOBJECT ES PARA QUE NOS SALGA EN NUESTRO HTML


@rutas_usuarios.route('/user', methods=['POST'])
def addUser():
    nombre = request.form['nombre'] # PARA PODER OBTENER EL CONTENIDO DEL INPUT CON EL NOMBRE QUE INDIQUEMOS
    apellido = request.form['apellido'] # PARA PODER OBTENER EL CONTENIDO DEL INPUT CON EL password QUE INDIQUEMOS
    email = request.form['email'] # PARA PODER OBTENER EL CONTENIDO DEL INPUT CON EL NOMBRE QUE INDIQUEMOS
    usuario : Usuario = Usuario(db)
    usuario.añadirUsuario(nombre,apellido,email)
    return redirect(url_for('routes.home')) # Y REDIRIGIMOS A HOME DE NUEVO. REDIRECT Y URL_FOR LO TENEMOS QUE IMPORTAR DE FLASK

    
@rutas_usuarios.route('/delete/<string:idusuario>')
def delete(idusuario):
    usuario : Usuario = Usuario(db)
    usuario.borrarUsuario(idusuario)
    return redirect(url_for('routes.home')) # Y REDIRIGIMOS A HOME DE NUEVO. REDIRECT Y URL_FOR LO TENEMOS QUE IMPORTAR DE FLASK


@rutas_usuarios.route('/productos')  # ESTO ES LA RUTA PARA VER LAS NOTAS DE LOS ALUMNOS EN MI APP SE PONE CON LA BARRA
def productos():
    infoProductos : Producto = Producto(db)
    return render_template('producto.html', data=infoProductos.dameProducto())  # PARA QUE SALGA NUESTRO INDEX AL INICIO #DATA=INSERTOBJECT ES PARA QUE NOS SALGA EN NUESTRO HTML


@rutas_usuarios.route('/userProductos', methods=['POST'])
def addProductos():
    idusuario = request.form['idusuario'] # PARA PODER OBTENER EL CONTENIDO DEL INPUT CON EL CODIGO ALUMNO QUE INDIQUEMOS
    titulo = request.form['titulo'] # PARA PODER OBTENER EL CONTENIDO DEL INPUT CON LA NOTA QUE INDIQUEMOS
    estado = request.form['estado'] # PARA PODER OBTENER EL CONTENIDO DEL INPUT CON LA NOTA QUE INDIQUEMOS
    producto : Producto = Producto(db)
    producto.añadeProducto(idusuario,titulo,estado)
    return redirect(url_for('routes.productos')) # Y REDIRIGIMOS A HOME DE NUEVO. REDIRECT Y URL_FOR LO TENEMOS QUE IMPORTAR DE FLASK


@rutas_usuarios.route('/deleteProductos/<string:idusuario>')
def deleteProductos(idusuario):
    producto : Producto = Producto(db)
    producto.borrarProducto(idusuario)
    return redirect(url_for('routes.productos')) # Y REDIRIGIMOS A HOME DE NUEVO. REDIRECT Y URL_FOR LO TENEMOS QUE IMPORTAR DE FLASK


