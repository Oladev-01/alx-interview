#!/usr/bin/python3
"""opening boxes"""


def canUnlockAll(boxes):
    n = len(boxes)
    opened = [False] * n
    opened[0] = True
    stack = [0]

    while stack:
        current_box = stack.pop()

        for key in boxes[current_box]:
            if 0 <= key < n and not opened[key]:
                opened[key] = True
                stack.append(key)

    return all(opened)
