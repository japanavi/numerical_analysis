
# Function whose integral we are approximating
def f(x, y, z):
    return (x*y*z)**0.5
# Function definition
def beta(x, y):
    return 8 - x - y
# Function definition
def alpha(x, y):
    return (4 - x**2 - y**2)**0.5
# Function definition
def d(x):
    return (4 - x**2)**0.5
# Function definition
def c(x):
    return 0

# Relevant Roots
R5 = [0.9061798459, 0.5384693101, 0, - 0.5384693101, - 0.9061798459]
# Relevant Coefficients
C5 = [0.2369268850, 0.4786286705, 0.5688888889, 0.4786286705, 0.2369268850]

def gaussian_triple_integral(a, b, m, n, p):
    """Returns an approximation to a triple integral using Gaussian
    Quadrature.

    Args:
        a (float): Left endpoint
        b (float): right endpoint
        m (int): Positive
        n (int): Positive
        p (int): Positive

    Returns:
        J (float): Triple integral approximation to f

    """
    h1 = (b - a)/2
    h2 = (b + a)/2
    J = 0

    for i in range(1, m+1):
        JX = 0
        x = h1*R5[i-1] + h2
        d1 = d(x)
        c1 = c(x)
        k1 = (d1 - c1)/2
        k2 = (d1 + c1)/2

        for j in range(1, n+1):
            JY = 0
            y = k1*R5[j-1] + k2
            beta1 = beta(x, y)
            alpha1 = alpha(x, y)
            l1 = (beta1 - alpha1)/2
            l2 = (beta1 + alpha1)/2

            for k in range(1, p+1):
                z = l1*R5[k-1] + l2
                Q = f(x, y, z)
                JY = JY + C5[k-1]*Q

            JX = JX + C5[j-1]*l1*JY

        J = J + C5[i-1]*k1*JX

    J = h1*J

    # Returning approximation
    return J

# Printing function call
print(gaussian_triple_integral(0, 2, 5, 5, 5))
# The above outputs: J = 20.418871571757997
