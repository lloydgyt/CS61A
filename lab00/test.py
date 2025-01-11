from operator import add, mul
def square(x):
    return mul(x, x)
def sum_squares(x, y):
    def square(x):
        return 1
    return add(square(x), square(y))
result = sum_squares(5, 12)