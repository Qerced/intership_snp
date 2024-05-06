from datetime import datetime, timedelta


def date_in_future(day: int | float) -> datetime:
    """
    >>> date_in_future([]) == datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    True
    """
    if not isinstance(day, (int, float)):
        day = 0
    return (datetime.now() + timedelta(days=day)).strftime('%d-%m-%Y %H:%M:%S')


if __name__ == '__main__':
    import doctest
    doctest.testmod()
