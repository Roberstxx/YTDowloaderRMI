import Pyro4
import yt_dlp
import os

# Crear carpeta si no existe
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
            with open(os.path.join("offline", nombre), "wb") as f:
                f.write(contenido_bytes)
            return f"Archivo '{nombre}' subido correctamente."
        except Exception as e:
            return f"Error al subir archivo: {e}"

def main():
    daemon = Pyro4.Daemon(host="192.168.1.13")  # IP del servidor
    ns = Pyro4.locateNS()
    uri = daemon.register(Descargador)
    ns.register("descargador.youtube", uri)
    print("Servidor Pyro corriendo. URI:", uri)
    daemon.requestLoop()

if __name__ == "__main__":
    main()

