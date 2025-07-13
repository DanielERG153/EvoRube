# rubiks/core/moves.py
import random
from .tables import MOVES
MOVE_TAGS = list(MOVES.keys())
random_move = lambda: random.choice(MOVE_TAGS)

def random_scramble(n):
    seq = []; prev = ''
    for _ in range(n):
        m = random_move()
        while prev and m[0] == prev[0]: m = random_move()
        seq.append(m); prev = m
    print(f"Scramble sequence: {' '.join(seq)}")  # Debug print
    return ' '.join(seq)