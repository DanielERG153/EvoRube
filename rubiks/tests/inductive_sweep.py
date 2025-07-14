import sys, argparse, os
from rubiks.cli import main as cli_main

def run_sweep(agent_type='random_walk', start_n=15, end_n=1, visual_interval=0):
    config_suffix = 'ea' if agent_type == 'evolutionary' else agent_type
    config_path = f'rubiks/experiment/configs/inductive_{config_suffix}.yaml'
    if not os.path.exists(config_path):
        print(f"Config {config_path} not found - skipping {agent_type}")
        return
    for n in range(start_n, end_n - 1, -1):  # High to low
        sys.argv = [sys.argv[0], '--config', config_path, '--visual_interval', str(visual_interval)]
        print(f"Running inductive game with scramble={n}, agent={agent_type}")
        cli_main()

if __name__ == '__main__':
    p = argparse.ArgumentParser(description='Inductive sweep')
    p.add_argument('--agent_type', default='random_walk', choices=['random_walk', 'evolutionary'])
    p.add_argument('--start_n', type=int, default=15)
    p.add_argument('--end_n', type=int, default=1)
    p.add_argument('--visual_interval', type=int, default=0)
    args = p.parse_args()
    run_sweep(args.agent_type, args.start_n, args.end_n, args.visual_interval)