import random
from typing import NamedTuple
from dataclasses import dataclass
from typing import ClassVar, List

@dataclass
class ChessBoard:
  FILES: ClassVar[List[str]] = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
  RANKS: ClassVar[List[str]] = ['1', '2', '3', '4', '5', '6', '7', '8']

file = random.choice(ChessBoard.FILES)
rank = random.choice(ChessBoard.RANKS)

class Position(NamedTuple):
    file: str
    rank: str


board_size = 8
start = Position(file, rank)

print(f'Start: {start}')

def get_reachables(current_position: Position) -> List[Position]:
    reachables = []

    right_up = Position(chr(ord(current_position.file) + 2), chr(ord(current_position.rank) + 1))
    if right_up.file in ChessBoard.FILES and right_up.rank in ChessBoard.RANKS:
        reachables.append(right_up)

    right_down = Position(chr(ord(current_position.file) + 2), chr(ord(current_position.rank) - 1))
    if right_down.file in ChessBoard.FILES and right_down.rank in ChessBoard.RANKS:
        reachables.append(right_down)

    up_right = Position(chr(ord(current_position.file) + 1), chr(ord(current_position.rank) + 2))
    if up_right.file in ChessBoard.FILES and up_right.rank in ChessBoard.RANKS:
        reachables.append(up_right)

    up_left = Position(chr(ord(current_position.file) - 1), chr(ord(current_position.rank) + 2))
    if up_left.file in ChessBoard.FILES and up_left.rank in ChessBoard.RANKS:
        reachables.append(up_left)

    left_up = Position(chr(ord(current_position.file) - 2), chr(ord(current_position.rank) + 1))
    if left_up.file in ChessBoard.FILES and left_up.rank in ChessBoard.RANKS:
        reachables.append(left_up)

    left_down = Position(chr(ord(current_position.file) - 2), chr(ord(current_position.rank) - 1))
    if left_down.file in ChessBoard.FILES and left_down.rank in ChessBoard.RANKS:
        reachables.append(left_down)

    down_left = Position(chr(ord(current_position.file) - 1), chr(ord(current_position.rank) - 2))
    if down_left.file in ChessBoard.FILES and down_left.rank in ChessBoard.RANKS:
        reachables.append(down_left)

    down_right = Position(chr(ord(current_position.file) + 1), chr(ord(current_position.rank) - 2))
    if down_right.file in ChessBoard.FILES and down_right.rank in ChessBoard.RANKS:
        reachables.append(down_right)

    return reachables

positions_stack = [start]
tour = []

while True:
    if not positions_stack:
        print("No more positions to consider.  Dead end.")
        exit(0)

    if len(tour) == board_size * board_size:
        print(f"Tour completed {tour}")
        exit(0)

    current_position = positions_stack.pop()
    print(f'Current position {current_position}')

    tour.append(current_position)

    next_positions = get_reachables(current_position)
    for position in next_positions:
        if position in tour:
            continue

        positions_stack.append(position)


