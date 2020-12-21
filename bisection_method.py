#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 20:24:06 2018

@author: joshapanavicius
"""

# Bisection Method
def biSect(a, b, tol, N, fn):
    """Finds a solution to f(x) = 0 given the continuous function f on the
        interval [a, b], where f(a) and f(b) have opposite signs.

    Args:
        a (type): Description of parameter `a`.
        b (type): Description of parameter `b`.
        tol (type): Description of parameter `tol`.
        N (type): Description of parameter `N`.
        fn (type): Description of parameter `fn`.

    Returns:
        type: Description of returned object.

    """
    i = 0
    while i <= N:
        p = a + (b - a)/2

        if fn(p) == 0 or (b - a)/2 < tol:
            # Procedure was successful
            return p

        i += 1
        if fn(a) * fn(p) > 0:
            a = p
        else:
            b = p
    # Procedure was unsuccessful
    print(f"Method failed after {N} iterations.")

a = 0
b = 2
tol = 0.001
N = 20
biSect(a, b, tol, N, lambda x: 1 - x ** 2)
