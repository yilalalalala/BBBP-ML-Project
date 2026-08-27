"""Command-line entry point for the project's experiment suites."""

from __future__ import annotations

import argparse
import runpy
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]
SUITES = {
    "fingerprint": PROJECT_ROOT / "results" / "fingerprint_comparison.py",
    "gcn": PROJECT_ROOT / "src" / "analysis" / "run_gcn_final.py",
}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--suite",
        choices=sorted(SUITES),
        default="fingerprint",
        help="Experiment suite to run (default: fingerprint).",
    )
    args = parser.parse_args()
    runpy.run_path(str(SUITES[args.suite]), run_name="__main__")


if __name__ == "__main__":
    main()
