"""Educational text transformations; these are not cryptographic tools."""

def _transform_ascii(text: str, operation) -> str:
    """Apply an operation to ASCII letters while preserving case and punctuation."""
    result = []
    for char in text:
        if "a" <= char <= "z":
            base = ord("a")
            result.append(chr(base + operation(ord(char) - base) % 26))
        elif "A" <= char <= "Z":
            base = ord("A")
            result.append(chr(base + operation(ord(char) - base) % 26))
        else:
            result.append(char)
    return "".join(result)


def encode_system_1(text: str) -> str:
    """Caesar shift by +3."""
    return _transform_ascii(text, lambda value: value + 3)


def decode_system_1(text: str) -> str:
    """Reverse the Caesar shift by -3."""
    return _transform_ascii(text, lambda value: value - 3)


def encode_system_2(text: str) -> str:
    """Reversible affine substitution: E(x) = (5x + 8) mod 26."""
    return _transform_ascii(text, lambda value: 5 * value + 8)


def decode_system_2(text: str) -> str:
    """Reverse the affine substitution; 21 is the modular inverse of 5 mod 26."""
    return _transform_ascii(text, lambda value: 21 * (value - 8))


def main_menu() -> None:
    while True:
        print("\nCodificador didáctico")
        print("1. Codificar con César (+3)")
        print("2. Decodificar César")
        print("3. Codificar con sustitución afín")
        print("4. Decodificar sustitución afín")
        print("5. Salir")

        option = input("Opción: ").strip()
        if option == "5":
            print("Fin")
            return
        if option not in {"1", "2", "3", "4"}:
            print("Opción no válida.")
            continue

        text = input("Texto: ")
        operations = {
            "1": encode_system_1,
            "2": decode_system_1,
            "3": encode_system_2,
            "4": decode_system_2,
        }
        print("Resultado:", operations[option](text))


if __name__ == "__main__":
    main_menu()
