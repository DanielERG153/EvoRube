import sys
from rubiks.cli import main as cli_main

def run_sweep(agent_type='random_walk', start_n=1, end_n=15):
    for n in range(start_n, end_n + 1):
        sys.argv = [sys.argv[0], '--config', f'rubiks/experiment/configs/inductive_{agent_type}.yaml', '--trace']
        print(f"Running inductive game with scramble={n}, agent={agent_type}")
        cli_main()  # Runs with overridden args

if __name__ == '__main__':
    run_sweep('random_walk')  # Or 'evolutionary'