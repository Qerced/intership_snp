def max_odd(array: list) -> int:
    """
    >>> max_odd([1, 2, 3, 4, 4])
    3
    >>> max_odd([21.0, 2, 3, 4, 4])
    21
    >>> max_odd(['ololo', 2, 3, 4, [1, 2], None])
    3
    >>> max_odd(['ololo', 'fufufu']) is None
    True
    >>> max_odd([2, 2, 4]) is None
    True
    """
    max_odd = None
    for num in array:
        if isinstance(num, float):
            integer_part, decimal_part = str(num).split('.')
            if int(decimal_part) != 0:
                continue
            num = int(integer_part)
        if isinstance(num, int) and num % 2 != 0:
            max_odd = num if max_odd is None or num > max_odd else max_odd
    return max_odd


if __name__ == '__main__':
    import doctest
    doctest.testmod()
