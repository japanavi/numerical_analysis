
import math
import matplotlib.pyplot as plt

k1 = 3
k2 = 0.002
k3 = 0.0006
k4 = 0.5

def F1(t, X1, X2):
    return k1*X1 - k2*X1*X2

def F2(t, X1, X2):
    return k3*X1*X2 - k4*X2

def runga_kutta_sys2(a, b, m, N, alpha1, alpha2):
    """Short summary.

    Args:
        a (type): Description of parameter `a`.
        b (type): Description of parameter `b`.
        m (type): Description of parameter `m`.
        N (type): Description of parameter `N`.
        alpha1 (type): Description of parameter `alpha1`.
        alpha2 (type): Description of parameter `alpha2`.

    Returns:
        type: Description of returned object.

    """
    h = (b - a) / N
    t = a
    # STEP 2
    W1 = alpha1
    W2 = alpha2
    # STEP 3
    print('t = ',t, 'w1 =',W1, 'w2 =', W2)
    TP = [0]
    y1 = [1000]
    y2 = [500]

    # STEP 4
    for i in range(1, N+1):
        # STEP 5
        X11 = h * F1(t, W1, W2)
        X12 = h * F2(t, W1, W2)
        # STEP 6
        X21 = h * F1(t + h / 2.0, W1 + X11 / 2.0, W2 + X12 / 2.0)
        X22 = h * F2(t + h / 2.0, W1 + X11 / 2.0, W2 + X12 / 2.0)
        # STEP 7
        X31 = h * F1(t + h / 2.0, W1 + X21 / 2.0, W2 + X22 / 2.0)
        X32 = h * F2(t + h / 2.0, W1 + X21 / 2.0, W2 + X22 / 2.0)
        # STEP 8
        X41 = h * F1(t + h, W1 + X31, W2 + X32)
        X42 = h * F2(t + h, W1 + X31, W2 + X32)
        # STEP 9
        W1 = W1 + (X11 + 2.0 * X21 + 2.0 * X31 + X41) / 6.0
        W2 = W2 + (X12 + 2.0 * X22 + 2.0 * X32 + X42) / 6.0
        # STEP 10
        t = a + i*h
        # STEP 11
        print('t = ',t, 'w1'+str(i)+'=',W1, 'w2'+str(i)+'=', W2)
        TP.append(t)
        y1.append(W1)
        y2.append(W2)

    plt.plot(TP, y1,'b^', label='Prey')
    plt.plot(TP, y2,'r--', label='Predators')
    plt.legend()
    plt.xlabel('Time')
    plt.ylabel('Population')
    plt.show()

runga_kutta_sys2(0, 4, 2, 40, 1000, 500)

def f(t, y):
    return 1 - y

def y(t):
    return 1 - math.e**(-t)

def problem4(a, b, N, alpha):
    h = (b - a)/N
    t = []
    w = [y(alpha), y(0.01)]

    for i in range(0, N-1):
        t.append(a + (i+2)*h)
        w.append(4*w[i+1] - 3*w[i] - 2*h*f(t[i], w[i]))
        print('t =',t[i], 'w'+str(i+2)+'=',w[i+2])

#problem4(0, 1, 10, 0)
# problem4(0, 1, 100, 0)
