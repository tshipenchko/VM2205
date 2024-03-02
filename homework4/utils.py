VARIABLES = ["x", "y", "z", "w", "v", "u", "t", "s", "r", "q", "p", "o", "n", "m"]


def dot_product(vec1, vec2):
    return sum(x * y for x, y in zip(vec1, vec2))


def generate_equations(matrix_a, vector_b):
    n = len(vector_b)
    equations = []
    for i in range(n):
        equation = ""
        for j in range(n):
            if j > 0:
                equation += " + " if matrix_a[i][j] >= 0 else " - "
            equation += f"{abs(matrix_a[i][j])}{VARIABLES[j]}"
        equation += f" = {vector_b[i]}"
        equations.append(equation)
    return equations


def print_equations(matrix_a, vector_b, label="System of Equations:"):
    print(label)
    for equation in generate_equations(matrix_a, vector_b):
        print(equation)


def percentage_relative_error(real_values, approx_values):
    return [
        abs((real - approx) / real) * 100
        for real, approx in zip(real_values, approx_values)
    ]


def print_values(values, label):
    print(f"{label}:")
    for i, val in enumerate(values):
        print(f"{VARIABLES[i]} = {val:.8f}")


def print_relative_error(solution, matrix_a, vector_b):
    approx_values = [dot_product(row, solution) for row in matrix_a]
    errors = percentage_relative_error(vector_b, approx_values)
    print_values(errors, "Percentage Relative Error")
