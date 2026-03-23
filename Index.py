from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/servicios')
def servicios():
    return "Sección de Servicios en construcción"

@app.route('/contacto')
def contacto():
    return "Sección de Contacto en construcción"

if __name__ == '__main__':
    # Cambiamos a puerto 5001 para evitar bloqueos
    app.run(debug=True, port=5001)