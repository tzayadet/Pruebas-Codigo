"""Standalone menu for reversing the educational Caesar-shift example."""

from codificador import decode_system_1


def main() -> None:
    print("Decodificador César (+3)")
    text = input("Texto codificado: ")
    print("Texto decodificado:", decode_system_1(text))


if __name__ == "__main__":
    main()
