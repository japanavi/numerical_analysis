#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 15:44:58 2018

@author: joshapanavicius
"""


#Method of False Position
def false_position(p0, p1, tol, N, fn):
    """Finds a solution to f(x) = 0 given the continuous function f on the
    interval [p0, p1] where f(p0) and f(p1) have opposite signs.

    Args:
        p0 (type): Description of parameter `p0`.
        p1 (type): Description of parameter `p1`.
        tol (type): Description of parameter `tol`.
        N (type): Description of parameter `N`.
        fn (type): Description of parameter `fn`.

    Returns:
        type: Description of returned object.

    """
    #Start iterations
    i = 2
    q0 = fn(p0)
    q1 = fn(p1)
    while i <= N:
        #Compute pi
        p = p1 - q1*((p1 - p0)/(q1 - q0))
        print('i =', i,'p =', p)
        if abs(p - p1) < tol:
            #Procedure was successful
            return print("After", i, "iterations, a root was found at p =", p)
        i += 1          #Continue iterations
        q = fn(p)       #Update q
        if q * q1 < 0:
            p0 = p1     #Update p0
            q0 = q1     #Update q0

        p1 = p          #Update p1
        q1 = q          #Update q1
    #Procedure was unsuccessful
    return print("The method failed after", N, "iterations.")
