
# 🎬 YouTube Downloader (Cliente) - Comunicación RMI con Pyro4

Este proyecto representa el **cliente** de un sistema de descarga de videos de YouTube. Utiliza **Flask** como interfaz web y se conecta mediante **Pyro4** (Python Remote Objects) a un servidor remoto que se encarga de procesar las descargas.

> ✅ **Este README cubre únicamente la parte del cliente.**

---

## 📁 Estructura del proyecto (Cliente)

```
cliente/
├── app.py                  # Aplicación Flask del cliente
├── templates/
│   └── index.html          # Interfaz web (formulario y lista de archivos)
├── offline/                # Carpeta donde se almacenan archivos descargados/subidos
├── requirements.txt        # Dependencias necesarias
```

---

## ⚙️ Requisitos

- Python 3.7 o superior
- pip
- Estar en la **misma red local** que el servidor
- Tener el servidor Pyro corriendo por separado

---

## 📦 Instalación y configuración

### 1. Clonar el repositorio

```bash
git clone https://github.com/tu_usuario/youtube-downloader-cliente.git
cd youtube-downloader-cliente
```

### 2. Crear entorno virtual (opcional pero recomendado)

```bash
python -m venv venv
source venv/bin/activate     # En Linux/macOS
venv\Scripts\activate        # En Windows
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## 🚀 Ejecución del cliente

### 1. Asegúrate de que el servidor Pyro está activo

En la computadora servidor (la que realiza las descargas), se deben seguir estos pasos:

#### a. Iniciar el NameServer de Pyro4:

```bash
pyro4-ns -n <IP_DEL_SERVIDOR>
```

Ejemplo:

```bash
pyro4-ns -n 192.168.1.13
```

> Este comando debe ejecutarse en una terminal y permanecer abierto.

#### b. Iniciar el servidor Pyro:

Desde otra terminal (en la misma carpeta donde está `pyro_server.py`):

```bash
python pyro_server.py
```

El servidor debe mostrar un mensaje como:

```
Servidor Pyro corriendo...
URI del servidor: PYRO:descargador.youtube@192.168.1.13:XXXX
```

---

### 2. Ejecutar el cliente Flask (en la laptop)

En la computadora cliente, simplemente corre:

```bash
python app.py
```

Esto iniciará un servidor web accesible en:

```
http://localhost:5001
```

> Asegúrate de que el puerto `5001` esté libre.

---

## 🌐 Uso del sistema

Desde la interfaz web puedes:

- Introducir una URL de YouTube y enviarla (la descarga se realiza en el servidor).
- Subir archivos manualmente a la carpeta `offline/`.
- Ver y acceder a los archivos descargados directamente desde el navegador.

---

## 📝 Notas importantes

- La dirección IP en `pyro_server.py` debe coincidir con la IP local de la PC donde corre el servidor.
- La carpeta `offline/` se crea automáticamente si no existe.
- El cliente no descarga directamente usando Pyro, pero puede convivir con el servidor corriendo en paralelo en la red.
- Si el servidor no está disponible, la app seguirá funcionando pero sin conexión a RMI.

---

## ✅ Tecnologías utilizadas

- Python 3
- Flask
- Pyro4
- yt_dlp

---

## 🧑‍💻 Autor

- **Tu Nombre**  
- GitHub: [@tu_usuario](https://github.com/tu_usuario)  
- Contacto: tu.email@ejemplo.com

---

## 📄 Licencia

Este proyecto está licenciado bajo la **MIT License**. Consulta el archivo `LICENSE` para más detalles.
