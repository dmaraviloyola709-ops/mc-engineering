from flask import Flask, render_template, request, redirect, url_for
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Inicialización de la aplicación Flask
app = Flask(__name__)

# ==========================================
# DEFINICIÓN DE RUTAS DEL SITIO
# ==========================================

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/nosotros')
def about():
    return render_template('about.html')

@app.route('/sistemadrywall')
def sistemadrywall():
    return render_template('sistemadrywall.html')

@app.route('/remodelacion')
def remodelacion():
    return render_template('remodelacion.html')

@app.route('/consultoria')
def consultoria():
    return render_template('consultoria.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

# ==========================================
# RUTA PARA PROCESAR EL FORMULARIO DE CORREO
# ==========================================

@app.route('/enviar_correo', methods=['POST'])
def enviar_correo():
    if request.method == 'POST':
        nombres = request.form.get('nombres')
        apellidos = request.form.get('apellidos')
        email_cliente = request.form.get('email')
        telefono = request.form.get('telefono')
        mensaje_cliente = request.form.get('mensaje')

        # NUEVO CORREO CONFIGURADO
        mi_correo = "mcinfo.ingenieria@gmail.com"
        
        # REEMPLAZA ESTO con las 16 letras que generes en la nueva cuenta
        mi_password = "TU_NUEVA_CLAVE_AQUI" 
        
        msg = MIMEMultipart()
        msg['From'] = mi_correo
        msg['To'] = mi_correo 
        msg['Subject'] = f"NUEVA COTIZACIÓN WEB: {nombres} {apellidos}"

        cuerpo_mensaje = f"""
        Has recibido un nuevo requerimiento desde la página web de M&C Integrated Engineering:

        DATOS DEL CLIENTE:
        -------------------
        Nombre: {nombres} {apellidos}
        Email: {email_cliente}
        Teléfono: {telefono}

        MENSAJE / REQUERIMIENTO:
        -------------------
        {mensaje_cliente}
        """
        
        msg.attach(MIMEText(cuerpo_mensaje, 'plain'))

        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(mi_correo, mi_password)
            server.sendmail(mi_correo, mi_correo, msg.as_string())
            server.quit()
            
            print("¡Correo enviado exitosamente!")
            return redirect(url_for('contacto'))
            
        except Exception as e:
            print(f"Error al enviar correo: {e}")
            return f"Hubo un error: {e}"

if __name__ == '__main__':
    app.run(debug=True, port=5001)