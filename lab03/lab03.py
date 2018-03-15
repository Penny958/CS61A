def ab_plus_c(a, b, c):
    """Computes a * b + c.

    >>> ab_plus_c(2, 4, 3)  # 2 * 4 + 3
    11
    >>> ab_plus_c(0, 3, 2)  # 0 * 3 + 2
    2
    >>> ab_plus_c(3, 0, 2)  # 3 * 0 + 2
    2
    """
    if a == 0:
        return c
    else:
        return b + ab_plus_c(a-1,b,c)

def gcd(a, b):
    """Returns the greatest common divisor of a and b.
    Should be implemented using recursion.

    >>> gcd(34, 19)
    1
    >>> gcd(39, 91)
    13
    >>> gcd(20, 30)
    10
    >>> gcd(40, 40)
    40
    """
    smaller = min(a,b)
    larger = max(a,b)
    reminder = larger % smaller
    if reminder == 0:
        return smaller
    else:
        return gcd(smaller,reminder)
    

def hailstone(n):
    """Print out the hailstone sequence starting at n, and return the
    number of elements in the sequence.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    # solution 1
    # def rec(n, step_num):
    #     print(n)
    #     if n == 1:
    #         return step_num
    #     else:
    #         if 0 == n % 2:
    #             n = int(n / 2)
    #         elif 1 == n % 2:
    #             n = int(n * 3 + 1)
    #         step_num += 1
    #         return rec(n,step_num)
    # return rec(n,1)
    # solution 2
    print(n)
    if n ==  1:
        return 1
    elif n % 2 == 0:
        return 1 + hailstone(n//2)
    else:
        return 1 + hailstone(n*3+1)
