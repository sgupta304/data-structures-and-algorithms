from data_structures_and_algorithms.challenges.day_one.array_reverse import reverse_list


def test_int_array():
    arr = [1, 3, 4, 5, 6, 8]
    actual = reverse_list(arr)
    expected = [8, 6, 5, 4, 3, 1]
    assert actual == expected


def test_int_array_negative():
    arr = [89, 2354, 3546, 23, 10, -923, 823, -12]
    actual = reverse_list(arr)
    expected = [-12, 823, -923, 10, 23, 3546, 2354, 89]
    assert actual == expected


def test_int_array_empty():
    arr = []
    actual = reverse_list(arr)
    expected = []
    assert actual == expected


def test_int_array_single_element():
    arr = [1]
    actual = reverse_list(arr)
    expected = [1]
    assert actual == expected


def test_int_array_text():
    arr = ["One", "Two", "Three", "Four", "Five"]
    actual = reverse_list(arr)
    expected = ["Five", "Four", "Three", "Two", "One"]
    assert actual == expected
