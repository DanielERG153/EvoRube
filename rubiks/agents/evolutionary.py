from .base import Agent
from dataclasses import dataclass
from ..core.moves import random_move
import numpy as np
import random

@dataclass(slots=True)
class EAParams:
    population_size: int = 100
    generations: int = 50
    mutation_rate: float = 0.15
    crossover_rate: float = 0.70
    elitism: float = 0.05

class EvolutionaryAgent(Agent):
    name = "evolutionary"
    def __init__(self, params: EAParams, genome_len=20):
        self.params = params
        self.genome_len = genome_len

    def _random_genome(self):
        return [random_move() for _ in range(self.genome_len)]

    def step(self, cube, fitness):
        pop = [self._random_genome() for _ in range(self.params.population_size)]
        for gen in range(self.params.generations):
            scores = [self._score_genome(g, cube, fitness) for g in pop]
            if max(scores) == 486:
                return True
            pop = self._next_generation(pop, scores)
        # Apply best to cube (fixes no change)
        best_genome = pop[np.argmax(scores)]
        for mv in best_genome:
            cube.move(mv)
        return False

    def _score_genome(self, genome, cube, fitness):
        tmp = cube.copy()
        for mv in genome:
            tmp.move(mv)
        return fitness.evaluate(tmp)

    def _next_generation(self, pop, scores):
        new_pop = []
        elite_n = int(self.params.elitism * self.params.population_size)
        elite_idx = np.argsort(scores)[-elite_n:]
        for i in elite_idx:
            new_pop.append(pop[i])
        while len(new_pop) < self.params.population_size:
            parent1 = random.choices(pop, weights=scores)[0]
            parent2 = random.choices(pop, weights=scores)[0]
            child = parent1.copy()
            if random.random() < self.params.crossover_rate:
                cx = random.randrange(self.genome_len)
                child[cx:] = parent2[cx:]
            child = [mv if random.random() > self.params.mutation_rate else random_move() for mv in child]
            new_pop.append(child)
        return new_pop