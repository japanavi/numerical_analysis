import math

a = (-1/0.6) + (1/0.6)*math.cos(0.6)


def f(x):
    return math.cos(x)

def g(x):
    return a*x + 1

print(f(0.45))
print(g(0.45))
print(abs(f(0.45) - g(0.45)))

def f1(x):
    return (1/0.54)*(x**2 - 1.5*x + 0.54)

def f2(x):
    return (1/0.18)*(x**2 - 0.9*x)

def f3(x):
    return (1/0.27)*(x**2 - 0.6*x)
    
