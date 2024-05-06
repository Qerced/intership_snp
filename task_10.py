import re
from collections import defaultdict


def count_words(text: str) -> dict:
    """
    >>> count_words("A man, a plan, a canal -- Panama")
    defaultdict(<class 'int'>, {'a': 3, 'man': 1, 'plan': 1, 'canal': 1, 'panama': 1})
    >>> count_words("Doo bee doo bee doo")
    defaultdict(<class 'int'>, {'doo': 3, 'bee': 2})
    """
    result = defaultdict(int)
    for word in re.findall(r'\b\w+\b', text):
        result[word.lower()] += 1
    return result


if __name__ == '__main__':
    import doctest
    doctest.testmod()
