def binary_search(arr, val_to_find):
    first = 0
    last = len(arr) - 1
    val_index = -1
    found = False
    while first <= last and not found:
        mid = (first + last) // 2
        if arr[mid] == val_to_find:
            found = True
            val_index = arr.index(val_to_find)
        else:
            if val_to_find < arr[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return val_index
