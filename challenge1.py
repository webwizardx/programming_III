def main():
    letters = [chr(i) for i in range(65, 91)]
    numbers = [str(i) for i in range(0, 10)]

    def permutations(plate: str = '', position: int = 0):
        if position == 6:
            print(plate)
            return

        characters = letters if position < 3 else numbers
        for char in characters:
            newPlate = f'{plate}{char}'
            permutations(newPlate, position + 1)

    permutations()


if __name__ == '__main__':
    main()
