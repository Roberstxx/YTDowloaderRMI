# 🎬 YouTube Downloader (Servidor) - Comunicación RMI con Pyro4

Este proyecto representa el **servidor** de un sistema de descarga y gestión remota de archivos multimedia. Utiliza **Pyro4** (Python Remote Objects) para ofrecer servicios remotos accesibles por clientes en la misma red, permitiendo descargar videos de YouTube y subir archivos desde interfaces cliente.

> ✅ **Este README cubre únicamente la parte del servidor.**

---

## 📁 Estructura del proyecto (Servidor)

```
servidor/
├── pyro_server.py          # Servidor Pyro que ofrece descarga y subida vía RMI
├── app.py                  # Aplicación Flask local del servidor (opcional)
├── templates/
│   └── index.html          # Interfaz web usada localmente en el servidor
├── offline/                # Carpeta donde se almacenan los archivos descargados o subidos
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
venv\Scripts\activate        # En Windows
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
- Ver los archivos descargados o subidos
- Previsualizar archivos como PDF, MP4, MP3, TXT, etc.

---

## ⚙️ Funcionalidades disponibles vía Pyro4

Los clientes remotos pueden, usando Pyro:

- 📥 `descargar_video(url)`: Descargar un video de YouTube a la carpeta `offline/`.
- 📤 `subir_archivo(nombre, contenido_bytes)`: Subir un archivo arbitrario desde el cliente.
- 📂 (Extensible) Se pueden agregar fácilmente funciones como `listar_archivos()` o `eliminar_archivo(nombre)`.

---

## 📝 Notas importantes

- La carpeta `offline/` se crea automáticamente si no existe.
- La IP en `pyro_server.py` debe ser la IP local del servidor.
- El servidor debe tener acceso a internet para descargar videos desde YouTube.
- Asegúrate de tener permisos de lectura/escritura sobre la carpeta `offline`.

---

## ✅ Tecnologías utilizadas

- Python 3
- Flask
- Pyro4
- yt_dlp

---

## 📄 Licencia

Este proyecto está licenciado bajo la **MIT License**. Consulta el archivo `LICENSE` para más detalles.
