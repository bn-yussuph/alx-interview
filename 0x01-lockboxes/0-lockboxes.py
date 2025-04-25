#!/usr/bin/python3
"""
Solution for the lockboxes problem.
"""


def canUnlockAll(boxes) -> bool:
    """
    Determine wether a series of lockboxes can be opened
    based on keys that can be attained.
    """
    if (type(boxes)) is not list:
        return False
    elif (len(boxes)) == 0:
        return False
    
    for i in range(1, len(boxes) - 1):
        key_found = False
        for j in range(len(boxes)):
            key_found = i in boxes[j] and i != j
            if key_found:
                break
        if key_found is False:
            return key_found
    return True
