#!/usr/bin/python3
"""min operations needed for a copy-paste job"""


def minOperations(n: int) -> int:
    """function returning the minimum algorithm needed
    for a copy-paste job"""
    if n <= 0:
        return 0
    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1
    return operations
