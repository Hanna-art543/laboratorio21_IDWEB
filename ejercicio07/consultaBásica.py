import time
import random

def consulta_bd(id):
    tiempo = random.randint(1, 5)
    print(f"Consulta {id} iniciada (tardará {tiempo}s)")
    time.sleep(tiempo)
    print(f"Consulta {id} finalizada")