import math

def f(t, y):
    return -t*y + 4*(t/4)

def g(t):
    return (4 - 3*math.e**-t**2)**0.5


def euler_method(a, b, alpha, N):
    """Short summary.

    Args:
        a (type): Description of parameter `a`.
        b (type): Description of parameter `b`.
        alpha (type): Description of parameter `alpha`.
        N (type): Description of parameter `N`.

    Returns:
        type: Description of returned object.

    """
    h = (b - a)/N
    t = a
    w = alpha
    print("t =", t, "      w = ", w)

    for i in range(1, N+1):
        w = w + h*f(t, w)
        t = a + i*h
        act = g(t)
        error = abs(w - act)
        print("t =", t, "    w = ", w, "    Actual =", act, "    Error =", error)

#euler_method(0, 1, 0, 10)
#print()
#euler_method(0, 1, 0, 100)

def modified_euler_method(a, b, alpha, N):
    """Short summary.

    Args:
        a (type): Description of parameter `a`.
        b (type): Description of parameter `b`.
        alpha (type): Description of parameter `alpha`.
        N (type): Description of parameter `N`.

    Returns:
        type: Description of returned object.

    """
    h = (b - a)/N
    t = a
    w = alpha
    print("t =", t, "      w = ", w)

    for i in range(1, N+1):
        w = w + (h/2)*(f(t, w) + f(t+h, w + h*f(t, w)))
        t = a + i*h
        act = g(t)
        error = abs(w - act)
        print("t =", t, "    w = ", w, "    Actual =", act, "    Error =", error)

#modified_euler_method(1, 2, g(1), 10)

def midpoint_method(a, b, alpha, N):
    """Short summary.

    Args:
        a (type): Description of parameter `a`.
        b (type): Description of parameter `b`.
        alpha (type): Description of parameter `alpha`.
        N (type): Description of parameter `N`.

    Returns:
        type: Description of returned object.

    """
    h = (b - a)/N
    t = a
    w = alpha
    print("t =", t, "      w = ", w)

    for i in range(1, N+1):
        w = w + h*(f(t+(h/2), w+(h/2)*f(t, w)))
        t = a + i*h
        act = g(t)
        error = abs(w - act)
        print("t =", t, "    w = ", w, "    Actual =", act, "    Error =", error)

midpoint_method(0, 1, 1, 10)

def heun_method(a, b, alpha, N):
    """Short summary.

    Args:
        a (type): Description of parameter `a`.
        b (type): Description of parameter `b`.
        alpha (type): Description of parameter `alpha`.
        N (type): Description of parameter `N`.

    Returns:
        type: Description of returned object.

    """
        h = (b - a)/N
        t = a
        w = alpha
        print("t =", t, "      w = ", w)

        for i in range(1, N+1):
            w = w + (h/4)*(f(t, w) + 3*f(t+(2*h/3), w+(2*h/3)*f(t+(h/3), \
            w+(h/3)*f(t,w))))
            t = a + i*h
            act = g(t)
            error = abs(w - act)
            print("t =", t, "    w = ", w, "    Actual =", act, "    Error =", error)

#heun_method(1, 2, g(1), 10)

def f(t, y):
    k = 6.22*10**-19
    n1 = 2000
    n2 = 2000
    n3 = 3000

    return k*(((n1 - y/2)**2)*((n2 - y/2)**2)*((n3 - 3*y/4)**3))


def runge_kutta_method4(a, b, N, alpha):
    """Short summary.

    Args:
        a (type): Description of parameter `a`.
        b (type): Description of parameter `b`.
        N (type): Description of parameter `N`.
        alpha (type): Description of parameter `alpha`.

    Returns:
        type: Description of returned object.

    """
    # Setting step size
    h = (b - a)/N
    t = a
    w = alpha

    # Carrying out method
    for i in range(1, N+1):
        # Using K variable to eliminate excessive nesting of f(t, w)
        K1 = h*f(t,w)
        K2 = h*f(t+(h/2), w + (K1/2))
        K3 = h*f(t+(h/2), w + (K2/2))
        K4 = h*f(t+h, w+K3)

        # Computing wi
        w = w + (K1 + 2*K2 + 2*K3 + K4)/6
        # Computing ti
        t = a + i*h

        print('t =', t, 'w =', w)

runge_kutta_method4(0, 0.2, 20, 0)
