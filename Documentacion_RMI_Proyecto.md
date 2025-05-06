
# 📄 Documentación del Proyecto: Descargador de YouTube con RMI usando Pyro4

Este instructivo describe paso a paso cómo instalar, configurar y ejecutar un sistema distribuido cliente-servidor que permite descargar videos de YouTube usando **RMI (Remote Method Invocation)** con **Pyro4**.

El sistema se divide en dos partes:

- 🖥️ **Servidor:** Se encarga de descargar el video desde YouTube usando `yt_dlp`.
- 💻 **Cliente:** Interfaz web desde la cual el usuario introduce la URL del video; se conecta al servidor vía Pyro4.

---

## 📦 1. Requisitos Generales

### Lenguaje y librerías necesarias (en ambas máquinas):

- Python 3.7 o superior
- pip
- Flask (solo para el cliente y servidor con interfaz web)
- Pyro4 (para la comunicación RMI)

### Librería adicional solo para el servidor:

- yt_dlp (descarga de videos)

---

## 🛠️ 2. Configuración del Servidor (PC Servidor)

### Paso 1: Clonar o copiar el proyecto en la PC Servidor

Coloca los siguientes archivos en una carpeta del servidor:

```
servidor/
├── pyro_server.py
├── app.py
├── templates/index.html
├── requirements.txt
```

### Paso 2: Crear entorno virtual (opcional pero recomendado)

```bash
python -m venv venv
source venv/bin/activate    # En Linux/macOS
venv\Scripts\activate     # En Windows
```

### Paso 3: Instalar dependencias

```bash
pip install -r requirements.txt
```

O manualmente:

```bash
pip install flask yt_dlp Pyro4
```

### Paso 4: Configurar la IP en `pyro_server.py`

Reemplaza `"192.168.1.13"` por la IP local del servidor:

```python
daemon = Pyro4.Daemon(host="192.168.1.13")  # <- IP del servidor
```

### Paso 5: Iniciar el Name Server de Pyro4

Abre una terminal y ejecuta:

```bash
pyro4-ns -n 192.168.1.13
```

> Este proceso debe quedar abierto todo el tiempo.

### Paso 6: Iniciar el servidor Pyro

En otra terminal, dentro del mismo proyecto:

```bash
python pyro_server.py
```

Verás un mensaje como:

```
Servidor Pyro corriendo...
URI del servidor: PYRO:descargador.youtube@192.168.1.13:XXXX
```

---

## 💻 3. Configuración del Cliente (Laptop)

### Paso 1: Clonar o copiar el cliente

Archivos necesarios:

```
cliente/
├── web_client.py
├── app.py (opcional, modo consola)
├── templates/index.html
├── requirements.txt
```

### Paso 2: Crear entorno virtual

```bash
python -m venv venv
source venv/bin/activate    # En Linux/macOS
venv\Scripts\activate     # En Windows
```

### Paso 3: Instalar dependencias

```bash
pip install flask Pyro4
```

> En el cliente **NO es necesario instalar `yt_dlp`** porque la descarga se realiza en el servidor.

### Paso 4: Configurar la IP del servidor en `web_client.py`

```python
ns = Pyro4.locateNS(host="192.168.1.13")
uri = ns.lookup("descargador.youtube")
```

---

## 🚀 4. Ejecutar el sistema (Prueba desde el navegador)

### 1. En el servidor:

- Inicia el NameServer:
  ```bash
  pyro4-ns -n 192.168.1.13
  ```
- Ejecuta el servidor Pyro:
  ```bash
  python pyro_server.py
  ```

### 2. En el cliente:

- Ejecuta el cliente web:
  ```bash
  python web_client.py
  ```

- Abre tu navegador y accede a:
  ```
  http://localhost:5000
  ```

- Introduce una URL de YouTube y haz clic en **Descargar**.

### 3. Resultado:

- El video será descargado automáticamente en la carpeta `offline/` del servidor.
- El cliente mostrará un mensaje confirmando la descarga exitosa.

---

## 🔄 5. ¿Cómo funciona RMI en este proyecto?

- El servidor Pyro expone un objeto remoto (`Descargador`) que tiene un método `descargar_video(url)`.
- El cliente no descarga el video directamente: se conecta al **NameServer**, busca ese objeto y llama remotamente al método.
- Pyro se encarga de **serializar, enviar y ejecutar** la solicitud en el servidor, y luego devolver la respuesta.
- Este mecanismo es un ejemplo clásico de **RMI (Remote Method Invocation)**.

---

## ✅ Observaciones Finales

- Ambos dispositivos deben estar conectados a la misma red local.
- Asegúrate de que no haya firewalls bloqueando los puertos (9090 y el asignado por Pyro).
- Puedes personalizar el nombre del objeto Pyro siempre que coincida entre servidor y cliente.

---

## 👨‍💻 Autor

**Tu Nombre**  
GitHub: [@tu_usuario](https://github.com/tu_usuario)

---

## 📄 Licencia

MIT License
