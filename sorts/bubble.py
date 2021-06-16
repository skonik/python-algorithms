from typing import List


def bubble_sort(array: List[int]) -> List[int]:


    for i in range(len(array) - 1):
        swapped = False
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                swapped = True
                print(f'swapping! {array[j]} and {array[j + 1]}')
                array[j], array[j + 1] = array[j + 1], array[j]
            print(array)
        if swapped == False:
            return array

    return array


