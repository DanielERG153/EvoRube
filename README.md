# EvoRube

Minimal evolutionary + inductive-game Rubik’s Cube simulator for exploring latent information in biology analogies.

---

## Installation

1. **Clone the repository**
   `git clone https://github.com/User/project.git`
2. **Create a virtual environment (POSIX)**
   `python3 -m venv .venv`
3. **Activate it**
   POSIX → `source .venv/bin/activate`   Windows → `.venv\Scripts\activate`
4. **Install in editable mode**
   `pip install -e .`

---

## Usage

Run a single experiment from the command line:

```bash
python -m rubiks.cli \
       --config rubiks/experiment/configs/random_walk.yaml \
       --trace \
       --visual_interval 12
```

* `--trace` writes step‑level logs to `data/trace.parquet`.
* `--visual_interval N` renders the cube every *N* steps (`0` = off).
* Pre‑supplied configs: `inductive_random_walk.yaml`, `inductive_ea.yaml`, `random_ea.yaml` (edit for budget, generations, etc.).

Run an **inductive sweep**:

```bash
python rubiks/tests/inductive_sweep.py \
       --agent_type evolutionary \
       --start_n 15 --end_n 1 \
       --visual_interval 0
```

Post‑run analysis:

```bash
python rubiks/tests/analyze_evo.py
```

Generates summary plots as PNG files under `reports/`.

### Long‑form Test Suite

`run_long_tests.sh` executes the three principal sweeps in parallel, waits for completion, then launches analysis automatically (≈ 10 GB disk on full runs):

```bash
#!/usr/bin/env bash
python3 rubiks/tests/inductive_sweep.py --agent_type random_walk   --start_n 15 --end_n 1 --visual_interval 0 &
python3 rubiks/tests/inductive_sweep.py --agent_type evolutionary  --start_n 15 --end_n 1 --visual_interval 0 &
python3 -m rubiks.cli --config rubiks/experiment/configs/random_ea.yaml --trace --visual_interval 0 &
wait
python3 rubiks/tests/analyze_evo.py
echo "All tests complete!"
```

Save, `chmod +x run_long_tests.sh`, then run with `./run_long_tests.sh`.

---

## Dependencies

* `numpy`
* `pyarrow`
* `duckdb`
* `PyYAML` (All installed automatically by `pip install -e .`.)

---

## Project Structure

```
rubiks/
├── core/          # Cube mechanics
├── agents/        # Search heuristics: random‑walk, evolutionary
├── experiment/    # Runner + YAML configs
└── tests/         # Sweeps, analytics
```

---

## Research Motivation

The *inductive game* treats the Rubik’s Cube as an information‑rich landscape in which **latent information** (shortest path ≤ 26 moves) is often inaccessible to naïve search. By progressively increasing a hidden scramble length *N* we quantify how different algorithms bridge the gap between:

* **Latent potential** – states that *could* reach optimality with an as‑yet‑unknown sequence.
* **Functional performance** – states actually reached by the agent under resource limits.

Key questions addressed:

1. At what scramble depth does success probability collapse for an undirected random walk?
2. Do adaptive heuristics (e.g., evolutionary algorithm with cube‑specific operators) push that boundary higher under equal compute budget?
3. How does incorporating feedback about move quality affect retention or recovery of latent potential (analogy: gene networks that remain cryptic yet re‑expressible)?

These experiments provide a quantitative test‑bed for hypotheses about the need for guided search when exploring vast combinatorial spaces.

For a deeper discussion—including biological parallels such as cave‑fish eye re‑emergence—see **BACKGROUND.md**.