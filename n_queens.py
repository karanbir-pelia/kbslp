
def print_matrix(matrix: list[list[int]]) -> None:
    for row in matrix:
        for value in row:
            print(value, end="  ")
        print()


def is_safe(matrix: list[list[int]], row_number: int,  column_number: int) -> bool:

    for row in range(row_number):
        if matrix[row][column_number] == 1:
            return False

    row = row_number
    column = column_number

    while row >= 0 and column >= 0:
        if matrix[row][column] == 1:
            return False
        row -= 1
        column -= 1

    row = row_number
    column = column_number

    while row >= 0 and column < len(matrix):
        if matrix[row][column] == 1:
            return False
        row -= 1
        column += 1

    return True


def n_queen(matrix: list[list[int]], row_number: int) -> bool:

    if row_number == len(matrix):
        return True

    for column_number in range(len(matrix)):
        if is_safe(matrix, row_number, column_number):
            matrix[row_number][column_number] = 1

            if n_queen(matrix, row_number + 1):
                return True

            matrix[row_number][column_number] = 0

    return False


if __name__ == "__main__":
    n = input("\nEnter the value for n : ")

    while not (n.isdigit() and int(n) > 0):
        print("\nEnter positive integer value.")
        n = input("\nEnter the value for n : ")

    matrix = [[0 for _ in range(int(n))] for _ in range(int(n))]

    if n_queen(matrix, 0):
        print_matrix(matrix)
