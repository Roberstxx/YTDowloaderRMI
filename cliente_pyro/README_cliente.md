
# 📥 Cliente Pyro - Descargador de YouTube

Este es el **cliente** que se conecta remotamente al servidor Pyro para solicitar la descarga de videos desde YouTube.

El cliente puede utilizarse desde la línea de comandos (`app.py`) o desde una interfaz web simple (`web_client.py` con Flask).

---

## 📁 Estructura del proyecto (Cliente)

```
cliente/
├── app.py                   # Cliente de consola que usa Pyro4
├── web_client.py            # Cliente web que se conecta al servidor Pyro
├── templates/
│   └── index.html           # Página HTML para la interfaz web
├── requirements.txt         # Dependencias necesarias
```

---

## ⚙️ Requisitos

- Python 3.7 o superior
- pip
- Estar conectado a la **misma red local** que el servidor
- IP del servidor Pyro configurada correctamente

---

## 📦 Instalación y configuración

### 1. Clonar el repositorio

```bash
git clone https://github.com/tu_usuario/youtube-downloader-cliente.git
cd youtube-downloader-cliente
```

### 2. Crear entorno virtual (opcional)

```bash
python -m venv venv
source venv/bin/activate     # En Linux/macOS
venv\Scripts\activate      # En Windows
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## 🧪 Modo consola (`app.py`)

### Uso

1. Asegúrate de que el servidor esté corriendo y accesible por IP.
2. Ejecuta:

```bash
python app.py
```

3. Ingresa la URL de un video de YouTube cuando se te solicite.
4. Verás la respuesta del servidor (éxito o error).

> Asegúrate de que la IP del servidor esté correcta en el archivo `app.py`:

```python
ns = Pyro4.locateNS(host="192.168.1.13")  # Cambia esta IP según tu red
```

---

## 🌐 Modo Web (`web_client.py`)

### Uso

1. Asegúrate de que el servidor Pyro esté corriendo.
2. Ejecuta:

```bash
python web_client.py
```

3. Abre tu navegador y accede a:

```
http://localhost:5000
```

4. Pega una URL de YouTube y haz clic en **Descargar**.
5. Verás el resultado en la misma página.

---

## ✅ Tecnologías utilizadas

- Python 3
- Flask
- Pyro4

---

## 📝 Notas

- Este cliente **no descarga los videos**. Solo envía la solicitud al servidor mediante RMI.
- La descarga se realiza en el servidor, no en la máquina cliente.
- Puedes modificar la IP del servidor en ambos scripts (`app.py` y `web_client.py`) según sea necesario.

---

## 👨‍💻 Autor

- **Tu Nombre**
- GitHub: [@tu_usuario](https://github.com/tu_usuario)

---

## 📄 Licencia

Este proyecto está bajo la licencia **MIT**.
