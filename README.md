# Blood-Brain Barrier Permeability Prediction

A comparative machine-learning study of blood-brain barrier permeability using molecular fingerprints and graph representations. The project evaluates rule-based, classical ML, neural-network, and graph-neural-network approaches under both random and Bemis–Murcko scaffold splits.

> Team project for NYU DS-GA 1003. This repository is a fork of the [original team repository](https://github.com/SanviNora/BBBP-ML-Project) and preserves its complete commit history and contributor attribution.

![AUC comparison across random and scaffold splits](results/auc_barchart_final.png)

## What the project studies

- **Representations:** Lipinski descriptors, ECFP4 fingerprints, and molecular graphs
- **Models:** Lipinski baseline, logistic regression, SVM, MLP, random forest, and GCN
- **Evaluation:** ROC-AUC, F1, precision, and recall across three seeds
- **Generalization:** random splits versus scaffold splits, which better test performance on unfamiliar chemical structures

## Selected results

The strongest recorded random-split ROC-AUC is **0.907 ± 0.015** from the random forest. On the more demanding scaffold split, the MLP records the strongest ROC-AUC at **0.775 ± 0.006**. The performance gap illustrates how molecular scaffold shift can make generalization substantially harder.

Results are reported from the checked-in experiment outputs in [`results/fingerprint_results.csv`](results/fingerprint_results.csv) and [`results/gcn_summary.csv`](results/gcn_summary.csv).

## Yila Cao's contributions

The preserved Git history documents Yila's work on:

- comparing fingerprint-based models across three seeds and two split strategies;
- adding class-imbalance handling to logistic regression, SVM, and MLP experiments;
- generating the cross-model ROC-AUC comparison and updating result visualizations.

See the repository's [contributors and commit history](https://github.com/SanviNora/BBBP-ML-Project/commits/bbbp_main/) for the full team record.

## Repository structure

```text
data/raw/               MoleculeNet BBBP data used by the experiments
src/data/               dataset loading, ECFP4 features, and scaffold splits
src/models/             baselines, fingerprint models, and GCN
src/evaluation/         metrics and command-line experiment runner
src/analysis/           error and representation analysis
results/                checked-in tables, figures, and analysis outputs
tests/                  focused data, metric, fingerprint-model, and GCN checks
```

## Setup

Python 3.10 or 3.11 is recommended.

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Reproduce the experiments

Run the fingerprint-based comparison:

```bash
python -m src.evaluation.runner --suite fingerprint
```

Run the GCN experiment separately because it is substantially more expensive:

```bash
python -m src.evaluation.runner --suite gcn
```

Run the lightweight test suite:

```bash
pytest -q tests/test_data.py tests/test_metrics.py
```

The experiments use seeds `42`, `123`, and `7`, defined in [`config.py`](config.py). Generated checkpoints and local environments are intentionally excluded from version control.

## Data and attribution

The repository includes the [MoleculeNet BBBP dataset](https://moleculenet.org/datasets-1) used by the original course project. Authors: Sanvi Jagtap, Yila Cao, and Yiyao Zhang, NYU Center for Data Science.

No separate license was included in the original team repository. The fork therefore does not add one or imply sole ownership.
