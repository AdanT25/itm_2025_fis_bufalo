def romano_a_entero(romano: str) -> int:
    """
    Convierte un número romano válido a un entero.
    Soporta notación sustractiva: IV, IX, XL, XC, CD, CM.
    """
    valores = {
        "I": 1, "V": 5,
        "X": 10, "L": 50,
        "C": 100, "D": 500,
        "M": 1000,
    }

    total = 0
    previo = 0

    # Trabajamos siempre en mayúsculas
    for letra in reversed(romano.upper()):
        valor = valores[letra]
        if valor < previo:
            total -= valor
        else:
            total += valor
        previo = valor

    return total


def entero_a_romano(numero: int) -> str:
    """
    Convierte un entero entre 1 y 3999 a número romano estándar.

    Ejemplos:
        4    -> IV
        9    -> IX
        58   -> LVIII
        1994 -> MCMXCIV
    """
    if numero < 1 or numero > 3999:
        raise ValueError("El número debe estar entre 1 y 3999 para convertir a romano.")

    valores = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"),
        (1, "I"),
    ]

    resultado = ""

    for valor, simbolo in valores:
        while numero >= valor:
            resultado += simbolo
            numero -= valor

    return resultado


# =====================================
#     🚀 SCANNER INTERACTIVO
# =====================================
if __name__ == "__main__":
    print("Conversor Romano <-> Entero (1–3999)")
    dato = input("Escribe un número romano o entero: ")

    if dato.isdigit():
        numero = int(dato)
        try:
            romano = entero_a_romano(numero)
            print(f"{numero} en romano es: {romano}")
        except ValueError as e:
            print("Error:", e)
    else:
        try:
            entero = romano_a_entero(dato)
            print(f"{dato} en entero es: {entero}")
        except KeyError:
            print("Error: número romano no válido.")
