def copiar_archivo_txto(origen, destino):
    try:
        with open (origen, "r", encoding ="utf-8") as archivo_origen:
            contenido = archivo_origen.read()
        
        with open (destino, "w", encoding = "utf-8") as archivo_destino:
            archivo_destino.write(contenido)
        
        print("Archivo de texto copiado correctamente.")

    except FileNotFoundError:
        print("Error: el archivo de origen no existe")
    
    except IOError:
        print("Error a leer o escribir el archivo")

origen = input("Nombre del archivo de texto origen: ")
destino = input("Nombre del archivo de texto destino: ")

copiar_archivo_txto(origen, destino)


