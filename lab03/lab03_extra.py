from lab03 import *

def is_palindrome(n):
    """
    Fill in the blanks '_____' to check if a number
    is a palindrome.

    >>> is_palindrome(12321)
    True
    >>> is_palindrome(42)
    False
    >>> is_palindrome(2015)
    False
    >>> is_palindrome(55)
    True
    """
    x, y = n, 0
    f = lambda: y * 10 + x % 10
    while x > 0:
        x, y = x // 10, f()
    return y == n

def skip_mul(n):
    """Return the product of n * (n - 2) * (n - 4) * ...

    >>> skip_mul(5) # 5 * 3 * 1
    15
    >>> skip_mul(8) # 8 * 6 * 4 * 2
    384
    """
    if n == 2:
        return 2
    elif n == 1:
        return 1
    else:
        return n * skip_mul(n - 2)

def count_up(n):
    """Print out all numbers up to and including n in ascending order.

    >>> count_up(5)
    1
    2
    3
    4
    5
    """
    def counter(i):
        print(i)
        if i == n:
            return
        return counter(i+1)
    counter(1)

def is_prime(n):
    """Returns True if n is a prime number and False otherwise.

    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    # my solution
    steps=0
    def prime_helper(steps,i):
        if steps > 2 :
            return False
        elif i == n:
            return True
        else:
            if n % i == 0:
                steps += 1
            return prime_helper(steps, i+1)
    return prime_helper(steps,1)
    # answers provided
    # def helper(i):
    #     if i > (n ** 0.5):
    #         return True
    #     elif n % i == 0:
    #         return False
    #     else:
    #         return helper(i+1)
    # return helper(2)

def interleaved_sum(n, odd_term, even_term):
    """Compute the sum odd_term(1) + even_term(2) + odd_term(3) + ..., up
    to n.

    >>> # 1 + 2^2 + 3 + 4^2 + 5
    ... interleaved_sum(5, lambda x: x, lambda x: x*x)
    29
    """
    def interleaved_helper(i,tag):
        if i == n:
            if tag == 1:
                return odd_term(n)
            else:
                return even_term(n)
        else:
            if tag == 1:
                return odd_term(i) + interleaved_helper(i+1,0)
            else:
                return even_term(i) + interleaved_helper(i+1,1)
    return interleaved_helper(1,1)
        
def ten_pairs(n):
    """Return the number of ten-pairs within positive integer n.

    >>> ten_pairs(7823952)
    3
    >>> ten_pairs(55055)
    6
    >>> ten_pairs(9641469)
    6
    """
    if n < 10:
        return 0
    else:
        return ten_pairs(n//10) + count_pairs(n//10,10-n%10)

def count_pairs(n,digit):
    if n == 0:
        return 0
    else:
        if n%10 == digit:
            return count_pairs(n//10,digit) + 1
        else:
            return count_pairs(n//10,digit)

