"""Unit tests for evaluation helpers."""

import pytest

from src.evaluation.metrics import compute_metrics


def test_compute_metrics_for_perfect_predictions():
    metrics = compute_metrics(
        y_true=[0, 0, 1, 1],
        y_pred=[0, 0, 1, 1],
        y_proba=[0.1, 0.2, 0.8, 0.9],
    )

    for name in ("accuracy", "f1", "precision", "recall", "auc"):
        assert metrics[name] == pytest.approx(1.0)


def test_auc_is_nan_when_probabilities_are_omitted():
    metrics = compute_metrics(y_true=[0, 1], y_pred=[0, 1])

    assert metrics["auc"] != metrics["auc"]
