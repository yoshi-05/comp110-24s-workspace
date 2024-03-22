"""List Utility Functions!"""

__author__ = "730671788"


def all(list_: list[int], number_: int) -> bool:
    """Testing whether the whole list is equal to Int."""
    x: int = 0 
    Same_or_not = True
    if len(list_) == 0:
        return False
    while x < len(list_) and Same_or_not is True:
        if list_[x] == number_:
            Same_or_not = True
            x += 1
        else:
            Same_or_not = False
    return Same_or_not
    

def max(int_list: list[int]) -> int:
    """Finding the max number in the list."""
    if len(int_list) == 0:
        raise ValueError("max() arg is an empty List")
    high_number: int = int_list[0]
    x: int = 0
    while x < len(int_list):
        if int_list[x] > high_number:
            high_number = int_list[x]
        x += 1
    return high_number


def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    """Seeing whether two lists are equal."""
    Same_or_not = True
    x: int = 0
    if len(list_1) == 0 and len(list_2) != 0 or len(list_2) == 0 and len(list_1) != 0 or len(list_1) != len(list_2):
        Same_or_not = False
    while x < len(list_1) and x < len(list_2) and Same_or_not is True:
        for elem in list_1:
            if elem == list_2[x]:
                x += 1
            else:
                Same_or_not = False
    return Same_or_not


def extend(list_1: list[int], list_2: list[int]) -> None:
    """Extending a list."""
    x: int = 0
    while x < len(list_2):
        list_1.append(list_2[x])
        x += 1