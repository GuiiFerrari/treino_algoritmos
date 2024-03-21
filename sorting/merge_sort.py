import numpy as np


def gen_int_random_array(size: int, low: int, high: int) -> np.ndarray:
    return np.random.randint(low=low, high=high, size=size)


def merge_sort(array: np.ndarray | list) -> np.ndarray | list:
    for j in range(1, len(array)):
        key = array[j]
        i = j - 1
        while i >= 0 and array[i] > key:
            array[i + 1] = array[i]
            i = i - 1
        array[i + 1] = key
    return array


def merge_sort_reversed(array: np.ndarray | list) -> np.ndarray | list:
    for i in range(len(array) - 2, -1, -1):
        key = array[i]
        j = i + 1
        while j < len(array) and array[j] < key:
            array[j - 1] = array[j]
            j = j + 1
        array[j - 1] = key
    return array


def main():
    array = gen_int_random_array(size=5, low=0, high=10)
    print(array)
    sorted_array = merge_sort(array=array.copy())
    print(sorted_array)
    sorted_array_v2 = merge_sort_reversed(array=array.copy())
    print(sorted_array_v2)
    array.sort()
    print(
        np.array_equal(a1=array, a2=sorted_array),
        np.array_equal(a1=array, a2=sorted_array_v2),
    )


if __name__ == "__main__":
    main()
