import uuid,time,json,yaml
from ..core.cube import Cube
from ..core.moves import random_scramble
from ..metrics.registry import get_fitness
from ..agents.registry import get_agent
from ..log import write_record,write_trace
from ..view.net_ascii import show_net  # Add
import multiprocessing as mp  # Add for graph
from ..view.progress_graph import graph_process  # Add this line

class Experiment:
    def __init__(self,cfg):
        self.cfg=cfg; self.trace=cfg.get('trace',False)
        self.visual_interval = cfg.get('visual_interval', 0)
        self.fitness=get_fitness(cfg['fitness'])
        self.agent=get_agent(cfg['agent'],cfg)
        self.scramble=cfg['scramble']
        self.budget=cfg['budget']
        self.track='random' if self.scramble=='full' else 'inductive'
        self.graph_queue = mp.Queue() if self.visual_interval > 0 else None
        if self.graph_queue:
            mp.Process(target=graph_process, args=(self.graph_queue,)).start()
    def _base_row(self):
        return {'trial_id':str(uuid.uuid4()),'timestamp':int(time.time()),'track':self.track,
                'scramble_n':-1 if self.scramble=='full' else self.scramble,
                'agent':self.agent.name,'fitness':self.fitness.name,
                'agent_params':json.dumps({k:self.cfg.get(k) for k in ('population_size','generations','mutation_rate','crossover_rate','elitism') if k in self.cfg}),
                'budget':self.budget}
    def run(self):
        start_time = time.time()
        cube=Cube(); cube.apply(random_scramble(100 if self.scramble=='full' else self.scramble))
        best=-1; bstate=None; steps=0
        plateau_steps = 0
        previous_score = -1
        plateau_threshold = 50
        while steps < self.budget:
            done = self.agent.step(cube, self.fitness)
            score = self.fitness.evaluate(cube)
            if score == previous_score:
                plateau_steps +=1
                if plateau_steps >= plateau_threshold:
                    print(f"Stuck in local optima at step {steps}, score {score}")
                    plateau_steps = 0  # Reset or break if desired
            else:
                plateau_steps = 0
            previous_score = score
            if self.trace: write_trace({**self._base_row(),'step_idx':steps,'score':score,'state':cube.to_bytes()})
            if score > best:
                    best, bstate = score, cube.copy()
                    elapsed = time.time() - start_time
                    print(f"New high score at step {steps}: {score} (elapsed {elapsed:.2f}s)")
                    show_net(cube)
            elif self.visual_interval > 0 and steps % self.visual_interval == 0:
                print(f"Step {steps}, score {score}:")
                show_net(cube)
            if steps % 100 == 0 and self.graph_queue:
                self.graph_queue.put((steps, score))
            if done: break
            steps +=1
        write_record({**self._base_row(),'steps_used':steps,'solved':cube.is_solved(),'best_score':best,'best_state':bstate.to_bytes()})
        if self.visual_interval > 0:  # Show final if visuals enabled
            print("Final end state:")
            show_net(cube)
            if self.graph_queue:
                self.graph_queue.put((steps, score))  # Final update
                self.graph_queue.put(None)  # End graph process