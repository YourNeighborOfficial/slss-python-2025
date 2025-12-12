# Intro to Sort
# Author: julian
# 4 December

import csv

# Sorting Algorithms
# We'll implement selection sort in two ways
#     * implement basic version using the example from yesterday
#     * implement sort with songs based on YouTube views in descending order


def selection_sort(l: list[int], ascending=True) -> list[int]:
    """Sorts a given list using selection sort


    Params:
        1 - list of numbers to sort
        ascending - True if sorting in ascending order
    Returns:
        a sorted list
    """
    num_items = len(l)
    # starting at the beginning of the list
    for i in range(num_items):
        # set the lowest_num to the current number
        # set the lowest_index to the current index
        lowest_num = l[i]
        lowest_index = i
        # check the rest of the list
        for j in range(i + 1, num_items):
            # if this number is smaller than the lowest
            if l[j] > lowest_num:
                # set the lowest_num to this number
                lowest_num = l[j]
                # set the lowest_index to this index
                lowest_index = j
        # swap the current number with the number at the lowest index
        # lowest index
        l[i], l[lowest_index] = l[lowest_index], l[i]

    return l


if __name__ == "__main__":
    sorted_list = selection_sort([1, 43, 55, -11, 100, 34])

    print(sorted_list)
