#!/usr/bin/python3
"""implementing game theory to determine the winner of a game"""


def isWinner(x: int, nums: list) -> str:
    """this function determines the winner of the most of the rounds x
        from the game of array nums. The array consist of integers
        at index i for each rounds,
        ranging from 1 to the nums[i], the players are Maria and Ben
        and Maria is said to always go first."""

    # i am checking the condition where the game should have no
    # winner based on the setting of the game
    if x == 0 or not nums or x != len(nums):
        return None

    player_1 = {'name': 'Maria', 'move': True}
    player_2 = {"name": 'Ben', "move": True}
    prime = [2, 3, 5, 7, 11, 13]
    winner = []
    for rounds in range(x):
        if nums[rounds] == 1:
            winner.append(player_2['name'])
        else:
            board = list(range(1, nums[rounds] + 1))
            for_prime = 0
            turn = True
            while turn:
                smallest_prime = prime[for_prime]
                if player_1['move']:
                    for index, get_prime in enumerate(board):
                        if board and get_prime % smallest_prime == 0:
                            board.pop(index)
                    if not board or not any(i in board for i in prime):
                        winner.append(player_1['name'])
                        turn = False
                    else:
                        player_1['move'] = False
                        player_2['move'] = True
                else:
                    for idx, get_prime in enumerate(board):
                        if board and get_prime % smallest_prime == 0:
                            board.pop(idx)
                    if not board or not any(i in board for i in prime):
                        winner.append(player_2['name'])
                        turn = False
                    else:
                        player_2['move'] = False
                        player_1['move'] = True
                for_prime += 1
    if winner:
        if winner.count('Maria') == winner.count('Ben'):
            return None
        return 'Maria' if winner.count('Maria') > winner.count('Ben') else 'Ben'  # noqa
    return None
