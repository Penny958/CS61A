#!python3
# def rational(n,d):
#   return n / d

# def numer(x):
#   integer_x = int(x)
#   decimal_x = x - integer_x
#   decimal_d = decimal_x
#   integer_d = int(decimal_d)
#   digit,denomi = 0,0
#   while decimal_d - integer_d != 0:
#     decimal_d *= 10
#     digit += 1
#     denomi = denomi*10 + 9
#     integer_d = int(decimal_d)
#   return integer_d + integer_x * denomi

# def denom(x):
#   integer_x = int(x)
#   decimal_x = x - integer_x
#   decimal_d = decimal_x
#   integer_d = int(decimal_d)
#   digit,denomi = 0,0
#   while decimal_d - integer_d != 0:
#     decimal_d *= 10
#     digit += 1
#     denomi = denomi*10 + 9 
#     integer_d = int(decimal_d)
#   return denomi

def rational(n,d):
  from fractions import gcd
  g = gcd(n,d)
  return [n//g,d//g]


def numer(x):
  return x[0]


def denom(x):
  return x[1]


def add_rational(x,y):
  nx,dx = numer(x),denom(x)
  ny,dy = numer(y), denom(y)
  return rational(nx * dy + ny * dx, dx * dy)


def mul_rational(x,y):
  return rational(numer(x) * numer(y), denom(x) * denom(y))


def print_rational(x):
  print(numer(x), '/', denom(x))


def rational_are_equal(x,y):
  return numer(x) * denom(y) == numer(y) * denom(x)


def square_rational(x):
  return mul_rational(x,x)


def square_rational_violating_once(x):
  return rational(numer(x) * numer(x), denom(x) * denom(x))


def square_rational_violating_twice(x):
  return [x[0] * x[0], x[1] * x[1]]


def pair(x, y):
  """Return a function that represent a pair"""
  def get(index):
    if index == 0:
      return x
    elif index == 1:
      return y
  return get


def select(p, i):
  """Return the element at index i of pair p"""
  return p(i)


# def count(s,value):
#   total, index = 0, 0
#   while index < len(s):
#     if s[index] == value:
#       total = total + 1
#     index = index + 1
# return total

def count(s, value):
  """Count the number of occurrences of value in sequence s."""
  total = 0
  for elem in s:
      if elem == value:
          total = total + 1
  return total