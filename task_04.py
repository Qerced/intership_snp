def sort_list(array: list) -> list:
    """
    >>> sort_list([])
    []
    >>> sort_list([2, 4, 6, 8])
    [8, 4, 6, 2, 2]
    >>> sort_list([1])
    [1, 1]
    >>> sort_list([1, 2, 1, 3])
    [3, 2, 3, 1, 1]
    """
    if not array or not isinstance(array, list):
        return []
    max_num = max(array)
    min_num = min(array)
    for i in range(len(array)):
        if array[i] == max_num:
            array[i] = min_num
        elif array[i] == min_num:
            array[i] = max_num
    array.append(min_num)
    return array


if __name__ == '__main__':
    import doctest
    doctest.testmod()
