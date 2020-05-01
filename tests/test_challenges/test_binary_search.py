import pytest
from data_structures_and_algorithms.challenges.day_three.binary_search import binary_search


@pytest.mark.parametrize(
    "arr, val_to_find, expected", [([4, 8, 15, 16, 23, 42], 15, 2),
                                   ([11, 22, 33, 44, 55, 66, 77], 90, -1),
                                   ([88, 32, 33, 44, 12], 44, 3),
                                   ([], 2, -1),
                                   ([], '', -1)]
)
def test_binary_search(arr, val_to_find, expected):
    assert binary_search(arr, val_to_find) == expected
