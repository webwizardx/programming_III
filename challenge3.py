def encrypt(text: str, moves: int, isDecrypting: bool = False) -> str:
    moves %= 26
    if isDecrypting:
        moves *= -1

    encryptedText = ''
    for i in range(len(text)):
        char = text[i]
        if not char.isalpha():
            encryptedText += char
            continue

        if (char.isupper()):
            encryptedText += chr((ord(char) + moves - 65) % 26 + 65)
        else:
            encryptedText += chr((ord(char) + moves - 97) % 26 + 97)
    return encryptedText


def menu():
    print('Seleccione una opcion')
    print('Ingrese 1 para encriptar')
    print('Ingrese 2 para desencriptar')
    choice = input()
    while choice != '1' and choice != '2':
        print('Opcion no valida. Intente nuevamente\n')
        print('Seleccione una opcion')
        print('Ingrese 1 para encriptar')
        print('Ingrese 2 para desencriptar')
        choice = input('\n')
    return choice


def main():
    choice = menu()

    if choice == '1':
        text = input("Ingrese el texto a encriptar:\n")
        moves = int(
            input("Ingrese clave para el encriptado (Debe ser un numero):\n"))
        print(f'Texto original: {text}')
        print(f'Texto encriptado: {encrypt(text=text, moves=moves)}')
    else:
        text = input("Ingrese el texto a desencriptar:\n")
        moves = int(
            input("Ingrese clave para el desencriptado (Debe ser un numero):\n"))
        print(f'Texto original: {text}')
        print(
            f'Texto encriptado: {encrypt(text=text, moves=moves, isDecrypting=True)}')


if __name__ == "__main__":
    main()
