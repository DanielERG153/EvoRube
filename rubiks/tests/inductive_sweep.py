import sys
from rubiks.cli import main as cli_main

def run_sweep(agent_type='random_walk', start_n=1, end_n=20, visual_interval=0):
    for n in range(start_n, end_n + 1):
        sys.argv = [sys.argv[0], '--config', f'rubiks/experiment/configs/inductive_{agent_type}.yaml', '--visual_interval', str(visual_interval)]
        print(f"Running inductive game with scramble={n}, agent={agent_type}")
        cli_main()

if __name__ == '__main__':
    run_sweep('random_walk', end_n=15)  # Or 'evolutionary', adjust end_n