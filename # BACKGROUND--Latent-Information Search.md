# BACKGROUND — Latent-Information Search Using EvoRube  
*(Companion document to the August 2025 lecture "Latent Information and the Inductive Game", SCHEMA_VERSION = 1)*

---

## 1 Motivation

Biological systems often retain **latent design information**—structural or regulatory capacity that is not expressed under present conditions but can be re-activated (e.g., cave-fish eye regrowth, antibiotic re-sensitisation).  
Standard evolutionary simulations rarely model the **inter-dimensional dependencies** that make recovering such capacity difficult.

EvoRube provides a fully mapped, discrete test-bed to measure how different algorithms bridge the gap between:

* **Latent potential** — theoretically reachable optimal states.  
* **Functional performance** — states actually reached under limited search budgets.

---

## 2 Why a Rubik’s Cube?

| Engineering criterion | Cube property | Biological analogue |
|-----------------------|--------------|---------------------|
| High-order dependencies | One quarter-turn moves 8–12 stickers; constraints couple three axes. | Pleiotropic mutations; allosteric enzyme shifts. |
| Quantifiable distance  | Optimal distance ≤ 26 half-turn moves (“God’s algorithm”). | Minimum mutation path to full function. |
| Fractional functionality | “Colour-solved” metric gives graded progress (0 – 54 stickers). | Partial enzyme activity; hypomorphic gene variants. |
| Controlled search space | 4.3 × 10¹⁹ states; 18 exact moves form an 18-regular graph. | Epistatic fitness landscapes. |
| Repeatability | Scramble length *N* and RNG seed fully reproduced. | Clonal selection lines; directed-evolution repeats. |

The cube captures **inter-dimensional dependencies** overlooked in many evolutionary models: a single move can simultaneously repair one constraint and break another, mirroring real genetic trade-offs.

---

## 3 Key Definitions

| Term | Operational definition in EvoRube |
|------|-----------------------------------|
| **Latent information** | Number of cube states ≤ 26 moves from solved **but not known** to the algorithm. |
| **Functional information** | Fitness score returned by a metric (default: Σ count² of matching colours per face). |
| **L/F gap** | log₂(states within *N*) ⁄ functional bits discovered during a run. |
| **Inductive game** | Start solved → apply *N* hidden moves → solver knows *N* but not the sequence. |

---

## 4 Experimental Framework

| Track | Initial state | Primary question |
|-------|---------------|------------------|
| **Inductive** | Solved → scramble *N* (1 – 15) | At what *N* does random search fail? How far can EA push the boundary? |
| **Random-cube** | Full random (≈ 100 moves) | How close can EA get to colour-solved within a fixed budget? |

### 4.1 Agents
* **Random-walk** — undirected baseline.  
* **Evolutionary-EA** — population, crossover, mutation; parameters in YAML.  
* Future: **Topology-EA** — macros/slice moves to reshape search space.

### 4.2 Fitness
Default: **face_colour_sqsum**  
\( \mathrm{score} = \sum_{f=1}^{6} (\text{matching stickers}_f)^2 \)

---

## 5 Data & Reproducibility

* **`data/runs.parquet`** — one row per trial (schema in `rubiks/schema.py`).  
* Optional **`data/trace.parquet`** — step-level rows when `--trace` set.  
* All RNG seeds recorded in `agent_params` JSON.

Query example:

```sql
SELECT scramble_n,
       avg(solved::INT) AS success_rate
FROM 'data/runs.parquet'
GROUP BY 1;
````

---

## 6 Interpretation Guidelines

1. **Random-search collapse** — success drops sharply near *N* ≈ 7–8.
2. **EA improvement** — any shift of the collapse point by ≥ 2 moves indicates the algorithm is leveraging latent information, not mere sampling variance.
3. **Topology edits** — adding macros that preserve sub-assemblies tests the hypothesis that biological systems encode “look-ahead logic” (design teleology).

---

## 7 Reference Reading

| Topic                           | Citation & open link                                                                                                                                                                                  |
| ------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Functional information metric   | Hazen et al., *PNAS* 2007 — [https://www.pnas.org/doi/10.1073/pnas.0701744104](https://www.pnas.org/doi/10.1073/pnas.0701744104)                                                                      |
| Adaptive loss & latent capacity | Behe, *Darwin Devolves* (2019) — [https://amzn.to/3xF9E4P](https://amzn.to/3xF9E4P)                                                                                                                   |
| Optimal cube paths              | Korf 1997 pattern-database paper — [https://www.cs.princeton.edu/courses/archive/fall06/cos402/papers/korfrubik.pdf](https://www.cs.princeton.edu/courses/archive/fall06/cos402/papers/korfrubik.pdf) |
| Cave-fish optic program         | Yoshizawa & Jeffery, *Curr. Biol.* 2011 — [https://doi.org/10.1016/j.cub.2011.04.008](https://doi.org/10.1016/j.cub.2011.04.008)                                                                      |
| LTEE citrate discussion         | Van Hofwegen, Hovde & Minnich, *J. Bacteriol.* 2016 — [https://journals.asm.org/doi/10.1128/jb.00831-15](https://journals.asm.org/doi/10.1128/jb.00831-15)                                            |

---

## 8 Simple Summary

> **EvoRube quantifies how much algorithmic “look-ahead” is required to rescue latent design information in a high-dependency search space—providing a concrete, engineering-level analogue for deepening understanding of guidance vs. randomness in the information processing of biological life.**