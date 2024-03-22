"""Dictionary Utility Functions!"""

__author__ = "730671788"


def invert(dict1: dict[str, str]) -> dict[str, str]:
    """Inverting dictionary."""
    return_dict: dict[str, str] = {}
    for key in dict1:
        if dict1[key] in return_dict:
            raise KeyError("Duplicate value found!")
        return_dict[dict1[key]] = key
    return return_dict


def favorite_color(dict1: dict[str, str]) -> str:
    """Identifying the favorite color."""
    color_dict: dict[str, int] = {}
    max_color: str = ""
    max_frequency: int = 0
    for key in dict1:
        if dict1[key] in color_dict:
            color_dict[dict1[key]] += 1
        else:
            color_dict[dict1[key]] = 1
    for key in color_dict:
        if color_dict[key] > max_frequency:
            max_frequency = color_dict[key]
            max_color = key
    return max_color


def count(list1: list[str]) -> dict[str, int]:
    """Count."""
    return_dict: dict[str, int] = {}
    for elem in list1:
        if elem in return_dict:
            return_dict[elem] += 1
        else: 
            return_dict[elem] = 1
    return return_dict


def alphabetizer(list1: list[str]) -> dict[str, list[str]]:
    """Categorizes words under letters."""
    return_dict: dict[str, list[str]] = {}
    for elem in list1:
        f_letter = elem[0].lower()
        if f_letter in return_dict:
            return_dict[f_letter].append(elem)
        else:
            return_dict[f_letter] = [elem]
    return return_dict


def update_attendance(dict1: dict[str, list[str]], week_day: str, s_name: str) -> None:
    """Updating Attendance!"""
    if week_day in dict1 and s_name in dict1 is False:
        dict1[week_day].append(s_name)
    else:
        dict1[week_day] = [s_name]