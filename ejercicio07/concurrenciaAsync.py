import asyncio
import random
import time

async def consulta_bd(id):
    tiempo = random.randint(1, 5)
    print(f"Consulta {id} iniciada (tardará {tiempo}s)")
    await asyncio.sleep(tiempo)
    print(f"Consulta {id} finalizada")

async def main():
    inicio = time.time()
    tareas = [consulta_bd(i + 1) for i in range(3)]
    await asyncio.gather(*tareas)
    fin = time.time()
    print(f"Tiempo total con async: {fin - inicio:.2f} segundos.")

asyncio.run(main())