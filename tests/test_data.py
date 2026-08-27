"""Focused checks for molecular fingerprint generation."""

import numpy as np

from src.data.dataset import smiles_to_ecfp4


def test_valid_smiles_returns_binary_fingerprint():
    fingerprint = smiles_to_ecfp4("CCO", n_bits=128)

    assert fingerprint.shape == (128,)
    assert fingerprint.dtype == np.float32
    assert set(np.unique(fingerprint)).issubset({0.0, 1.0})


def test_invalid_smiles_returns_none():
    assert smiles_to_ecfp4("not-a-smiles") is None
