

def f(x):
    return x**2 - 1


def df(x):
    return 2 * x


def newtons_method(p0, tol, N, f, df):
    """Finds a solution to f(x) = 0 given an initial approximation p0.

    Args:
        p0 (float): Initial approximation
        tol (float): Tolerance
        N (int): Maximum number of iterations
        f (function): Function to approximate
        df (function): Derivative of f

    Returns:
        p (float): Solution to f(x) = 0

    """
    # Start iterations
    i = 1
    while i <= N:
        p = p0 - (f(p0)/df(p0))
        if abs(p - p0) < tol:
            # Procedure was successful
            return p

        i += 1
        p0 = p
    # Procedure was unsuccessful
    return print(f"The method failed after {N} iterations.")

print(newtons_method(0.5, 1e-4, 10, f, df))
# Outputs: 1.000000000000001
