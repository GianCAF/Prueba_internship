def integerSort(input_array: list[int]) -> list[int]:
    """Ordena una lista de enteros de menor a mayor"""
    sorted_array = input_array[:]

    for index in range(1, len(sorted_array)):
        current_value = sorted_array[index]
        position = index - 1

        while position >= 0 and sorted_array[position] > current_value:
            sorted_array[position + 1] = sorted_array[position]
            position -= 1

        sorted_array[position + 1] = current_value

    return sorted_array


def main() -> None:
    raw_numbers = input("Ingresa enteros separados por coma: ")
    numbers = [int(number.strip()) for number in raw_numbers.split(",") if number.strip()]
    print(integerSort(numbers))


if __name__ == "__main__":
    main()
