from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hola_mundo():
    return '¡Hola, mundo!'

@app.route('/about')
def acerca_de():
    return 'Esta es la página de acerca de.'

if __name__ == '__main__':
    app.run(debug=True)