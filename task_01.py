def is_palindrome(text: str) -> bool:
    """
    >>> is_palindrome("A man, a plan, a canal -- Panama")
    True
    >>> is_palindrome("Madam, I'm Adam!")
    True
    >>> is_palindrome(333)
    True
    >>> is_palindrome(None)
    False
    >>> is_palindrome("Abracadabra")
    False
    """
    clean_text = ''.join(char.lower() for char in str(text) if char.isalnum())
    return clean_text == clean_text[::-1]


if __name__ == '__main__':
    import doctest
    doctest.testmod()
