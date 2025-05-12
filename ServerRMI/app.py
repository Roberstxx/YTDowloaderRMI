from flask import Flask, request, jsonify, render_template, send_from_directory, redirect, url_for
import Pyro4
import os

app = Flask(__name__)

def get_descargador():
    ns = Pyro4.locateNS(host="192.168.1.13")
    uri = ns.lookup("descargador.youtube")
    return Pyro4.Proxy(uri)

@app.route('/')
def index():
    archivos = os.listdir('offline')
    return render_template('index.html', archivos_descargados=archivos)

@app.route('/descargar', methods=['POST'])
def descargar():
    url = request.form.get('url')
    try:
        descargador = get_descargador()
        resultado = descargador.descargar_video(url)
        return jsonify({'resultado': resultado})
    except Exception as e:
        return jsonify({'resultado': f"Error: {e}"})

@app.route('/subir', methods=['POST'])
def subir():
    archivo = request.files.get('archivo')
    if archivo and archivo.filename:
        contenido = archivo.read()
        try:
            descargador = get_descargador()
            resultado = descargador.subir_archivo(archivo.filename, contenido)
            print(resultado)
        except Exception as e:
            print(f"Error: {e}")
    return redirect(url_for('index'))

@app.route('/offline/<path:archivo>')
def servir_archivo(archivo):
    return send_from_directory('offline', archivo)

if __name__ == '__main__':
    if not os.path.exists("offline"):
        os.makedirs("offline")
    app.run(debug=True, host='0.0.0.0', port=5001)

