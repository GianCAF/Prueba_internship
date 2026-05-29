def isPalindrome(input_str: str) -> bool:
    """Verifica si un texto se escribe igual sin importar porque lado se inicie a leer"""
    clean_text = "".join(char.lower() for char in input_str if char.isalnum())
    return clean_text == clean_text[::-1]


def main() -> None:
    text = input("Ingresa un texto: ")
    print(isPalindrome(text))


if __name__ == "__main__":
    main()
