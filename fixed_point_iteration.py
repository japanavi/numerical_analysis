

# Fixed Point Iteration Method
def fixed_point_iteration(p_0, tol, N, gn):
    """Finds a solution to p = g(p) given an initial approximation p0.

    Args:
        p_0 (float): Initial approximation
        tol (float): Tolerance
        N (int): Maximum number of iterations
        gn (function): Description of parameter `gn`.

    Returns:
        p (float): Solution to p = g(p)

    """
    i = 1
    while i <= N:
        p = gn(p_0)

        if abs(p - p_0) < tol:
            return p

        i += 1
        p_0 = p
        
    # Procedure was unsuccessful
    print(f"The Method failed after {N} iterations.")
