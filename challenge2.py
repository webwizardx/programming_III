
def printMatrix(matrix):
    print(
        f"""|{matrix[0][0]}|{matrix[0][1]}|{matrix[0][2]}|
            \r|{matrix[1][2]}|{matrix[1][1]}|{matrix[1][0]}|
            \r|{matrix[2][0]}|{matrix[2][1]}|{matrix[2][2]}|
        """)


def main():
    """
    Programa para mostrar una matrix
    """
    matrix = [[], [], []]
    print("Ingrese los datos de la matrix")
    for i in range(0, len(matrix)):
        for j in range(0, 3):
            n = input(
                f"Ingrese el valos de la matrix en la posicion [{i}][{j}]:\n")
            matrix[i].append(n)

    print("Mostrando matrix\n")
    printMatrix(matrix=matrix)


if __name__ == '__main__':
    main()
