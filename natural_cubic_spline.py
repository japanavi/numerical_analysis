import numpy as np

xData1 = [0, 1, 2]
yData1 = [0, 1, 2]

def natural_cubic_spline(n, xData, yData):
    """Short summary.

    Args:
        n (type): Description of parameter `n`.
        xData (type): Description of parameter `xData`.
        yData (type): Description of parameter `yData`.

    Returns:
        type: Description of returned object.

    """
    h = np.array(xData)
    a = np.array(xData)
    for i in range (0, n-1):
        h[i] = xData[i+1] - xData[i]
    for i in range (1, n-1):
        a[i] = (3/h[i])*(a[i+1] - a[i]) - (3/h[i-1])*(a[i] - a[i-1])
    l[0] = 1
    mu[0] = 0
    z[0] = 0
    for i in range (1, n-1):
        l[i] = 2*(xData[i+1] - xData[i-1]) - h[i-1]*mu[i-1]
        mu[i] = h[i]/l[i]
        z[i] = (a[i] - h[i-1]*z[i-1])/l[i]

    l[n] = 1
    z[n] = 0
    c[n] = 0
    k = [1, 2, 3]
    for j in range (n - k[i], 0):
        c[j] = z[j] - mu[j]*c[j+1]
        b[j] = (a[j+1] - a[j])/(h[j]) - h[j]*(c[j+1] + 2*c[j])/(3)
        d[j] = (c[j+1] - c[j])/(3*h[j])


    print(a[0], a[1])
    print(b[0], b[1])
    print(c[0], c[1])
    print(d[0], d[1])

natural_cubic_spline(len(xData1), xData1, yData1)
