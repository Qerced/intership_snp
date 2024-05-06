def multiply_numbers(inputs: any = '') -> int:
    """
    >>> multiply_numbers() is None
    True
    >>> multiply_numbers('ss') is None
    True
    >>> multiply_numbers('1234')
    24
    >>> multiply_numbers('sssdd34')
    12
    >>> multiply_numbers(2.3)
    6
    >>> multiply_numbers([5, 6, 4])
    120
    """
    result = None
    for num in str(inputs):
        if num.isnumeric():
            result = result * int(num) if result is not None else int(num)
    return result


if __name__ == '__main__':
    import doctest
    doctest.testmod()
