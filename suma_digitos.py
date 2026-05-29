def digitsSum(input_int: int) -> int:
    """Regresa la suma de los digitos"""
    return sum(int(digit) for digit in str(abs(input_int)))


def main() -> None:
    value = int(input("Ingresa un numero entero: "))
    print(digitsSum(value))


if __name__ == "__main__":
    main()
