"""Functions that implement sorting algorithms."""

__author__ = "730671788"


def insertion_sort(x: list[int]) -> None:
    """Basic insertion sort algorithm. Insert into an already sorted list."""
    sorted_idx: int = 0
    for idx in range (0, len(x) - 1):
        unsorted_idx: int = sorted_idx + 1
        current_elem = x[unsorted_idx]
        while unsorted_idx > 0 and current_elem < x[unsorted_idx -1]:
            x[unsorted_idx] = x[unsorted_idx -1]
            unsorted_idx -= 1
        x[unsorted_idx] = current_elem
        sorted_idx += 1
    return None


def selection_sort(x: list[int]) -> None:
    """Basic selection sort algorithm. Repeatedly find the minimum and swap it."""
    idx_counter: int = 0
    while idx_counter < len(x):
        minimum_idx = idx_counter
        idx_counter2 = idx_counter
        for idx in range(idx_counter2 + 1, len(x)):
            if x[idx] < x[minimum_idx]:
                minimum_idx = idx
            idx_counter2 += 1
        if x[minimum_idx] < x[idx_counter]:
            tempo = x[idx_counter]
            x[idx_counter] = x[minimum_idx]
            x[minimum_idx] = tempo
        idx_counter += 1
    return None