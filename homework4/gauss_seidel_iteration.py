from utils import dot_product, print_equations, print_relative_error, print_values


def main():
    # You have to place them in the right order
    matrix_a = [
        [8, 5, 2],
        [2, 10, -2],
        [1, 3, 6],
    ]
    vector_b = [25, 20, 30]
    x0 = [0] * len(vector_b)

    print_equations(matrix_a, vector_b)
    solution = gauss_seidel_iteration(matrix_a, vector_b, x0, max_iter=10)
    print_values(solution, "Solution using Gauss-Seidel iteration method")
    print_relative_error(solution, matrix_a, vector_b)


def gauss_seidel_iteration(matrix_a, vector_b, x0, tol=1e-6, max_iter=1000):
    n = len(vector_b)
    x = x0[:]
    for _ in range(max_iter):
        x_new = [0] * n
        for i in range(n):
            x_new[i] = (
                vector_b[i]
                - dot_product(matrix_a[i][:i], x_new[:i])
                - dot_product(matrix_a[i][i + 1 :], x[i + 1 :])
            ) / matrix_a[i][i]
        if max(abs(x_new[i] - x[i]) for i in range(n)) < tol:
            return x_new
        x = x_new
    return x


if __name__ == "__main__":
    main()
