import Pyro4
import yt_dlp
import os

# Asegúrate de que la carpeta "offline" exista
if not os.path.exists("offline"):
    os.makedirs("offline")

@Pyro4.expose
class Descargador:
    def descargar_video(self, url):
        ydl_opts = {
            'format': 'best',
            'outtmpl': 'offline/%(title)s.%(ext)s',
            'restrictfilenames': True,
        }

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            return "Video descargado con éxito"
        except Exception as e:
            return f"Error: {str(e)}"

    def subir_archivo(self, nombre, contenido_bytes):
        try:
            ruta = os.path.join("offline", nombre)
            with open(ruta, "wb") as f:
                f.write(contenido_bytes)
            return f"Archivo '{nombre}' subido correctamente."
        except Exception as e:
            return f"Error al subir el archivo: {e}"

# Iniciar el servidor Pyro
def main():
    daemon = Pyro4.Daemon(host="192.168.1.13")  # Cambia a la IP de tu servidor
    ns = Pyro4.locateNS()  # Se conecta al Name Server
    uri = daemon.register(Descargador)
    ns.register("descargador.youtube", uri)  # Nombre que debe usar el cliente

    print("Servidor Pyro corriendo. URI:", uri)
    daemon.requestLoop()

if __name__ == "__main__":
    main()
