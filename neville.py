import numpy as np

def f(x):
    return (1 + x**2)**(-1)

def f1():
    return 1 + 10**(1/2)


xData = [i for i in range(-5, 6)]
yData = [f(x) for x in xData]

def nevilles_method(xData, yData, x):
    """Evaluates the interpolating polynomial P on the n + 1 distinct numbers
        x_0, ... , x_n at the number x for the function f.

    Args:
        xData (type): Description of parameter `xData`.
        yData (type): Description of parameter `yData`.
        x (type): Description of parameter `x`.

    Returns:
        Q (array): Description of returned object.

    """
    n = len(xData)
    Q = np.zeros((n,n))  # A representative calculation
    Q[:, 0] = np.array (np.array (yData))

    for i in range (1, n):
        for j in range (1, i):
            Q[i, j]= ((x - xData[i-j])*Q[i, j-1] - (x - xData[i])*Q[i-1, j-1])/(xData[i] - xData[i-j])

    return Q[i, j]

i = 0
while i < 10:
    i +=1
    print('y'+str(i)+' =', nevilles_method(xData, yData, i)*f1())

print('f(1 + (10)^(0.5)) =', f((1 + 10**(1/2))))

xData1 = [8.3, 8.6]
yData1 = [17.56492, 18.50515]
dyData1 = [3.116256, 3.151762]
