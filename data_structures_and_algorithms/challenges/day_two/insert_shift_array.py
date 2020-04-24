def insert_shift_arr(arr, val_to_insert):
    if arr is None or not arr or val_to_insert is None or not val_to_insert:
        return None
    index = get_middle_index(arr)
    arr.insert(index, val_to_insert)
    return arr


def delete_shift_arr(arr):
    if arr is None or not arr:
        return None
    len_array_int = int(len(arr) / 2)
    if len(arr) % 2 != 0:
        arr.pop(len_array_int)
    return arr


def insert_shift_arr_long_version(arr, val_to_insert):
    new_arr = []
    index = get_middle_index(arr)
    new_arr_counter = 0
    for counter, value in enumerate(arr):
        if index == counter:
            new_arr.insert(new_arr_counter, val_to_insert)
            new_arr_counter += 1
        new_arr.insert(new_arr_counter, value)
        new_arr_counter += 1
    return new_arr


def delete_shift_arr_long_version(arr):
    len_array_int = int(len(arr) / 2)
    if len(arr) % 2 != 0:
        arr.pop(len_array_int)
    return arr


def get_middle_index(arr):
    len_array_int = int(len(arr) / 2)
    return len_array_int if len(arr) % 2 == 0 else len_array_int + 1
