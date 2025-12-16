class OperadorInvalidoError(Exception):
    pass


def calcular_operacion(operacion):
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
        raise OperadorInvalidoError("Operador inválido")

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
