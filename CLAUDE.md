# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Environment Setup

Uses conda with Python 3.7:

```bash
conda env create -f environment.yml -n "sorting_algo"
conda activate sorting_algo
```

## Commands

**Run tests:**
```bash
python -m pytest
python -m pytest -v --cov ./src/
```

**Run a single test:**
```bash
python -m pytest tests/test_merge_sort.py::test_merge_sort_recursive
```

**Run performance benchmarks** (from `src/`):
```bash
python -m main
```

## Architecture

All sorting implementations sort **in-place** and share a consistent interface.

### `src/sort/`

Each algorithm module contains static/class method implementations grouped by class:

- **`merge_sort.py`** — Three variants:
  - `MergeSortRecursive` — classic divide-and-conquer, `merge_sort(arr, left, right)`
  - `MergeSortIterative` — queue-based bottom-up, `merge_sort(arr)` (no index args)
  - `MergeSortIterativeWithStack` — two-stack approach, `merge_sort(arr, left, right)`

- **`quick_sort.py`** — Three variants, all use random pivot selection:
  - `QuickSortRecursiveLomuto` — Lomuto partition, recursive
  - `QuickSortIterativeLomuto` — Lomuto partition, stack-based iterative
  - `QuickSortRecursiveHoare` — Hoare partition, recursive (note: recursive call includes pivot: `quick_sort(arr, left, pivot)`)

### `src/main.py`

Performance harness using `timeit` on 1M-element arrays. Not a test file — import paths use bare `sort.*` (no `src.` prefix), relying on being run as `python -m main` from the `src/` directory.

### `tests/`

Pytest tests import via `src.sort.*`. All tests use `random.sample(range(1,11), 10)` (permutations of 1–10) and assert the result equals `list(range(1, 11))`.

### Key interface differences

`MergeSortIterative.merge_sort` takes only `arr` (no `left`/`right`). All other variants take `(arr, left, right)`.
