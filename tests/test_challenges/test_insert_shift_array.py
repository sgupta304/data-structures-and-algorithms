from data_structures_and_algorithms.challenges.day_two.insert_shift_array import insert_shift_arr, delete_shift_arr, \
    insert_shift_arr_long_version


def test_arr_insert_arr_none():
    actual = insert_shift_arr(None, 5)
    expected = None
    assert actual == expected


def test_arr_insert_val_none():
    actual = insert_shift_arr([2, 4, 6, 8], None)
    expected = None
    assert actual == expected


def test_arr_insert_both_none():
    actual = insert_shift_arr(None, None)
    expected = None
    assert actual == expected


def test_arr_insert_empty_arr():
    actual = insert_shift_arr([], 5)
    expected = None
    assert actual == expected


def test_arr_insert_empty_val():
    actual = insert_shift_arr([2, 4, 6, 8], '')
    expected = None
    assert actual == expected


def test_arr_insert_empty_val_and_empty_arr():
    actual = insert_shift_arr([], '')
    expected = None
    assert actual == expected


def test_arr_insert_shift_one():
    actual = insert_shift_arr([2, 4, 6, 8], 5)
    expected = [2, 4, 5, 6, 8]
    assert actual == expected


def test_arr_insert_shift_two():
    actual = insert_shift_arr([4, 8, 15, 23, 42], 16)
    expected = [4, 8, 15, 16, 23, 42]
    assert actual == expected


def test_arr_insert_shift_words():
    actual = insert_shift_arr(["One", "8", "15", "23", "Ten"], "16")
    expected = ["One", "8", "15", "16", "23", "Ten"]
    assert actual == expected


def test_arr_insert_shift_mix():
    actual = insert_shift_arr(["One", "8", "15", "23", "Ten"], 16)
    expected = ["One", "8", "15", 16, "23", "Ten"]
    assert actual == expected


def test_arr_insert_shift_longer_version_one():
    actual = insert_shift_arr_long_version([2, 4, 6, 8], 5)
    expected = insert_shift_arr([2, 4, 6, 8], 5)
    assert actual == expected


def test_arr_insert_shift_longer_version_two():
    actual = insert_shift_arr_long_version([4, 8, 15, 23, 42], 16)
    expected = insert_shift_arr([4, 8, 15, 23, 42], 16)
    assert actual == expected


def test_arr_insert_shift_longer_version_words():
    actual = insert_shift_arr_long_version(["One", "8", "15", "23", "Ten"], "16")
    expected = insert_shift_arr(["One", "8", "15", "23", "Ten"], "16")
    assert actual == expected


def test_arr_insert_shift_longer_version_mix():
    actual = insert_shift_arr_long_version(["One", "8", "15", "23", "Ten"], 16)
    expected = insert_shift_arr(["One", "8", "15", "23", "Ten"], 16)
    assert actual == expected


def test_arr_delete_shift_one():
    actual = delete_shift_arr([2, 4, 6, 8])
    expected = [2, 4, 6, 8]
    assert actual == expected


def test_arr_delete_shift_two():
    actual = delete_shift_arr([4, 8, 15, 23, 42])
    expected = [4, 8, 23, 42]
    assert actual == expected


def test_arr_delete_shift_words():
    actual = delete_shift_arr(["One", "8", "15", "23", "Ten"])
    expected = ["One", "8", "23", "Ten"]
    assert actual == expected


def test_arr_delete_shift_mix():
    actual = delete_shift_arr(["One", "8", 15, "23", "Ten"])
    expected = ["One", "8", "23", "Ten"]
    assert actual == expected


def test_arr_delete_empty_arr():
    actual = delete_shift_arr([])
    expected = None
    assert actual == expected


def test_arr_delete_none_arr():
    actual = delete_shift_arr(None)
    expected = None
    assert actual == expected
