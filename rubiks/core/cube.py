"""Cube class. Colour-solved is default for EvoRube v-1.0."""
import numpy as np
from .tables import MOVES
FACES=('U','R','F','D','L','B')
_SOLVED=np.repeat(np.arange(6,dtype=np.uint8),9)
class Cube:
    ORIENTATION=FACES
    def __init__(self,arr=None): self.state=_SOLVED.copy() if arr is None else arr
    def copy(self): return Cube(self.state.copy())
    def move(self,tag):
        for cyc in MOVES[tag]: self.state[list(cyc)]=np.roll(self.state[list(cyc)],1)
    def apply(self,seq): [self.move(t) for t in seq.split() if t]
    def is_solved(self,strict=False):
        return np.array_equal(self.state,_SOLVED) if strict else all((self.state[i:i+9]==self.state[i]).all() for i in range(0,54,9))
    def to_bytes(self): return self.state.tobytes()
    @classmethod
    def from_bytes(cls,b): return cls(np.frombuffer(b,dtype=np.uint8).copy())