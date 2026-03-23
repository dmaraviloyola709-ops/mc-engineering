from flask import Flask, render_template, url_for

app = Flask(__name__)

# Ruta para la página de Inicio (INICIO)
@app.route('/')
def home():
    return render_template('home.html')

# Ruta para la página de Nosotros (NOSOTROS)
# Nota: La función se llama 'about' porque así la tienes en tu layout: url_for('about')
@app.route('/nosotros')
def about():
    return render_template('about.html')

# Ruta para Servicios o Proyectos
@app.route('/servicios')
def servicios():
    # Si aún no tienes servicios.html, esto evitará que el programa se caiga
    return "Sección de Servicios y Proyectos en construcción - M&C Ingeniería"

# Ruta para Contacto (CONTACTO)
@app.route('/contacto')
def contacto():
    return "Sección de Contacto en construcción - M&C Ingeniería"

if __name__ == '__main__':
    # Usamos el puerto 5001 como lo tenías configurado
    app.run(debug=True, port=5001)