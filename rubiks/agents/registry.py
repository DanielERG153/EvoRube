from .random_walk import RandomWalk
from .evolutionary import EvolutionaryAgent, EAParams
_REG={'random_walk':lambda cfg:RandomWalk(),
      'evolutionary':lambda cfg: EvolutionaryAgent(EAParams(**cfg.get('params', {})), cfg.get('genome_len', 20))}
get_agent=lambda n,cfg={}:_REG[n](cfg)