from math import cos


def f(x):
    return cos(x)


def secant_method(p0, p1, tol, N, f):
    """Finds a solution to f(x) = 0 given initial appromximations p0 and p1.

    Args:
        p0 (float): Description of parameter `p0`.
        p1 (float): Description of parameter `p1`.
        tol (float): Tolerance
        N (int): Maximum number of iterations
        f (function): Function to approximate

    Returns:
        p (float): Description of returned object.

    """
    # Start iterations
    i = 2
    q0 = f(p0)
    q1 = f(p1)
    while i <= N:
        # Compute pi
        p = p1 - q1 * ((p1 - p0)/(q1 - q0))

        if abs(p - p1) < tol:
            # Procedure was successful
            return p

        # Continue iterations
        i += 1

        p0 = p1
        q0 = q1
        p1 = p
        q1 = f(p)
    # Procedure was unsuccessful
    return print(f'The method failed after {N} iterations.')

print(secant_method(0.5, 2, 1e-8, 10, f))
# Outputs: 1.5707963267948966
