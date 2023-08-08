def is_even(n):
    '''
    >>> is_even(2)
    True
    >>> is_even(3)
    False
    '''
    if n % 2 == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    import doctest
    doctest.testmod()