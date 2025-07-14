# rubiks/tests/test_random_scramble.py
import random
from rubiks.core.cube import Cube

g = list('URFDLB') + [f"{f}'" for f in 'URFDLB'] + [f"{f}2" for f in 'URFDLB']
for _ in range(1000):
    c = Cube()
    seq = random.choices(g, k=25)
    for m in seq: c.move(m)
    for m in reversed(seq):  # apply exact inverse sequence
        c.move(m.replace("'", '') if "'" in m else (m if '2' in m else m+"'")) 
    assert c.is_solved()
print("Random scrambling test passed!")  # Optional, to confirm completion