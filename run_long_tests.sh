#!/bin/bash
python3 rubiks/tests/inductive_sweep.py --agent_type random_walk --start_n 15 --end_n 1 --visual_interval 0 &
python3 rubiks/tests/inductive_sweep.py --agent_type evolutionary --start_n 15 --end_n 1 --visual_interval 0 &
python3 -m rubiks.cli --config rubiks/experiment/configs/random_ea.yaml --trace --visual_interval 0 &
wait
python3 rubiks/tests/analyze_evo.py  # Run analytics after
echo "All tests complete!"