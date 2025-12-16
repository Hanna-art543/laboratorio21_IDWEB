from geometria import calcular_operacion, OperadorInvalidoError

try:
    operacion = input("Ingrese la operación (ejemplo: 10 / 2): ")
    resultado = calcular_operacion(operacion)
    print("Resultado:", resultado)

except ZeroDivisionError as e:
    print("Error:", e)

except OperadorInvalidoError as e:
    print("Error:", e)

except ValueError as e:
    print("Error:", e)
