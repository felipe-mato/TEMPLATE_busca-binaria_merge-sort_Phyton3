def binary_search(list_data, value):
    low = 0
    high = len(list_data) -1
    while (low <= high):
        mid = (low + high) // 2
        if (list_data[mid]) == value:
            return mid
        elif (list_data[mid] < value):
            low = mid + 1
        else:
            high = mid -1
    return -1

data = [31,32,63,130,131,220,46,423,
        444,464,482,490,492,504,514,
        558,600,608,664,690,691,693,
        785,819,843,884,899,901,908,
        908,913,940]
print(binary_search(data, 490))