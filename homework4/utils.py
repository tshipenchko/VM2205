VARIABLES = ["x", "y", "z", "w", "v", "u", "t", "s", "r", "q", "p", "o", "n", "m"]


def dot_product(vec1, vec2):
    return sum(x * y for x, y in zip(vec1, vec2))


def print_equations(matrix_a, vector_b):
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
