import pandas as pd
import numpy as np


n = 8

board = pd.DataFrame(0, index=range(n), columns=range(n))

print(board)

positions = []
dead_ends = []

def find_empty_square():
    return board.where(board==0).stack().index[0]

def dead_end(square):
    new = positions + [square]
    print(new)

    if new in dead_ends:
        return True

    return False


def place_piece(square):
    global board

    board.loc[square[0], :] = 1
    board.loc[:, square[1]] = 1

    mask = np.eye(board.shape[0], board.shape[1], k=square[1], dtype=bool)
    board = board.where(~mask, 1)
    mask = np.fliplr(mask)
    board = board.where(~mask, 1)
    print(board)


while True:
    if len(positions) == n:
        print(f'Done {positions}.')
        exit(0)

    square = find_empty_square()

    print(square)

    if not square:
        print(f'Hit dead end')
        dead_ends.append(positions)
        positions = positions[:-1]

    if dead_end(square):
        print(f'Dead end {square} {dead_ends}')
        continue

    place_piece(square)

    positions.append(square)

