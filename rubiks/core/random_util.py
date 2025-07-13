import random, numpy as np
def set_seed(seed=None):
    random.seed(seed); np.random.seed(seed if seed is not None else random.randrange(2**32))