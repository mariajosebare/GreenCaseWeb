import requests
from flask import Flask, request, render_template, flash, redirect, session


app = Flask(__name__)
app.secret_key = "w9z$C&F)"


@app.route("/login", methods=['POST'])
def hacerLogin():
    f = 1
    data = {
        'email': request.form['email'],
        'password': request.form['password']
    }
    response = requests.post("http://localhost:5000/login", data).json()
    if response is None:
        flash('Nombre de usuario o contraseña incorrectos')
        logout()
        return redirect('/login')
    else:
        session['IdUsuario'] = response['IdUsuario']
        session['Nombre'] = response['Nombre']
        session['Apellido'] = response['Apellido']
        return redirect('/modulos')


@app.route("/modulos", methods=['GET'])
def obtenerModulos():
    if 'IdUsuario' in session:
       return render_template('pages/modulos.html')
    else:
        return redirect('/login')



@app.route("/login", methods=['GET'])
def obtenerLogin():
    return render_template('pages/login.html')


def logout():
    del session['IdUsuario']
    del session['Nombre']
    del session['Apellido']


if __name__ == '__main__':
    app.run(host="localhost", port=5001, debug=True)