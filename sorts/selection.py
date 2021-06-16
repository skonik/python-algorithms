from typing import List


def selection_sort(array: List[int]) -> List[int]:

    i = 0

    while i < len(array):
        min_item_index = i

        j = i
        while j < len(array):
            if array[j] < array[min_item_index]:
                min_item_index = j

            j += 1

        array[i], array[min_item_index] = array[min_item_index], array[i]

        i += 1

    return array

