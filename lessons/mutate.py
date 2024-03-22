"""Mutating functions."""


__author__ = "730671788"


def manual_append(list_1: list[int], number_1: int) -> None:
    """Appending a List."""
    list_1.append(number_1)


def double(the_doubled_input: list[int]) -> None:
    """Doubling Function."""
    number_multipled = 0
    while number_multipled < len(the_doubled_input):
        the_doubled_input[number_multipled] = the_doubled_input[number_multipled] * 2
        number_multipled += 1 
