from flask import Flask, render_template

app = Flask(__name__)

# Ruta principal (Inicio)
@app.route('/')
def home():
    return render_template('home.html')

# Ruta para la página About (fíjate que está en minúsculas)
@app.route('/about')
def about():
    return render_template('about.html')

# Condición para arrancar el servidor (sin espacios extras)
if __name__ == '__main__':
    app.run(debug=True)