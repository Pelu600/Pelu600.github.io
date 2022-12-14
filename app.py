from flask import Flask, render_template, url_for, request, redirect
import os
from forms import SignupForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'malwarefuck'

lista_empleados = ["Ana", "Claudia", "Soledad"]

@app.route('/')
@app.route('/inicio')
def inicio():

    return render_template("index.html", numero_empleados = len(lista_empleados))

@app.route('/servicios')
def servicios():
    return render_template('servicios.html')

@app.route('/productos')
def productos():
    return render_template('productos.html')

@app.route('/usuarios/<int:numerousuario>')
def usuarios(numerousuario):

    #return f"Bienvenido a la web usuario numero {numerousuario}"
    return render_template('usuarios/usuarios.html', num_usuario = numerousuario)



@app.route('/usuarios/<int:id>/<string:nombreusuarios>')
def datosusuario(id, nombreusuarios):

    #return f"estos son los datos del usuario. Id {id}. Nombre de usuario: {nombreusuarios}"
    return render_template('usuarios/datos_usuarios.html', id = id, nombreusuarios = nombreusuarios)




@app.route('/posts')
@app.route('/posts/<int:npost>')
def posts(npost = 0):

    return "Este es el post N {}".format(npost)

@app.route('/contacto', methods = ["GET", "POST"])
def contacto():

    form = SignupForm()

    if form.validate_on_submit():

        nombre = form.name.data
        email = form.email.data
        contra = form.password.data

        return redirect(url_for("inicio"))

    return render_template('contacto.html', form = form)

if __name__ == "__main__":

    os.environ['FLASK_ENV'] = "development"
    app.run(debug = True)
