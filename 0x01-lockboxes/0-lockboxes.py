#!/usr/bin/python3
'''LockBoxes'''

def canUnlockAll(boxes):
    '''Determines if all the boxes can be opened or not
    Returns:
        True: all boxes can be opened
        False: if not all boxes can be opened
    '''
    length = len(boxes)
    keys = set()
    opened_boxes = []
    y = 0

    while y < length:
        oldi = y
        opened_boxes.append(y)
        keys.update(boxes[y])
        for key in keys:
            if key != 0 and key < length and key not in opened_boxes:
                y = key
                break
        if oldi != y:
            continue
        else:
            break

    for y in range(length):
        if y not in opened_boxes and y != 0:
            return False
    return True
