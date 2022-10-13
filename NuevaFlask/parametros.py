from flask import Flask
from flask import request
from flask import url_for
from flask import render_template


app = Flask(__name__)




@app.route('/')

def index():

    return '<h1>Hola Mundo Leymar</h1>'

@app.route('/parametros')

def params():

   parametro = request.args.get('parametro1', 'No contiene este parametro')

   return "El parametro es: {}".format(parametro)

@app.route('/hola/')
@app.route('/hola/<string:nombre>')
@app.route('/hola/<string:nombre>/<int:edad>')
def holafun(nombre= None, edad= None):

    if nombre and edad:
        return 'Hola {} tienes {} años'.format(nombre,edad)
    elif nombre:
        return 'Hola {}'.format(nombre)
    else:
        return 'Hola'


# url_for()

@app.route('/enlaces/')
def enlaces():
    cad='<a href="{0}">Decir hola Maria</a>({0})<br/>'.format(url_for("holafun"))
    cad= cad + '<a href="{0}">Decir hola Maria</a>({0})<br/>'.format(url_for("holafun", nombre="Maria"))
    cad= cad + '<a href="{0}">Decir hola Maria</a>({0})<br/>'.format(url_for("holafun", nombre="Maria", edad=16))
    return cad


if __name__ == '__main__':
    app.run(debug=True, port=8000)