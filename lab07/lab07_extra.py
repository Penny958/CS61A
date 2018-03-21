from lab07 import *

# Q6
def cumulative_sum(t):
    """Mutates t where each node's root becomes the sum of all entries in the
    corresponding subtree rooted at t.

    >>> t = Tree(1, [Tree(3, [Tree(5)]), Tree(7)])
    >>> cumulative_sum(t)
    >>> t
    Tree(16, [Tree(8, [Tree(5)]), Tree(7)])
    """
    def sum_subtree(t):
        if t.is_leaf() :
            return t.label
        return sum([t.label] + [sum_subtree(b) for b in t.branches])
    if t.is_leaf() is False:
        t.label = sum_subtree(t)
        t.branches = t.branches
    for b in t.branches: 
        return cumulative_sum(b)
            

# Q7
def reverse_other(t):
    """Reverse the entries of every other level of the tree using mutation.

    >>> t = Tree(1, [Tree(2), Tree(3), Tree(4)])
    >>> reverse_other(t)
    >>> t
    Tree(1, [Tree(4), Tree(3), Tree(2)])
    >>> t = Tree(1, [Tree(2, [Tree(5, [Tree(7), Tree(8)]), Tree(6)]), Tree(3)])
    >>> reverse_other(t)
    >>> t
    Tree(1, [Tree(3, [Tree(5, [Tree(8), Tree(7)]), Tree(6)]), Tree(2)])
    """
    is_odd = False
    def reverse_b(branch):
        num = len(branch)
        for i in range(num//2):
            branch[i].label, branch[num - i - 1].label = branch[num - i - 1].label, branch[i].label
            branch[i].branches, branch[num - i - 1].branches = branch[i].branches, branch[num - i - 1].branches
        return branch
    def reverse_deep(t):
        nonlocal is_odd
        if not is_odd:
            is_odd = True
            t.label = t.label
            t.branches = reverse_b(t.branches)
        else:
            is_odd = False
        for b in t.branches:
            return reverse_deep(b)
    return reverse_deep(t)
# Q8
def deep_map_mut(fn, link):
    """Mutates a deep link by replacing each item found with the
    result of calling fn on the item.  Does NOT create new Links (so
    no use of Link's constructor)

    Does not return the modified Link object.

    >>> link1 = Link(3, Link(Link(4), Link(5, Link(6))))
    >>> deep_map_mut(lambda x: x * x, link1)
    >>> print(link1)
    <9 <16> 25 36>
    """
    if isinstance(link, Link):
        if not isinstance(link.first, Link):
            link.first = fn(link.first)
            link.rest = link.rest
        else:
            deep_map_mut(fn, link.first)

        if link.rest is not Link.empty:
            deep_map_mut(fn, link.rest)

# Q9
def has_cycle(link):
    """Return whether link contains a cycle.

    >>> s = Link(1, Link(2, Link(3)))
    >>> s.rest.rest.rest = s
    >>> has_cycle(s)
    True
    >>> t = Link(1, Link(2, Link(3)))
    >>> has_cycle(t)
    False
    >>> u = Link(2, Link(2, Link(2)))
    >>> has_cycle(u)
    False
    """
    def deep_traversal(rest_link):
        if rest_link is link:
            return True
        elif rest_link.rest is Link.empty:
            return False
        else:
            return deep_traversal(rest_link.rest)
    return deep_traversal(link.rest)

def has_cycle_constant(link):
    """Return whether link contains a cycle.

    >>> s = Link(1, Link(2, Link(3)))
    >>> s.rest.rest.rest = s
    >>> has_cycle_constant(s)
    True
    >>> t = Link(1, Link(2, Link(3)))
    >>> has_cycle_constant(t)
    False
    """
    primitive_link = link
    while link.rest is not Link.empty:
        if link.rest is primitive_link:
            return True
        else:
            link = link.rest
    return False
