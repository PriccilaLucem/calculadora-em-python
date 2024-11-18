def validar_numeros(*args):
    """Verifica se todos os argumentos fornecidos são números."""
    for arg in args:
        if not isinstance(arg, (int, float)):
            raise TypeError(f"O valor {arg} não é um número.")
