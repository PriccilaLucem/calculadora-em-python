import math

def potencia(base, expoente):
    """Retorna a base elevada ao expoente."""
    return base ** expoente


def raiz_quadrada(numero):
    """Retorna a raiz quadrada de um número. Levanta um erro para números negativos."""
    if numero < 0:
        raise ValueError("Raiz quadrada de número negativo não é permitida.")
    return math.sqrt(numero)
