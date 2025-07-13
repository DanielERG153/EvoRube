import uuid,time,json,yaml
from ..core.cube import Cube
from ..core.moves import random_scramble
from ..metrics.registry import get_fitness
from ..agents.registry import get_agent
from ..log import write_record,write_trace
from ..view.net_ascii import show_net  # Add at top

class Experiment:
    def __init__(self,cfg):
        self.cfg=cfg; self.trace=cfg.get('trace',False)
        self.fitness=get_fitness(cfg['fitness'])
        self.agent=get_agent(cfg['agent'],cfg)
        self.scramble=cfg['scramble']
        self.budget=cfg['budget']
        self.track='random' if self.scramble=='full' else 'inductive'
    def _base_row(self):
        return {'trial_id':str(uuid.uuid4()),'timestamp':int(time.time()),'track':self.track,
                'scramble_n':-1 if self.scramble=='full' else self.scramble,
                'agent':self.agent.name,'fitness':self.fitness.name,
                'agent_params':json.dumps({k:self.cfg.get(k) for k in ('population_size','generations','mutation_rate','crossover_rate','elitism') if k in self.cfg}),
                'budget':self.budget}
    def run(self):
        cube=Cube(); cube.apply(random_scramble(100 if self.scramble=='full' else self.scramble))
        best=-1; bstate=None; steps=0
        while steps < self.budget:
            done = self.agent.step(cube, self.fitness)
            score = self.fitness.evaluate(cube)
            if steps % 10 == 0:  # Every 10 steps
                print(f"Step {steps}, score {score}:")
                show_net(cube)
            if self.trace: write_trace({**self._base_row(),'step_idx':steps,'score':score,'state':cube.to_bytes()})
            if score>best: best, bstate=score,cube.copy()
            if done: break
            steps +=1
        write_record({**self._base_row(),'steps_used':steps,'solved':cube.is_solved(),'best_score':best,'best_state':bstate.to_bytes()})

    def run(self):
        cube = Cube(); cube.apply(random_scramble(100 if self.scramble == 'full' else self.scramble))
        print("Initial scrambled cube:")
        show_net(cube)  # Visual after scramble
        best = -1; bstate = None; steps = 0
        while steps < self.budget:
            done = self.agent.step(cube, self.fitness)
            score = self.fitness.evaluate(cube)
            print(f"Step {steps}, score {score}:")
            show_net(cube)  # Visual per step (random changes)
            if self.trace: write_trace({**self._base_row(),'step_idx':steps,'score':score,'state':cube.to_bytes()})
            if score > best: best, bstate = score, cube.copy()
            if done: break
            steps +=1
        print("Final cube (approaching solved?):")
        show_net(cube)
        write_record({**self._base_row(),'steps_used':steps,'solved':cube.is_solved(),'best_score':best,'best_state':bstate.to_bytes()})