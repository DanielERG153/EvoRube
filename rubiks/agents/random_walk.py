from .base import Agent
from ..core.moves import random_move
class RandomWalk(Agent):
    name='random_walk'
    def step(self,cube,fitness): cube.move(random_move()); return fitness.evaluate(cube)==486