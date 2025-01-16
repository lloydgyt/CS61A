HW_SOURCE_FILE = __file__

def split(num):
    """ split num to remain digits and last digit

    >>> split(123)
    12
    3
    """
    return num // 10, num % 10

def num_eights(pos):
    """Returns the number of times 8 appears as a digit of pos.

    >>> num_eights(3)
    0
    >>> num_eights(8)
    1
    >>> num_eights(88888888)
    8
    >>> num_eights(2638)
    1
    >>> num_eights(86380)
    2
    >>> num_eights(12345)
    0
    >>> from construct_check import check
    >>> # ban all assignment statements
    >>> check(HW_SOURCE_FILE, 'num_eights',
    ...       ['Assign', 'AnnAssign', 'AugAssign', 'NamedExpr'])
    True
    """
    if pos < 10:
        if pos == 8:
            return 1
        else:
            return 0
    if pos % 10 == 8:
        return num_eights(pos // 10) + 1
    else:
        return num_eights(pos // 10)


def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(8)
    8
    >>> pingpong(10)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    -2
    >>> pingpong(30)
    -2
    >>> pingpong(68)
    0
    >>> pingpong(69)
    -1
    >>> pingpong(80)
    0
    >>> pingpong(81)
    1
    >>> pingpong(82)
    0
    >>> pingpong(100)
    -6
    >>> from construct_check import check
    >>> # ban assignment statements
    >>> check(HW_SOURCE_FILE, 'pingpong',
    ...       ['Assign', 'AnnAssign', 'AugAssign', 'NamedExpr'])
    True
    """
    def switch(i):
        """ decides whether or not to switch direction """
        if i % 8 == 0 or num_eights(i) > 0:
            return True
        else:
            return False
    def ith_element(i):
        if i == 1:
            return 1
        else:
            return ith_element(i - 1) + var(i - 1)
    def var(i):
        """ takes in current index, returns current variation"""
        if i == 1:
            return 1
        else:
            if switch(i):
                return -var(i - 1)
            else:
                return var(i - 1)
    return ith_element(n)


def get_larger_coin(coin):
    """Returns the next larger coin in order.
    >>> get_larger_coin(1)
    5
    >>> get_larger_coin(5)
    10
    >>> get_larger_coin(10)
    25
    >>> get_larger_coin(2) # Other values return None
    """
    if coin == 1:
        return 5
    elif coin == 5:
        return 10
    elif coin == 10:
        return 25


def get_smaller_coin(coin):
    """Returns the next smaller coin in order.
    >>> get_smaller_coin(25)
    10
    >>> get_smaller_coin(10)
    5
    >>> get_smaller_coin(5)
    1
    >>> get_smaller_coin(2) # Other values return None
    """
    if coin == 25:
        return 10
    elif coin == 10:
        return 5
    elif coin == 5:
        return 1


def count_coins(change):
    """Return the number of ways to make change using coins of value of 1, 5, 10, 25.
    >>> count_coins(15)
    6
    >>> count_coins(10)
    4
    >>> count_coins(20)
    9
    >>> count_coins(100) # How many ways to make change for a dollar?
    242
    >>> count_coins(200)
    1463
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'count_coins', ['While', 'For'])
    True
    """
    def use_max_change(change_part, max):
        """ return the number of ways to make change for CHANGE
            and use MAX as the largest coin
        """
        # base case
        if change_part < 0:
            return 0
        if change_part == 0: # Surely we can make change for 0
            return 1
        if max == 1:
            return 1
        smaller_max = get_smaller_coin(max)
        return use_max_change(change_part - max, max) + use_max_change(change_part, smaller_max)
    return use_max_change(change, 25)
