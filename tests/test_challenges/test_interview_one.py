import pytest
from data_structures_and_algorithms.challenges.day_4.interview_one import sum_of_rows


@pytest.mark.parametrize(
    "array, expected",
    [([[1, 2, 3], [3, 5, 7], [1, 7, 10]], [6, 15, 18]),
     ([[0, 1, 5], [-4, 7, 2], [-3, 12, 11]], [6, 5, 20]),
     ([[0, 1, 5], [-4, None, 2], [-3, 12, 11]], [6, -2, 20])]
)
def test_sum_of_rows(array, expected):
    assert sum_of_rows(array) == expected
