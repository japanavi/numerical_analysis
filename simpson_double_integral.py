def d(x):
    return 2*x

def c(x):
    return x

# Function we are approximating
def f(x, y):
    return x**2 + y**3


def simpson_double_integral(a, b, m, n, c, d, f):
    """Approximates a double integral using Simpson's Method.

    Args:
        a (float): Endpoint
        b (float): Endpoint
        m (int): Number of partitions (must be even  & positive)
        n (int): Number of partitions (must be even  & positive)
        c (function): Lower bounding function
        d (function): Upper bounding function
        f (function): Function to approximate

    Returns:
        J (float): Approximation

    """
    # Setting step size
    h = (b - a)/n
    J1 = 0     # End terms
    J2 = 0     # Even terms
    J3 = 0     # Odd terms

    # Compostie Simpson Method for x
    # The range function omits the last term, which is why the range is
    #  from 1 to n + 1, as this actually includes the endpoint n.
    for i in range(0, n+1):
        x = a + i*h
        HX = (d(x) - c(x))/m
        # End terms
        K1 = f(x, c(x)) + f(x, d(x))
        # Even terms
        K2 = 0
        # Odd terms
        K3 = 0

        # The range function omits the last term, which is why the range is
        #  only from 1 to m.
        for j in range(1, m):
            y = c(x) + j*HX
            Q = f(x, y)

            if j % 2 == 0:
                K2 = K2 + Q

            else:
                K3 = K3 + Q

        # L is the Composite Simpson approximation for the first integral
        L = (K1 + 2*K2 + 4*K3)*(HX/3)
        if i == 0 or i == n:
            J1 = J1 + L

        elif i % 2 == 0:
            J2 = J2 + L

        else:
            J3 = J3 + L

    # Calculates final approximation
    J = (J1 + 2*J2 + 4*J3)*(h/3)

    return J

print(simpson_double_integral(2, 2.2, 4, 4, c, d, f))
# Outputs: 16.50864062500002
