
#Modified Newton's Method
def mod_newtonMethod(p0, tol, N, fn, dfn, ddfn):
    """Finds a solution to f(x) = 0 given an initial approximation p0.

    Args:
        p0 (type): Description of parameter `p0`.
        tol (type): Description of parameter `tol`.
        N (type): Description of parameter `N`.
        fn (type): Description of parameter `fn`.
        dfn (type): Description of parameter `dfn`.
        ddfn (type): Description of parameter `ddfn`.

    Returns:
        type: Description of returned object.

    """
    #Start iterations
    i = 1
    while i <= N:
        #Compute pi
        p = p0 - (fn(p0) * dfn(p0))/((dfn(p0))**2 - fn(p0) * ddfn(p0))
        print('i =', i, 'p =', p)
        if abs(p - p0) < tol:
            #Procedure was successful
            return print("After", i, "iterations, a root was found at p =", p)
        i += 1  #Continue iterations
        p0 = p  #Update p0
    #Procedure was unsuccessful
    return print("The method failed after", N, "iterations.")
