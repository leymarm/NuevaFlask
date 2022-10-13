from flask import Flask



app = Flask(__name__)




@app.route('/')

def index():

    return '<h1>Hola Mundo Leymar</h1>'

@app.route('/saludar')

def saludar():

    return '<h1>Hola Gente</h1>'

if __name__ == '__main__':
    
app.run(debug=True, port=8000)