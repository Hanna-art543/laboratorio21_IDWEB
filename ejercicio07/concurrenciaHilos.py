import threading
import time

inicio = time.time()

hilos = []
for i in range(3):
    hilo = threading.Thread()
    hilos.append(hilo)
    hilo.start()

for hilo in hilos:
    hilo.join()

fin = time.time()
print(f"Tiempo total con hilos: {fin - inicio:.2f} segundos.")