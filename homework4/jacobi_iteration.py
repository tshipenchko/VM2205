from utils import VARIABLES, dot_product, print_equations


def main():
    # You have to place them in the right order
    matrix_a = [
        [8, 5, 2],
        [2, 10, -2],
        [1, 3, 6],
    ]
    vector_b = [25, 20, 30]
    x0 = [0] * len(vector_b)

    print("System of Equations:")
    for equation in print_equations(matrix_a, vector_b):
        print(equation)

    solution = jacobi_iteration(matrix_a, vector_b, x0)
    print("\nSolution using Jacobi's iteration method:")
    for i, val in enumerate(solution):
        print(f"{VARIABLES[i]} = {val}")


def jacobi_iteration(matrix_a, vector_b, x0, tol=1e-6, max_iter=1000):
    n = len(vector_b)
    x = x0[:]
    for _ in range(max_iter):
        x_new = [0] * n
        for i in range(n):
            x_new[i] = (
                vector_b[i]
                - dot_product(matrix_a[i][:i], x[:i])
                - dot_product(matrix_a[i][i + 1 :], x[i + 1 :])
            ) / matrix_a[i][i]
        if max(abs(x_new[i] - x[i]) for i in range(n)) < tol:
            return x_new
        x = x_new
    return x


if __name__ == "__main__":
    main()
