

def f(x):
    return (10 / (x+4))**0.5

def steffensen_method(p0, tol, N, f):
    """Finds a solution to p = f(p) given an initial approximation p0.

    Args:
        p0 (float): Initial approximation
        tol (float): Tolerance
        N (int): Maximum number of iterations
        f (function): Function to approximate

    Returns:
        p (float): Solution to p = f(p)

    """
    # Start iterations
    i = 1
    while i <= N:
        p1 = f(p0)
        p2 = f(p1)
        p = p0 - ((p1 - p0)**(2)) / (p2 - 2*p1 + p0)

        if abs(p - p0) < tol:
            # Procedure was successful
            return p
        # Continue iterations
        i += 1
        # Update p0
        p0 = p
    # Procedure was unsuccessful
    return print(f'Method failed after {N} iterations')

print(steffensen_method(1.5, 1e-8, 3, f))
# Outputs: 1.3652300134140969
