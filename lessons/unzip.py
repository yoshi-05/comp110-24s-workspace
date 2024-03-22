"""Splitting a dictionary into two lists!"""

__author__ = "730671788"


def get_keys(a: dict[str, int]) -> list[str]:
    """Function to get keys!"""
    list_1: list[str] = []
    for key in a:
        list_1.append(key)
    return list_1


def get_values(a: dict[str, int]) -> list[int]:
    """Function to get values!"""
    list_1: list[int] = []
    for key in a:
        list_1.append(a[key])
    return list_1