import numpy as np
import matplotlib.pyplot as plt


"""Rienmann Sum"""


def lowersum(f, a, b, n):
    x = symbols('x')
    area = 0
    h = (b - a) / n
    t = a
    for i in range(n):
        l = min(f.subs(x, t), f.subs(x, t + h))
        area += l * h
        t = t + h
    return area


def uppersum(f, a, b, n):
    x = symbols('x')
    area = 0
    h = (b - a) / n
    t = a
    for i in range(n):
        l = max(f.subs(x, t), f.subs(x, t + h))
        area += l * h
        t = t + h
    return area


def Rienmannsum(f, a, b):
    e = 1
    n = int(input("Initial number of divisions you want: "))
    while e > 10 ** -4:
        L = lowersum(f, a, b, n)
        U = uppersum(f, a, b, n)
        e = U - L
        n *= 10
    return (U + L) / 2


'''Simpsons Method of numerical integration'''


def simps(f,a,b,N=50):
    '''
    f : function
        Vectorized function of a single variable
    a , b : numbers
        Interval of integration [a,b]
    N : (even) integer
        Number of subintervals of [a,b]
    '''
    if N % 2 == 1:
        raise ValueError("N must be an even integer.")
    dx = (b-a)/N
    x = np.linspace(a,b,N+1)
    y = f(x)
    S = dx/3 * np.sum(y[0:-1:2] + 4*y[1::2] + y[2::2])
    return S

'''Trapezoid Rule for numerical integration'''

def trapz(f,a,b,N=50):
    '''
    f : function
        Vectorized function of a single variable
    a , b : numbers
        Interval of integration [a,b]
    N : integer
        Number of subintervals of [a,b]
    '''
    x = np.linspace(a,b,N+1)
    y = f(x)
    y_right = y[1:] # Right endpoints
    y_left = y[:-1] # Left endpoints
    dx = (b - a)/N
    T = (dx/2) * np.sum(y_right + y_left)
    return T





