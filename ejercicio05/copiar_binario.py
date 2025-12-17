def copiar_archivo_binario(origen, destino):
    try:
        with open (origen, "rb") as archivo_origen:
            contenido = archivo_origen.read()
        with open (destino, "wb") as archivo_destino:
            archivo_destino.write(contenido)
        
        print("Archivo binario copiado correctamente.")
    
    except FileNotFoundError:
        print("Error: el archivo de origen no existe.")
    
    except IOError:
        print("Error al copiar el archivo binario")
    

origen = input("Nombre del archivo binario origen: ")
destino = input("Nombre del archivo binario destino: ")

copiar_archivo_binario(origen, destino)


