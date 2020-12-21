#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 21:59:55 2018

@author: joshapanavicius
"""

def f1(x):
    return x**3 - 2*x**2 -5

def f3(x):
    return x**4 + x**3 + 3*x**2 + 2*x + 2

def f7(x):
    return 600*x**4 - 550*x**3 + 200*x**2 - 20*x - 1

#Muller's Method
def muller_method(p0, p1, p2, tol, N, fn):
    """Short summary.

    Args:
        p0 (type): Description of parameter `p0`.
        p1 (type): Description of parameter `p1`.
        p2 (type): Description of parameter `p2`.
        tol (type): Description of parameter `tol`.
        N (type): Description of parameter `N`.
        fn (type): Description of parameter `fn`.

    Returns:
        type: Description of returned object.

    """
    h1 = p1 - p0
    h2 = p2 - p1
    s1 = (fn(p1) - fn(p0))/h1
    s2 = (fn(p2) - fn(p1))/h2
    d = (s1 - s2)/(h2 + h1)
    i = 3
    while i <= N:
        b = s2 + h2*d
        D = (b**(2) - 4*fn(p2)*d)**0.5
        if abs(b - D) < abs(b + D):
            E = b + D
        else:
            E = b - D
        h = -2*fn(p2)/E
        p = p2 + h
        print('i =', i, 'p =', p)
        if abs(h) < tol:
            return print('After', i, 'iterations, we found a root at p =', p)
        p1 = p2
        p2 = p
        h1 = p1 - p0
        h2 = p2 - p1
        s1 = (fn(p1) - fn(p0))/h1
        s2 = (fn(p2) - fn(p1))/h2
        d = (s1 - s2)/(h2 + h1)
        i += 1
    return print('After', N, 'iterations.')

#Newton's Method
def newtonMethod(p0, tol, N, fn, dfn):
    """Finds a solution to f(x) = 0 given an initial approximation p0.

    Number, Number, Number, Function, Function -> Number"""
    #Start iterations
    i = 1
    while i <= N:
        #Compute pi
        p = p0 - (fn(p0)/dfn(p0))
        print('i =', i, 'p =', p)
        if abs(p - p0) < tol:
            #Procedure was successful
            return print("After", i, "iterations, a root was found at p =", p)
        i += 1  #Continue iterations
        p0 = p  #Updates p0
    #Procedure was unsuccessful
    return print("The method failed after", N, "iterations.")

muller_method(-0.5, 0, 0.5, 0.00001, 20, f7)
