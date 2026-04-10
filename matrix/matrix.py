def read_matrix():
    rows, cols = map(int, input("Enter matrix size: ").split())
    print("Enter matrix:")
    matrix = []
    for i in range(rows):
        row = list(map(float, input().split()))
        matrix.append(row)
    return matrix
def print_matrix(matrix):
    print("The result is:")
    for row in matrix:
        output_row = []
        for num in row:
            if num == int(num):
                output_row.append(str(int(num)))
            else:
                output_row.append(str(num))
        print(" ".join(output_row))
def add_matrices(a, b):
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        print("The operation cannot be performed.")
        return
    result = []
    for i in range(len(a)):
        row = []
        for j in range(len(a[0])):
            row.append(a[i][j] + b[i][j])
        result.append(row)
    print_matrix(result)
def multiply_by_constant(matrix, constant):
    result = []
    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix[0])):
            row.append(matrix[i][j] * constant)
        result.append(row)
    print_matrix(result)
def multiply_matrices(a, b):
    if len(a[0]) != len(b):
        print("The operation cannot be performed.")
        return
    result = []
    for i in range(len(a)):
        row = []
        for j in range(len(b[0])):
            total = 0
            for k in range(len(b)):
                total += a[i][k] * b[k][j]
            row.append(total)
        result.append(row)
    print_matrix(result)
def transpose_main(matrix):
    result = []
    for j in range(len(matrix[0])):
        row = []
        for i in range(len(matrix)):
            row.append(matrix[i][j])
        result.append(row)
    return result
def transpose_side(matrix):
    result = []
    rows = len(matrix)
    cols = len(matrix[0])
    for j in range(cols):
        row = []
        for i in range(rows):
            row.append(matrix[rows - 1 - i][cols - 1 - j])
        result.append(row)
    return result
def transpose_vertical(matrix):
    result = []
    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix[0]) - 1, -1, -1):
            row.append(matrix[i][j])
        result.append(row)
    return result
def transpose_horizontal(matrix):
    result = []
    for i in range(len(matrix) - 1, -1, -1):
        row = []
        for j in range(len(matrix[0])):
            row.append(matrix[i][j])
        result.append(row)
    return result
def determinant(matrix):
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    det = 0
    for col in range(n):
        minor = []
        for i in range(1, n):
            row = []
            for j in range(n):
                if j != col:
                    row.append(matrix[i][j])
            minor.append(row)
        det += ((-1) ** col) * matrix[0][col] * determinant(minor)
    return det
def inverse_matrix(matrix):
    det = determinant(matrix)
    if det == 0:
        print("This matrix doesn't have an inverse.")
        return
    n = len(matrix)
    cofactors = []
    for i in range(n):
        cofactor_row = []
        for j in range(n):
            minor = []
            for r in range(n):
                if r == i:
                    continue
                row = []
                for c in range(n):
                    if c == j:
                        continue
                    row.append(matrix[r][c])
                minor.append(row)
            cofactor = ((-1) ** (i + j)) * determinant(minor)
            cofactor_row.append(cofactor)
        cofactors.append(cofactor_row)
    adjugate = transpose_main(cofactors)
    result = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(adjugate[i][j] / det)
        result.append(row)
    print_matrix(result)
while True:
    print("1. Add matrices")
    print("2. Multiply matrix by a constant")
    print("3. Multiply matrices")
    print("4. Transpose matrix")
    print("5. Calculate a determinant")
    print("6. Inverse matrix")
    print("0. Exit")
    choice = input("Your choice: ")
    if choice == "1":
        print("Enter size of first matrix:")
        a = read_matrix()
        print("Enter size of second matrix:")
        b = read_matrix()
        add_matrices(a, b)
    elif choice == "2":
        matrix = read_matrix()
        constant = float(input("Enter constant: "))
        multiply_by_constant(matrix, constant)
    elif choice == "3":
        print("Enter size of first matrix:")
        a = read_matrix()
        print("Enter size of second matrix:")
        b = read_matrix()
        multiply_matrices(a, b)
    elif choice == "4":
        print("1. Main diagonal")
        print("2. Side diagonal")
        print("3. Vertical line")
        print("4. Horizontal line")
        transpose_choice = input("Your choice: ")
        matrix = read_matrix()
        if transpose_choice == "1":
            print_matrix(transpose_main(matrix))
        elif transpose_choice == "2":
            print_matrix(transpose_side(matrix))
        elif transpose_choice == "3":
            print_matrix(transpose_vertical(matrix))
        elif transpose_choice == "4":
            print_matrix(transpose_horizontal(matrix))
    elif choice == "5":
        matrix = read_matrix()
        print("The result is:")
        det = determinant(matrix)
        if det == int(det):
            print(int(det))
        else:
            print(det)
    elif choice == "6":
        matrix = read_matrix()
        if len(matrix) != len(matrix[0]):
            print("This matrix doesn't have an inverse.")
        else:
            inverse_matrix(matrix)
    elif choice == "0":
        break
    print()