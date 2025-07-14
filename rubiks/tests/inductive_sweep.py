import sys
from rubiks.cli import main as cli_main

def run_sweep(agent_type='random_walk', start_n=15, end_n=1, visual_interval=0):
    for n in range(start_n, end_n - 1, -1):  # Countdown from start_n to end_n
        sys.argv = [sys.argv[0], '--config', f'rubiks/experiment/configs/inductive_{agent_type}.yaml', '--visual_interval', str(visual_interval)]
        print(f"Running inductive game with scramble={n}, agent={agent_type}")
        cli_main()

if __name__ == '__main__':
    run_sweep('random_walk', start_n=15, end_n=1)  # Adjust start/end as needed; Or 'evolutionary'