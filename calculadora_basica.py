"""Basic command-line calculator."""

def sumar(a: float, b: float) -> float:
    return a + b


def restar(a: float, b: float) -> float:
    return a - b


def multiplicar(a: float, b: float) -> float:
    return a * b


def dividir(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("No se puede dividir entre cero.")
    return a / b


def calculadora() -> None:
    operations = {
        "1": ("Suma", sumar),
        "2": ("Resta", restar),
        "3": ("Multiplicación", multiplicar),
        "4": ("División", dividir),
    }

    while True:
        print("\nCalculadora básica")
        for key, (label, _) in operations.items():
            print(f"{key}. {label}")
        print("0. Salir")

        option = input("Operación: ").strip()
        if option == "0":
            return
        if option not in operations:
            print("Opción no válida.")
            continue

        try:
            first = float(input("Primer número: "))
            second = float(input("Segundo número: "))
            result = operations[option][1](first, second)
        except ValueError:
            print("Introduce valores numéricos válidos.")
            continue
        except ZeroDivisionError as error:
            print(error)
            continue

        print("Resultado:", result)


if __name__ == "__main__":
    calculadora()
