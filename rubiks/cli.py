"""Tiny CLI wrapper for Experiment runner."""
import argparse, yaml
from rubiks.experiment.runner import Experiment
from rubiks.core.random_util import set_seed

def main():
    p = argparse.ArgumentParser(description='EvoRube – run one experiment')
    p.add_argument('--config', default='rubiks/experiment/configs/random_walk.yaml')
    p.add_argument('--trace', action='store_true', help='log every step to trace.parquet')
    args = p.parse_args()
    cfg = yaml.safe_load(open(args.config))
    if args.trace: cfg['trace'] = True
    set_seed()  # Ensure random scrambles
    Experiment(cfg).run()

if __name__ == '__main__': main()