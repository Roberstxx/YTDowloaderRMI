from flask import Flask, request, render_template, redirect, url_for, flash
import Pyro4

app = Flask(__name__)
app.secret_key = "clave_secreta"

def get_descargador():
    ns = Pyro4.locateNS(host="192.168.1.13")  # IP del servidor
    uri = ns.lookup("descargador.youtube")
    return Pyro4.Proxy(uri)

@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None
    if request.method == 'POST':
        url = request.form.get('url')
        if url:
            try:
                descargador = get_descargador()
                resultado = descargador.descargar_video(url)
            except Exception as e:
                resultado = f"Error al contactar al servidor: {str(e)}"
    return render_template('index.html', resultado=resultado)

@app.route('/subir', methods=['POST'])
def subir():
    archivo = request.files.get('archivo')
    if not archivo or not archivo.filename:
        flash("Archivo no válido.")
        return redirect(url_for('index'))

    try:
        contenido = archivo.read()
        descargador = get_descargador()
        resultado = descargador.subir_archivo(archivo.filename, contenido)
        flash(resultado)
    except Exception as e:
        flash(f"Error al subir el archivo: {str(e)}")

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5002)



