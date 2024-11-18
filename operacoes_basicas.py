def somar(a, b):
    """Retorna a soma de dois números."""
    return a + b


def subtrair(a, b):
    """Retorna a subtração de dois números."""
    return a - b


def multiplicar(a, b):
    """Retorna a multiplicação de dois números."""
    return a * b


def dividir(a, b):
    """Retorna a divisão de dois números. Levanta um erro se o divisor for zero."""
    if b == 0:
        raise ValueError("Divisão por zero não é permitida.")
    return a / b
