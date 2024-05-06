class WrongNumberOfPlayersError(Exception):
    ...


class NoSuchStrategyError(Exception):
    ...


ALLOWED_COMBINATIONS = {
    0: ('RS', 'SP', 'PR', 'RR', 'PP', 'SS'),
    1: ('SR', 'PS', 'RP')
}


def rps_game_winner(players: list) -> str:
    """
    >>> rps_game_winner([['player1', 'P'], ['player2', 'S'], ['player3', 'S']])
    Traceback (most recent call last):
    ...
    WrongNumberOfPlayersError
    >>> rps_game_winner([['player1', 'P'], ['player2', 'A']])
    Traceback (most recent call last):
    ...
    NoSuchStrategyError
    >>> rps_game_winner([['player1', 'P'], ['player2', 'S']])
    'player2 S'
    >>> rps_game_winner([['player1', 'P'], ['player2', 'P']])
    'player1 P'
    """
    if len(players) != 2:
        raise WrongNumberOfPlayersError
    players_dict = {index: value for index, value in enumerate(players)}
    for key, value in ALLOWED_COMBINATIONS.items():
        if players_dict[0][1] + players_dict[1][1] in value:
            return ' '.join(players_dict[key])
    raise NoSuchStrategyError


if __name__ == '__main__':
    import doctest
    doctest.testmod()
