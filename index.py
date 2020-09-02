#empezar a llamr el flask, y para importar html es el render_template
from flask import Flask, render_template
#arrancar en una variable llamada app para poder crear rutas del servidor y URL
app = Flask(__name__)

#crear una ruta para la pagina principal utilizando un decoradro con el @ y el / es para decirle que es la pagina principal
@app.route('/')
#crear una funcion que va a manejar esta ruta
def home():
    return render_template('home.html')

#crear ruta about
@app.route('/about')
#funcion que va a manejar la ruta about
def about():
    return render_template('about.html')


# hacer que la aplicacion se quede escuchando siempre(osea que tiene que estar activa todo el tiempo por medio del servidor)
#primero hacer una validacion para comprobar si estamos en el archivo principal
if __name__ == '__main__':
    app.run(debug=True) #este metodo run nos permite ejecutar la aplicacion 
                        #el debug es para no estar reiniciando el servidor cada vez que cambio el codigo



