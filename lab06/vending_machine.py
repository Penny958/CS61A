def vending_machine(snacks):
    """Cycles through sequence of snacks.

    >>> vender = vending_machine(('chips', 'chocolate', 'popcorn'))
    >>> vender()
    'chips'
    >>> vender()
    'chocolate'
    >>> vender()
    'popcorn'
    >>> vender()
    'chips'
    >>> other = vending_machine(('brownie',))
    >>> other()
    'brownie'
    >>> vender()
    'chocolate'
    """
    index = -1
    def select_snack():
        nonlocal index
        index = (index + 1) % len(snacks)
        if index >= 0 :
            return snacks[index]
        else:
            return "Snacks is empty"
    return select_snack