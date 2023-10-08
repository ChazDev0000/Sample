def matrix_addition(matrix1, matrix2):
    rows1 = len(matrix1)
    cols1 = len(matrix1[0])
    rows2 = len(matrix2)
    cols2 = len(matrix2[0])

    # Check if multiplication is possible
    if cols1 != rows2:
        print("Invalid dimensions for addition.")
        return None

    # Initialize the result matrix with zeros
    result = [[0 for _ in range(cols2)] for _ in range(rows1)]

    # Perform matrix multiplication
    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                result[i][j] += matrix1[i][k] + matrix2[k][j]

    return result

def get_matrix_from_user():
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))

    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            element = float(input(f"Enter element at position ({i+1}, {j+1}): "))
            row.append(element)
        matrix.append(row)

    return matrix

# Get input matrices from user
print("Enter details for the first matrix:")
matrix1 = get_matrix_from_user()

print("\nEnter details for the second matrix:")
matrix2 = get_matrix_from_user()

# Multiply matrices
result = matrix_multiplication(matrix1, matrix2)

# Print result
if result is not None:
    print("\nThe result of addition is:")
    for row in result:
        print(row)
