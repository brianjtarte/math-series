def fibonacci(n):
    """
        This function will return the fibonacci sequence at the nth position when run
    """
    if n < 0:
        print("ERROR!")

    elif n == 0:
        return 0

    elif n == 1 or n == 2:
        return 1

    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def lucas(n):
    """
        This function will return the lucas sequence at the nth position when run
    """
    if n < 0:
        return "ERROR!"

    elif n == 0:
        return 2

    elif n == 1:
        return 1

    else:
        return lucas(n - 1) + lucas(n - 2)

def sum_series(n,a=0,b=1):
    """
    This function will return the fibonacci sequence at the nth position when the optional parameters are NOT called,
    and return the lucas sequence at the nth position when optional parameters 2 and 1 are used.
    """
    if n < 0:
        return "ERROR!"

    elif n == 0:
        return a

    elif n == 1:
        return b

    else:
        return sum_series(n - 1, a, b) + sum_series(n - 2, a, b)
