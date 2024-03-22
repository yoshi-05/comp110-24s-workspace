"""Summing the elements of a list using different loops."""

__author__ = "730671788"


def w_sum(vals: list[float]) -> float:
    """Using while loops."""
    x: int = 0
    added_value: float = 0.0
    if vals == []:
        return 0.0
    while x < len(vals):
        added_value = added_value + vals[x]
        x += 1
    return added_value


def f_sum(vals: list[float]) -> float:
    """Using for loops."""
    added_value: float = 0.0
    for index in vals:
        added_value = added_value + index
    return added_value


def f_range_sum(vals: list[float]) -> float:
    """Using range."""
    added_value: float = 0.0
    if vals == []:
        return 0.0
    for idx in range(0, len(vals)):
        added_value = added_value + vals[idx]
    return added_value