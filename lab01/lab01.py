def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    result = 1
    while k > 0:
        result = result * n
        n = n - 1
        k = k - 1
    return result


def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    result = 0
    while y:
        print("DEBUG: y % 10 = ", y % 10)
        result += y % 10
        print("DEBUG: result = ", result)
        y //= 10
        print("DEBUG: y = ", y)
    return result

def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    last = False
    debug_counter = 1;
    while n > 0:
        if n % 10 == 8:
            if last == True:
                return True
            else:
                last = True
        else:
            last = False
        debug_counter += 1
        print("DEBUG: last = ", last, ",dc = ", debug_counter)
        n //= 10 # n goes towards 0
    return False