from sympy import *

import numpy as np

x = symbols('x')

"""Root approximation using Newton-Raphson Method"""


def newton(function, initial_guess, max_iter):
    xn = initial_guess

    for n in range(0, max_iter):

        fxn = function.subs(x, xn)

        if abs(fxn) < 10 ** -4:  # find the |f(x)| upto appropriate decimal digits

            print('Found solution after', n, 'iterations.')
            try:
                return xn.evalf(4)
            except AttributeError:
                return xn

        Dfxn = diff(function, x).subs(x, xn)

        if Dfxn == 0:
            print('Zero derivative. No solution found.')

            return None

        xn = xn - fxn / Dfxn

    print('Exceeded maximum iterations. No solution found.')

    return None


"""Root approximation using bisection method"""


def bisection(f, a, b, max_iter):
    if f.subs(x, a) * f.subs(x, b) >= 0:
        print("Bisection method fails.")
        return None

    a_n = a
    b_n = b

    for n in range(1, max_iter + 1):
        m_n = (a_n + b_n) / 2
        f_m_n = f.subs(x, m_n)

        if f.subs(x, a_n) * f_m_n < 0:
            a_n = a_n
            b_n = m_n

        elif f.subs(x, b_n) * f_m_n < 0:
            a_n = m_n
            b_n = b_n

        elif f_m_n == 0:
            print("Found exact solution.")
            return m_n

        else:
            print("Bisection method fails.")

            return None
    print("Found approximate solution after", max_iter, "iteration")
    return ((a_n + b_n) / 2)

        '''Root approximation using secant Method'''

def secant(f,a,b,N):
    if f(a)*f(b) >= 0:
        print("Secant method fails.")
        return None
    a_n = a
    b_n = b
    for n in range(1,N+1):
        m_n = a_n - f(a_n)*(b_n - a_n)/(f(b_n) - f(a_n))
        f_m_n = f(m_n)
        if f(a_n)*f_m_n < 0:
            a_n = a_n
            b_n = m_n
        elif f(b_n)*f_m_n < 0:
            a_n = m_n
            b_n = b_n
        elif f_m_n == 0:
            print("Found exact solution.")
            return m_n
        else:
            print("Secant method fails.")
            return None
    return a_n - f(a_n)*(b_n - a_n)/(f(b_n) - f(a_n))
