# 💻 YouTube Downloader (Cliente) - Interfaz Web con Pyro4

Este proyecto representa el **cliente web** que se comunica con el servidor remoto de descargas vía **Pyro4 (Python Remote Objects)**. Permite a los usuarios enviar URLs de videos de YouTube para que el servidor los descargue, así como subir archivos directamente al servidor desde una interfaz web sencilla desarrollada en Flask.

> 🔗 Este cliente debe ejecutarse en la misma red local que el servidor.

---

## 📁 Estructura del proyecto (Cliente)

```
cliente/
├── web.client.py           # Aplicación Flask cliente
├── templates/
│   └── index.html          # Interfaz HTML para enviar URL o subir archivos
```

---

## ⚙️ Requisitos

- Python 3.7 o superior
- pip
- Estar en la **misma red local** que el servidor
- Tener el servidor y el NameServer de Pyro4 corriendo

---

## 📦 Instalación y configuración

### 1. Clonar o copiar el cliente

```bash
# Puedes copiar manualmente o usar git si tienes el repo compartido
cd cliente
```

### 2. Crear entorno virtual (opcional pero recomendado)

```bash
python -m venv venv
source venv/bin/activate     # Linux/macOS
venv\Scripts\activate      # Windows
```

### 3. Instalar dependencias

```bash
pip install flask Pyro4
```

---

## 🚀 Ejecución del cliente

```bash
python web.client.py
```

Abre el navegador y visita:

```
http://localhost:5002
```

---

## ✨ Funcionalidades disponibles

- 🎥 Ingresar una URL de YouTube y solicitar la descarga desde el servidor.
- 📤 Subir archivos (MP3, PDF, TXT, etc.) al servidor remoto.
- 📝 Ver mensajes de confirmación del servidor (subida/descarga exitosa o errores).

---

## 🔧 Notas de configuración

- En `web.client.py`, asegúrate de que esta línea tenga la **IP del servidor Pyro**:

```python
Pyro4.config.NS_HOST = "192.168.1.13"
```

- El servidor debe tener corriendo el `NameServer` (`pyro4-ns`) y el archivo `pyro_server.py`.

---

## ✅ Tecnologías utilizadas

- Python 3
- Flask
- Pyro4
- HTML/CSS

---

## 📄 Licencia

Este cliente está licenciado bajo la **MIT License**. Consulta el archivo `LICENSE` si se incluye.