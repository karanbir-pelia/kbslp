
def print_matrix(matrix: list[list[int]]) -> None:
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == -1:
                print(end="   ")
            else:
                print(matrix[i][j], end="  ")
        print()


def calculate_f_n(current_matrix: list[list[int]], final_matrix: list[list[int]], initial_value) -> int:
    for i in range(len(current_matrix)):
        for j in range(len(current_matrix)):
            if current_matrix[i][j] != final_matrix[i][j]:
                initial_value += 1

    return initial_value


initial_matrix = [
    [2, 8, 3],
    [1, 6, 4],
    [7, -1, 5]
]

final_matrix = [
    [1, 2, 3],
    [8, -1, 4],
    [7, 6, 5]
]

f_n = calculate_f_n(initial_matrix, final_matrix, 0)

print(f"\nInitial matrix:\n")
print_matrix(initial_matrix)
print(f"\nFinal matrix:\n")
print_matrix(final_matrix)
print(f"\nf(n) = {f_n}")


current_matrix = previous_matrix = initial_matrix

level = 0

while current_matrix != final_matrix:

    level += 1

    blank_position = []

    for i in range(len(current_matrix)):
        for j in range(len(current_matrix[i])):
            if current_matrix[i][j] == -1:
                blank_position = [i, j]
                break

    movable_positions = []

    if blank_position[0] != 0:
        movable_positions.append([blank_position[0] - 1, blank_position[1]])

    if blank_position[0] != len(current_matrix) - 1:
        movable_positions.append([blank_position[0] + 1, blank_position[1]])

    if blank_position[1] != 0:
        movable_positions.append([blank_position[0], blank_position[1] - 1])

    if blank_position[1] != len(current_matrix[0]) - 1:
        movable_positions.append([blank_position[0], blank_position[1] + 1])

    alternate_matrices = [[row.copy() for row in current_matrix]
                          for _ in range(len(movable_positions))]

    f_ns = [level] * len(movable_positions)

    for i in range(len(movable_positions)):

        alternate_matrices[i][
            blank_position[0]][blank_position[1]] = alternate_matrices[i][movable_positions[i][0]][movable_positions[i][1]]
        alternate_matrices[i][
            movable_positions[i][0]][movable_positions[i][1]] = -1

        f_ns[i] = calculate_f_n(alternate_matrices[i], final_matrix, f_ns[i])

    for alternate_matrix in alternate_matrices:
        if alternate_matrix == previous_matrix:
            del f_ns[alternate_matrices.index(previous_matrix)]
            del alternate_matrices[alternate_matrices.index(previous_matrix)]

    print(f"\n\nLevel {level} has {len(alternate_matrices)} alternatives:")

    for i in range(len(alternate_matrices)):
        print(f"\nAlternate Matrix {i + 1}:\n")
        print_matrix(alternate_matrices[i])
        print(f"\nf(n) = {f_ns[i]}")

    previous_matrix = current_matrix
    current_matrix = alternate_matrices[f_ns.index(min(f_ns))]

    print(f"\n\nCurrent matrix:\n")
    print_matrix(current_matrix)

print("\nHence, we have obtained the final matrix.\n")
