from collections import defaultdict


def combine_anagrams(array: list) -> list:
    """
    >>> combine_anagrams(["cars", "for", "potatoes", "racs", "four", "scar", "creams", "scream"])
    [['cars', 'racs', 'scar'], ['for'], ['potatoes'], ['four'], ['creams', 'scream']]
    """
    anagram_groups = defaultdict(list)
    for word in array:
        anagram_groups[''.join(sorted(word))].append(word)
    return list(anagram_groups.values())


if __name__ == '__main__':
    import doctest
    doctest.testmod()
