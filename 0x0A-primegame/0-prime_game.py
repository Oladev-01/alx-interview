#!/usr/bin/python3
"""implementing game theory to determine the winner of a game"""


def sieve_erastosthenes(max_n):
    """sieve out the prime numbers"""
    sieve = [True] * (max_n + 1)
    sieve[0] = sieve[1] = False
    for start in range(2, int(max_n ** 0.5) + 1):
        if sieve[start]:
            for multiple in range(start * start, max_n + 1, start):
                sieve[multiple] = False
    return sieve


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

    max_n = max(nums)
    # get the sieve of prime numbers from the integers
    sieve = sieve_erastosthenes(max_n)
    player_1 = player_2 = 0
    # get the prime for each n
    prime_count = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_count[i] = prime_count[i - 1] + (1 if sieve[i] else 0)

    for n in nums:
        prime_count_for_n = prime_count[n]
        if prime_count_for_n % 2 == 0:
            player_2 += 1
        else:
            player_1 += 1
    if player_1 > player_2:
        return 'Maria'
    elif player_2 > player_1:
        return 'Ben'
    else:
        return None
