from multiprocessing import Process
import time

inicio = time.time()

procesos = []
for i in range (3):
    p = Process()
    procesos.append(p)
    p.start()

for p in procesos:
    p.join()

fin = time.time()
print(f"Tiempo total con procesos: {fin - inicio:.2f} segundos")
