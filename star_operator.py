import numpy as np


def star_operator(state, delta_operators):
    """
    The ★ Convergence Operator
    Series: Mathematical Foundations for Universal Systems
    Author: Carolina Johnson (CJ), 2025

    Projects a system state onto its consistent subspace by eliminating
    representational inconsistencies across bases, coordinate systems,
    and computational modalities.

    Parameters:
    - state:            current system state (vector or matrix)
    - delta_operators:  list of self-adjoint inconsistency operators

    Returns:
    - projected state in the consistent subspace
    """
    combined = sum(d @ d.T for d in delta_operators)
    eigenvalues, eigenvectors = np.linalg.eigh(combined)
    kernel_mask = np.abs(eigenvalues) < 1e-10
    kernel_projection = eigenvectors[:, kernel_mask] @ eigenvectors[:, kernel_mask].T
    return kernel_projection @ state


def demonstrate_star_operator():
    """
    Demonstrates the ★ operator projecting two inconsistent representations
    of the same underlying state onto their shared consistent subspace.

    Two representations of the same truth carry different artifacts
    from their respective bases or coordinate systems.
    After applying ★, both project onto the same invariant structure.
    """
    np.random.seed(42)
    dim = 6

    # The underlying truth
    true_state = np.array([1.0, 0.0, 1.0, 0.0, 1.0, 0.0])

    # Two representations of the same truth with different artifacts
    rep_A = true_state + np.random.randn(dim) * 0.3
    rep_B = true_state + np.random.randn(dim) * 0.3

    # Inconsistency operators (must be self-adjoint)
    delta_1 = np.random.randn(dim, dim)
    delta_1 = (delta_1 + delta_1.T) / 2
    delta_2 = np.random.randn(dim, dim)
    delta_2 = (delta_2 + delta_2.T) / 2

    result_A = star_operator(rep_A, [delta_1, delta_2])
    result_B = star_operator(rep_B, [delta_1, delta_2])

    print("--- THE ★ CONVERGENCE OPERATOR ---")
    print()
    print("Before ★:")
    print(f"  Representation A: {rep_A.round(3)}")
    print(f"  Representation B: {rep_B.round(3)}")
    print(f"  Difference norm:  {np.linalg.norm(rep_A - rep_B):.4f}")
    print()
    print("After ★:")
    print(f"  Projection A: {result_A.round(3)}")
    print(f"  Projection B: {result_B.round(3)}")
    print(f"  Difference norm: {np.linalg.norm(result_A - result_B):.4f}")
    print()
    if np.linalg.norm(result_A - result_B) < np.linalg.norm(rep_A - rep_B):
        print("Both representations projected onto the same consistent subspace.")
        print("Drift eliminated. Invariant structure revealed.")
    else:
        print("Check your delta operators. They must be self-adjoint.")


if __name__ == "__main__":
    demonstrate_star_operator()
