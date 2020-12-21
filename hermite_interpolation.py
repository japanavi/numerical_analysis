import numpy as np

xData1 = [8.3, 8.6]
yData1 = [17.56492, 18.50515]
dyData1 = [3.116256, 3.151762]

xData2 = [0.1, 0.2, 0.3, 0.4]
yData2 = [-0.62049958, -0.28398668, 0.00660095, 0.24842440]
dyData2 = [3.58502082, 3.14033271, 2.66668043, 2.16529366]

xData3 = [0.30, 0.32, 0.35]
yData3 = [0.29552, 0.31457, 0.34290]
dyData3 = [0.95534, 0.94924, 0.93937]


def hermite_interpolation(xData, yData, dyData):
    """Short summary.

    Args:
        xData (type): Description of parameter `xData`.
        yData (type): Description of parameter `yData`.
        dyData (type): Description of parameter `dyData`.

    Returns:
        type: Description of returned object.

    """
    n = len(xData)
    Q = np.zeros((2*n+1, 2*n+1))
    z = np.zeros((2*n+1, 2*n+1))
    for i in range (0, n):
        z[2*i] = xData[i]
        z[2*i+1] = xData[i]
        Q[2*i, 0] = yData[i]
        Q[2*i+1, 0] = yData[i]
        Q[2*i+1, 1] = dyData[i]
        if i != 0:
            Q[2*i, 1] = (Q[2*i, 0] - Q[2*i-1, 0])/(z[2*i, 0] - z[2*i-1, 0])
            for i in range (2, 2*n+1):
                for j in range (2, i+1):
                    Q[i,j] = (Q[i, j-1] - Q[i-1, j-1])/(z[i, 0] - z[i-j, 0])
    #For problem a
    print("Q[0, 0] = %.7f" % Q[0,0])
    print("Q[1, 0] = %.7f" % Q[1,0])
    print("Q[2, 0] = %.7f" % Q[2,0])
    print("Q[3, 0] = %.7f" % Q[3,0])
    print("Q[1, 1] = %.7f" % Q[1,1])
    print("Q[2, 1] = %.7f" % Q[2,1])
    print("Q[3, 1] = %.7f" % Q[3,1])
    print("Q[2, 2] = %.7f" % Q[2,2])
    print("Q[3, 2] = %.7f" % Q[3,2])
    print("Q[3, 3] = %.7f" % Q[3,3])

    #For problem d
    #print("Q[0, 0] = %.7f" % Q[0,0])
    #print("Q[1, 1] = %.7f" % Q[1,1])
    #print("Q[2, 2] = %.7f" % Q[2,2])
    #print("Q[3, 3] = %.7f" % Q[3,3])
    #print("Q[4, 4] = %.7f" % Q[4,4])
    #print("Q[5, 5] = %.7f" % Q[5,5])
    #print("Q[6, 6] = %.7f" % Q[6,6])
    #print("Q[7, 7] = %.7f" % Q[7,7])

    #For problem 5a
    #print("Q[0, 0] = %.5f" % Q[0,0])
    #print("Q[1, 1] = %.5f" % Q[1,1])
    #print("Q[2, 2] = %.5f" % Q[2,2])
    #print("Q[3, 3] = %.2f" % Q[3,3])
    #print("Q[4, 4] = %.3f" % Q[4,4])
    #print("Q[5, 5] = %.2f" % Q[5,5])

    #H = Q[0,0] + Q[1,1]*(0.34-0.3) + Q[2,2]*(0.34-0.3)**2 + Q[3,3]*(0.34-0.32)*((0.34-0.3)**2) + \
    #Q[4,4]*((0.34-0.32)**2)*((0.34-0.3)**2) + Q[5,5]*(0.34-0.35)*((0.34-0.32)**2)*((0.34-0.3)**2)
    #print("H = %.5f" % H)
print(hermite_interpolation(xData1, yData1, dyData1))
#print(hermite_interpolation(xData2, yData2, dyData2))
#print(hermite_interpolation(xData3, yData3, dyData3))
