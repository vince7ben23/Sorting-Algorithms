import random
import pytest
from src.sort.merge_sort import MergeSortRecursive, MergeSortIterative, MergeSortIterativeWithStack

VARIANTS = [MergeSortRecursive, MergeSortIterative, MergeSortIterativeWithStack]

EDGE_CASES = [
    ([2, 1], [1, 2]),
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
    ([3, 1, 2, 3, 1, 2], [1, 1, 2, 2, 3, 3]),
]

def run_merge_sort(cls, arr):
    if cls is MergeSortIterative:
        cls.merge_sort(arr)
    else:
        cls.merge_sort(arr, 0, len(arr) - 1)

@pytest.mark.parametrize("cls", VARIANTS)
def test_merge_sort(cls):
    sample = random.sample(range(1,11), 10)
    run_merge_sort(cls, sample)
    assert sample == list(range(1, 11))

@pytest.mark.parametrize("cls", VARIANTS)
@pytest.mark.parametrize("input_arr,expected", EDGE_CASES)
def test_merge_sort_edge_cases(cls, input_arr, expected):
    sample = list(input_arr)
    run_merge_sort(cls, sample)
    assert sample == expected
