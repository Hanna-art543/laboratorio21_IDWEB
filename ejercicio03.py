class OperadorInvalidoError(Exception):
    def __init__(self, operador):
        super().__init__(f"Operador inválido: '{operador}'. Use +, -, * o /")


def calcular_operacion(operacion):
    # Eliminar espacios extra y separar
    partes = operacion.strip().split()

    if len(partes) != 3:
        raise ValueError("Formato incorrecto. Ejemplo válido: 10 / 2")

    num1_str, operador, num2_str = partes

    try:
        numero1 = float(num1_str)
        numero2 = float(num2_str)
    except ValueError:
        raise ValueError("Los valores ingresados deben ser números")

    if operador not in ["+", "-", "*", "/"]:
        raise OperadorInvalidoError(operador)

    if operador == "+":
        return numero1 + numero2
    elif operador == "-":
        return numero1 - numero2
    elif operador == "*":
        return numero1 * numero2
    elif operador == "/":
        if numero2 == 0:
            raise ZeroDivisionError("No se puede dividir entre cero")
        return numero1 / numero2


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
