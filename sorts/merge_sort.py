from typing import List


def merge(left: List[int], right: List[int]) -> List[int]:
    total_length = len(left + right)
    left_idx, right_idx = 0, 0

    merged = [0 for _ in range(total_length)]
    merged_idx = 0

    while merged_idx < len(merged):

        left_done = left_idx == len(left)
        right_done = right_idx == len(right)

        if not left_done and not right_done:
            left_element = left[left_idx]
            right_element = right[right_idx]

            if left_element < right_element:
                merged[merged_idx] = left_element
                left_idx += 1
            else:
                merged[merged_idx] = right_element
                right_idx += 1
        else:
            break

        merged_idx += 1

    while left_idx < len(left):
        merged[merged_idx] = left[left_idx]
        left_idx += 1
        merged_idx += 1

    while right_idx < len(right):
        merged[merged_idx] = right[right_idx]
        right_idx += 1
        merged_idx += 1

    return merged


def merge_sort(ar: List[int]) -> List[int]:
    if len(ar) <= 1:
        return ar

    half = len(ar) // 2

    left, right = ar[:half], ar[half:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)
