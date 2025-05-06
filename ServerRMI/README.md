
# 🎬 YouTube Downloader (Servidor) - Comunicación RMI con Pyro4

Este proyecto representa el **servidor** de un sistema de descarga de videos de YouTube. Utiliza **Pyro4** (Python Remote Objects) para ofrecer un servicio remoto accesible por clientes en la misma red, permitiendo que estos soliciten descargas de videos.

> ✅ **Este README cubre únicamente la parte del servidor.**

---

## 📁 Estructura del proyecto (Servidor)

```
servidor/
├── pyro_server.py          # Servidor Pyro que realiza las descargas
├── app.py                  # Aplicación Flask local del servidor
├── templates/
│   └── index.html          # Interfaz web (opcional, usada localmente)
├── offline/                # Carpeta donde se almacenan los videos descargados
├── requirements.txt        # Dependencias necesarias
```

---

## ⚙️ Requisitos

- Python 3.7 o superior
- pip
- Estar conectado a la **misma red local** que los clientes

---

## 📦 Instalación y configuración

### 1. Clonar el repositorio

```bash
git clone https://github.com/tu_usuario/youtube-downloader-servidor.git
cd youtube-downloader-servidor
```

### 2. Crear entorno virtual (opcional pero recomendado)

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

## 🚀 Ejecución del servidor

### 1. Iniciar el NameServer de Pyro4

```bash
pyro4-ns -n <IP_DEL_SERVIDOR>
```

Ejemplo:

```bash
pyro4-ns -n 192.168.1.13
```

> Este comando debe permanecer ejecutándose en una terminal.

### 2. Ejecutar el servidor Pyro

Desde otra terminal, en el mismo directorio del archivo `pyro_server.py`, ejecuta:

```bash
python pyro_server.py
```

Deberías ver algo como:

```
Servidor Pyro corriendo...
URI del servidor: PYRO:descargador.youtube@192.168.1.13:XXXX
```

---

## 🌐 Interfaz web local (opcional)

También puedes usar `app.py` para ejecutar una interfaz web en el mismo servidor:

```bash
python app.py
```

Accede desde el navegador en:

```
http://localhost:5001
```

Desde aquí podrás:

- Descargar videos de YouTube desde el servidor
- Subir archivos manualmente a la carpeta `offline/`
- Ver los archivos descargados

---

## 📝 Notas importantes

- Asegúrate de que la IP en `pyro_server.py` sea la IP local del servidor.
- La carpeta `offline/` se crea automáticamente si no existe.
- El servidor y cliente deben estar conectados a la misma red local.
- El servidor debe tener acceso a internet para descargar videos desde YouTube.

---

## ✅ Tecnologías utilizadas

- Python 3
- Flask
- Pyro4
- yt_dlp

---

## 📄 Licencia

Este proyecto está licenciado bajo la **MIT License**. Consulta el archivo `LICENSE` para más detalles.
