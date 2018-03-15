HW_SOURCE_FILE = 'hw04.py'

###############
#  Questions  #
###############

def intersection(st, ave):
    """Represent an intersection using the Cantor pairing function."""
    return (st+ave)*(st+ave+1)//2 + ave

def street(inter):
    return w(inter) - avenue(inter)

def avenue(inter):
    return inter - (w(inter) ** 2 + w(inter)) // 2

w = lambda z: int(((8*z+1)**0.5-1)/2)

def taxicab(a, b):
    """Return the taxicab distance between two intersections.

    >>> times_square = intersection(46, 7)
    >>> ess_a_bagel = intersection(51, 3)
    >>> taxicab(times_square, ess_a_bagel)
    9
    >>> taxicab(ess_a_bagel, times_square)
    9
    """
    return abs(street(a)-street(b)) + abs(avenue(a) - avenue(b))

def squares(s):
    """Returns a new list containing square roots of the elements of the
    original list that are perfect squares.

    >>> seq = [8, 49, 8, 9, 2, 1, 100, 102]
    >>> squares(seq)
    [7, 3, 1, 10]
    >>> seq = [500, 30]
    >>> squares(seq)
    []
    """
    square_roots = []
    length = len(s)
    num_roots = 0
    from math import sqrt
    for i in range(0, length):
        root = sqrt(s[i])
        decimal = root - int(root)
        if decimal == 0.0:
            square_roots.append(int(root))
            num_roots += 1
    return square_roots

def g(n):
    """Return the value of G(n), computed recursively.

    >>> g(1)
    1
    >>> g(2)
    2
    >>> g(3)
    3
    >>> g(4)
    10
    >>> g(5)
    22
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'g', ['While', 'For'])
    True
    """
    total = n
    def G(n):
        if n <= 3:
            return n
        else :
            return G(n-1) + 2 * G(n-2) + 3 * G(n-3)
    return G(n)

def g_iter(n):
    """Return the value of G(n), computed iteratively.

    >>> g_iter(1)
    1
    >>> g_iter(2)
    2
    >>> g_iter(3)
    3
    >>> g_iter(4)
    10
    >>> g_iter(5)
    22
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'g_iter', ['Recursion'])
    True
    """
    def G(n) :
        mul_n1 = 1
        mul_n2 = 2
        mul_n3 = 3
        result = 0
        if n <= 3:
            result = n
        else:
            # my answer
            while n > 4:
                mul_n1,mul_n2,mul_n3 = mul_n1 * 1 + mul_n2,mul_n1 * 2 + mul_n3,mul_n1 * 3
                n -= 1
            # result = mul_n1 * G(3) + mul_n2 * G(2) + mul_n3 * G(1)
            result = mul_n1 * 3 + mul_n2 * 2 + mul_n3 * 1
            # answer provided
            # while n > 3:
            #     mul_n1,mul_n2,mul_n3 = mul_n2,mul_n3,mul_n3 + 2 * mul_n2 + 3 * mul_n1
            #     n = n - 1 
            # result = mul_n3
        return result
    return G(n)

def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(7)
    7
    >>> pingpong(8)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    0
    >>> pingpong(30)
    6
    >>> pingpong(68)
    2
    >>> pingpong(69)
    1
    >>> pingpong(70)
    0
    >>> pingpong(71)
    1
    >>> pingpong(72)
    0
    >>> pingpong(100)
    2
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'pingpong', ['Assign', 'AugAssign'])
    True
    """
    # answer
    # def pingpong_next(k, p, up):
    #     if k == n:
    #         return p
    #     if up:
    #         return pingpong_switch(k+1, p+1, up)
    #     else:
    #         return pingpong_switch(k+1, p-1, up)

    # def pingpong_switch(k, p, up):
    #     if has_seven(k) or k % 7 == 0:
    #         return pingpong_next(k, p, not up)
    #     else:
    #         return pingpong_next(k, p, up)

    # return pingpong_next(1,1,True)
    # my solution
    def pingpong1(t, num, dire):
        if not t:
            return num
        if dire:
            if has_seven(n-(t-1)) or not (n-(t-1)) % 7:
                return pingpong1(t-1, num+1, 1-dire)
            else:
                return pingpong1(t-1, num+1, dire)
        else:
            if has_seven(n-(t-1)) or not (n-(t-1)) % 7:
                return pingpong1(t-1, num-1, 1-dire)
            else:
                return pingpong1(t-1, num-1, dire)
    return pingpong1(n-1, 1, 1)

def has_seven(k):
    """Returns True if at least one of the digits of k is a 7, False otherwise.

    >>> has_seven(3)
    False
    >>> has_seven(7)
    True
    >>> has_seven(2734)
    True
    >>> has_seven(2634)
    False
    >>> has_seven(734)
    True
    >>> has_seven(7777)
    True
    """
    if k % 10 == 7:
        return True
    elif k < 10:
        return False
    else:
        return has_seven(k // 10)

def count_change(amount):
    """Return the number of ways to make change for amount.

    >>> count_change(7)
    6
    >>> count_change(10)
    14
    >>> count_change(20)
    60
    >>> count_change(100)
    9828
    """
    def count_change_part(n, m):
        if n == 0:
            return 1
        elif n < 0:
            return 0
        elif m == 0:
            return 1
        else:
            return count_change_part(n - 2**m, m) + count_change_part(n, m-1)
    def get_max_exponent(n):
        from math import sqrt
        return int(sqrt(n))
    return count_change_part(amount, get_max_exponent(amount))
###################
# Extra Questions #
###################

from operator import sub, mul

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'make_anonymous_factorial', ['Assign', 'AugAssign', 'FunctionDef', 'Recursion'])
    True
    """
    # return lambda n: 1 if not n else mul(n, make_anonymous_factorial()(n-1)) 
    return (lambda f:lambda k:f(f,k))(lambda f, k: k if k == 1 else mul(k, f(f, sub(k, 1)))) 