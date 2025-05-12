import Pyro4

def main():
    try:
        # IP del servidor donde corre Pyro4 y el NameServer
        ns = Pyro4.locateNS(host="192.168.1.13")
        uri = ns.lookup("descargador.youtube")
        descargador = Pyro4.Proxy(uri)

        # Entrada del usuario
        url = input("Ingresa la URL del video de YouTube: ")
        resultado = descargador.descargar_video(url)
        print("Respuesta del servidor:", resultado)

    except Exception as e:
        print("Error al conectar con el servidor:", e)

if __name__ == "__main__":
    main()
