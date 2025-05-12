from flask import Flask, request, jsonify, render_template, send_from_directory, redirect, url_for
import os
import Pyro4

app = Flask(__name__)

# Función para obtener el proxy Pyro
def get_descargador():
    ns = Pyro4.locateNS(host="192.168.1.13")  # IP del servidor Pyro
    uri = ns.lookup("descargador.youtube")
    return Pyro4.Proxy(uri)

# Ruta para la página principal
@app.route('/')
def index():
    archivos_descargados = os.listdir('offline')
    return render_template('index.html', archivos_descargados=archivos_descargados)

# Ruta para subir archivo
@app.route('/subir', methods=['POST'])
def subir():
    if 'archivo' not in request.files:
        return redirect(url_for('index'))

    archivo = request.files['archivo']
    if archivo.filename == '':
        return redirect(url_for('index'))

    try:
        contenido = archivo.read()
        descargador = get_descargador()
        resultado = descargador.subir_archivo(archivo.filename, contenido)
        print(resultado)
    except Exception as e:
        print(f"Error al subir: {e}")
    return redirect(url_for('index'))

# Ruta para descargar video desde cliente
@app.route('/descargar', methods=['POST'])
def descargar():
    url = request.form['url']
    try:
        descargador = get_descargador()
        resultado = descargador.descargar_video(url)
        return jsonify({'resultado': resultado})
    except Exception as e:
        return jsonify({'resultado': f"Error: {e}"})

# Ruta para servir archivos
@app.route('/offline/<path:path>')
def send_file(path):
    return send_from_directory('offline', path)

if __name__ == '__main__':
    if not os.path.exists("offline"):
        os.makedirs("offline")
    app.run(debug=True, host='0.0.0.0', port=5001)
