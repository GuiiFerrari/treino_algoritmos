import cvxpy as cp
import numpy as np

from numpy.typing import NDArray
from scipy.linalg import cholesky


def is_psd(matrix: NDArray) -> bool:
    if not np.array_equal(matrix, matrix.T):
        return False
    eigenvalues = np.linalg.eigvals(matrix)
    if any(np.diagonal(matrix) < 0.0):
        return False
    if any(eigenvalues < 0.0):
        return False
    # Verify all submatrices
    mask = np.array([True] * matrix.shape[0])
    for i in range(len(matrix)):
        mask_i = mask.copy()
        mask_i[i] = False
        matrix_i = matrix[mask_i, :][:, mask_i]
        if np.linalg.det(matrix_i) < 0.0:
            return False
    print()


def block_cholesky(matrix: NDArray) -> NDArray:

    # ==========================================
    # 1. Setup: Your "Broken" Matrix
    # ==========================================
    n = 6
    # Let's assume 'matrix' is your 6x6 matrix where the 5x5 is historical,
    # and the 6th row/col breaks the PSD property.
    # (Replace this mock 'matrix' with your actual numpy array)

    # Quick check: This will likely raise an error because matrix is not PSD
    try:
        np.linalg.cholesky(matrix)
    except np.linalg.LinAlgError:
        print("Confirmed: Original matrix is NOT Positive Semidefinite.\n")

    # ==========================================
    # 2. CVXPY Optimization Setup
    # ==========================================
    # Define the variable. 'symmetric=True' applies our dimension reduction math!
    X = cp.Variable((n, n), symmetric=True)

    # Define the Weight Matrix (W)
    W = np.ones((n, n))
    W[:5, :5] = 100.0  # Heavy penalty for changing the historical 5x5 block
    W[5, :] = 1.0  # Allow the 6th row/col to shift freely
    W[:, 5] = 1.0

    # Objective: Minimize Weighted Frobenius Norm
    # cp.multiply does element-wise (Hadamard) multiplication
    objective = cp.Minimize(cp.norm(cp.multiply(W, X - matrix), "fro"))

    # Constraints
    # X >> 0 is CVXPY's syntax for Positive Semidefinite (X ⪰ 0)
    constraints = [X >> 0, cp.diag(X) == 1]  # Must be a valid correlation matrix

    # The Epsilon Bound (Soft Lock on the 5x5 history)
    epsilon = 0.01  # Allow maximum 1% shift in historical correlations
    for i in range(5):
        for j in range(
            i + 1, 5
        ):  # Only loop upper triangle to avoid redundant constraints
            constraints.append(cp.abs(X[i, j] - matrix[i, j]) <= epsilon)

    # ==========================================
    # 3. Solve the Problem
    # ==========================================
    prob = cp.Problem(objective, constraints)

    # SCS or CVXOPT are good solvers for SDP (Semidefinite Programming) problems
    prob.solve(solver=cp.SCS, verbose=True)
    # prob.solve(solver=cp.CVXOPT, verbose=True)

    if prob.status not in ["optimal", "optimal_inaccurate"]:
        print(f"Optimization failed. Status: {prob.status}")
        # If it fails, you may need to increase epsilon
    else:
        print("Optimization Successful!")
        X_optimal = X.value

        # Clean up floating point noise (e.g., exact 1.0 on diagonals)
        np.fill_diagonal(X_optimal, 1.0)
        min_eig = np.min(np.linalg.eigvals(X_optimal))
        if min_eig < 0:
            print(f"Applying numerical fix. Lowest eigenvalue was: {min_eig}")
            X_optimal += np.eye(n) * max(-min_eig + 1e-8, 1e-8)

        # ==========================================
        # 4. Extract the Cholesky Decomposition
        # ==========================================
        # scipy's cholesky with lower=True gives the L matrix (A = L * L.T)
        L = cholesky(X_optimal, lower=True)

        print("\nOptimized PSD Correlation Matrix (X):")
        print(np.round(X_optimal, 3))

        print("\nLower Triangular Cholesky Matrix (L):")
        print(np.round(L, 3))


def main():
    #     A = np.array([[4, 2, 1], [2, 3, 1], [1, 1, 0.5]], dtype=float)
    A = np.array(
        [
            [1.00, 0.80, 0.50, 0.30, 0.20, 0.90],
            [0.80, 1.00, 0.60, 0.40, 0.30, -0.80],  # Contradictory 6th factor
            [0.50, 0.60, 1.00, 0.70, 0.50, 0.10],
            [0.30, 0.40, 0.70, 1.00, 0.60, 0.20],
            [0.20, 0.30, 0.50, 0.60, 1.00, 0.05],
            [0.90, -0.80, 0.10, 0.20, 0.05, 1.00],
        ]
    )
    # res = is_psd(matrix=A)
    res = block_cholesky(matrix=A)


if __name__ == "__main__":
    main()
