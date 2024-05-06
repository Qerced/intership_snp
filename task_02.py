def coincidence(array: list = [], band: range = range(0)) -> list:
    """
    >>> coincidence([1, 2, 3, 4, 5], range(3, 6))
    [3, 4, 5]
    >>> coincidence()
    []
    >>> coincidence([None, 1, 'foo', 4, 2, 2.5], range(1, 4))
    [1, 2, 2.5]
    """
    return [num for num in array if isinstance(num, (int, float))
            and band.start <= num < band.stop]


if __name__ == '__main__':
    import doctest
    doctest.testmod()
