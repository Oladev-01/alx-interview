#!/usr/bin/python3
"""opening boxes"""
from typing import List


def canUnlockAll(boxes: List[List[int]]) -> bool:
    """checking if all boxes can be unlocked"""
    unlocked = [False] * len(boxes)  # starting with all the
    # boxes not yet unlocked
    unlocked[0] = True  # by default, first box. i.e box 0 is iunlocked
    keys = [0]  # we only have the key to box 0, and it is unlocked

    while keys:
        box = keys.pop()  # checking the
        # content of the unlocked box for keys to other boxes
        for key in boxes[box]:  # checking through the unlocked box
            if 0 <= key < len(boxes) and not unlocked[key]:
                # if the box of that key
                # is not yet unlocked, we unlock it
                unlocked[key] = True  # unlocking...
                keys.append(key)  # we add the gotten key to the list of keys
    return all(unlocked)
