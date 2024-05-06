def connect_dicts(dict1: dict, dict2: dict) -> dict:
    """
    >>> connect_dicts({"a": 2, "b": 12}, {"c": 11, "e": 5})
    {'c': 11, 'b': 12}
    >>> connect_dicts({"a": 13, "b": 9, "d": 11}, {"c": 12, "a": 15})
    {'d': 11, 'c': 12, 'a': 13}
    >>> connect_dicts({"a": 14, "b": 12}, {"c": 11, "a": 15})
    {'c': 11, 'b': 12, 'a': 15}
    """
    priority, updatable = (
        (dict1, dict2) if sum(dict1.values()) > sum(dict2.values())
        else (dict2, dict1)
    )
    updatable.update(priority)
    return {
        k: v for k, v in sorted(
            updatable.items(), key=lambda x: x[1]
        ) if v > 9
    }


if __name__ == '__main__':
    import doctest
    doctest.testmod()
