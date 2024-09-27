# Implementing a bi-section method function in python!
import matplotlib.pyplot as plt

def bisection_method(func: str, a, b, error_accept):
    """
    This function solves for an unknown root of a non-linear function given the
    function, the initial root boundaries, and an acceptable level of error.

    Parameters:
    - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    :param func: The user defined function, which is entered as a string.
    :param a: The initial lower root boundary.
    :param b: The initial upper root boundary
    :param error_accept: The user'sacceptable level of error

    Returns:
    - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    :return: The root boundaries and the error at the final iteration.
    """
    # defining functions
    def f(x):
        f = eval(func)
        return f

    error = abs(b - a)

    # while loop to match error acceptance
    while error > error_accept:
        c = (b + a) / 2

        if f(a) * f(b) >= 0:
            print("No root for multiple roots present!")
            quit()

        elif f(c) * f(a) < 0:
            b = c
            error = abs(b - a)

        elif f(c) * f(b) < 0:
            a = c
            error = abs(b - a)

        else:
            print("Error!")
            quit()

    print(f"The error is {error}")
    print(f"The lower boundary, a, is {a} and the upper boundary, b, is {b}")
