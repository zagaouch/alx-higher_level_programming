#!/usr/bin/python3
def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers.
    Complexity:
        O(log n)
    """

    left, right = 0, len(list_of_integers) - 1
    while left < right:
        mid = (left + right) // 2
        if (list_of_integers[mid] > list_of_integers[mid - 1]
            and list_of_integers[mid] > list_of_integers[mid + 1]):
            return mid
        elif list_of_integers[mid] < list_of_integers[mid - 1]:
            right = mid - 1
        else:
            left = mid + 1
    return left
