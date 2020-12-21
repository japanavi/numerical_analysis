
import numpy

xData1 = [8.3, 8.6]
yData1 = [17.56492, 18.50515]
dyData1 = [3.116256, 3.151762]

# input is list of tuples [(x1,y1),(x2,y2),...,(xn,yn)] xi are Chebyshev nodes
def hermit_interpolate(input):
    """Short summary.

    Args:
        input (type): Description of parameter `input`.

    Returns:
        type: Description of returned object.

    """
    n = len(input)
    points = numpy.zeros(shape=(2 * n + 1, 2 * n + 1))
    X, Y = zip(*input)
    X = list(X)
    Y = list(Y)

    for i in range(0, 2 * n, 2):
        points[i][0] = X[i / 2]
        points[i + 1][0] = X[i / 2]
        points[i][1] = Y[i / 2]
        points[i + 1][1] = Y[i / 2]

        for i in range(2, 2 * n + 1):
            for j in range(1 + (i - 2), 2 * n):
                if i == 2 and j % 2 == 1:
                    points[j][i] = calculate_f_p_x(X[j / 2]);

                else:
                    points[j][i] = (points[j][i - 1] - points[j - 1][i - 1]) / (points[j][0] - points[(j - 1) - (i - 2)][0])


# here is function to calculate value for given x
def result_polynomial(xpoint):  
    """Short summary.

    Args:
        xpoint (type): Description of parameter `xpoint`.

    Returns:
        type: Description of returned object.

    """
    val = 0
    for i in range(0, 2 * n):
        factor = 1.
        j = 0
        while j < i:
            factor *= (xpoint - X[j / 2])
            if j + 1 != i:
                factor *= (xpoint - X[j / 2])
                j += 1
            j += 1
        val += factor * points[i][i + 1]
    return val

hermit_interpolate([(8.3, 17.56492), (8.6, 18.50515)])
