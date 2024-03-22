"""Testing Dictionary Utility Functions!"""

__author__ = "730671788"


from exercises.ex05.dictionary import invert
from exercises.ex05.dictionary import favorite_color
from exercises.ex05.dictionary import count
from exercises.ex05.dictionary import alphabetizer
from exercises.ex05.dictionary import update_attendance
import pytest


def test_invert_1() -> None:
    """Testing Use Case."""
    dict1: dict[str, str] = {"number": "one"}
    return_dict: dict[str, str] = {}
    return_dict = invert(dict1)
    assert return_dict == {"one": "number"}


def test_invert_2() -> None:
    """Testing Use Case (2)."""
    dict1: dict[str, str] = {"reginald": "subnautica"}
    return_dict: dict[str, str] = {}
    return_dict = invert(dict1)
    assert return_dict == {"subnautica": "reginald"}


def test_invert_3() -> None:
    """Testing Edge Case (Using numbers in strings)!"""
    with pytest.raises(KeyError):
        dict1: dict[str, str] = {"subautica": "reginald", "name": "reginald"}
        invert(dict1)


def test_favorite_color_1() -> None:
    """Testing Use Case 1!"""
    dict1: dict[str, str] = {"Person_1": "yellow", "Person_2": "blue", "Person_3": "blue"}
    return_string: str = ""
    return_string = favorite_color(dict1)
    assert return_string == "blue"


def test_favorite_color_2() -> None:
    """Testing Use Case 2!"""
    dict1: dict[str, str] = {"Person_1": "yellow", "Person_2": "blue", "Person_3": "red"}
    return_string: str = ""
    return_string = favorite_color(dict1)
    assert return_string == "yellow"


def test_favorite_color_3() -> None:
    """Testing Edge Case using all colors!"""
    dict1: dict[str, str] = {"Blue": "yellow", "Green": "yellow", "Purple": "blue", "Red": "blue"}
    return_string: str = ""
    return_string = favorite_color(dict1)
    assert return_string == "yellow"


def test_count_1() -> None:
    """Testing Use Case 1!"""
    list1: list[str] = ["Blue", "Red", "Red", "Blue", "Yellow"]
    return_dict: dict[str, int] = {}
    return_dict = count(list1)
    assert return_dict == {"Blue": 2, "Red": 2, "Yellow": 1}


def test_count_2() -> None:
    """Testing Use Case 1!"""
    list1: list[str] = ["Blue", "Red", "Red", "Blue", "Yellow"]
    return_dict: dict[str, int] = {}
    return_dict = count(list1)
    assert return_dict == {"Blue": 2, "Red": 2, "Yellow": 1}


def test_count_3() -> None:
    """Testing Edge Case !"""
    list1: list[str] = ["Blue", "Red", "Red", "Blue", "Yellow"]
    return_dict_1: dict[str, int] = {}
    return_dict_2: dict[str, int] = {}
    return_dict_1 = count(list1)
    assert return_dict_1 == {"Blue": 2, "Red": 2, "Yellow": 1}
    list1.pop(1)
    return_dict_2 = count(list1)
    assert return_dict_2 == {"Blue": 2, "Red": 1, "Yellow": 1}


def test_alphabetizer_1() -> None:
    """Testing Use Case 1!"""
    list1: list[str] = ["purple", "red", "yellow", "yak"]
    return_dict = alphabetizer(list1)
    assert return_dict == {'p': ['purple'], 'r': ['red'], 'y': ['yellow', 'yak']}


def test_alphabetizer_2() -> None:
    """Testing Use Case 2!"""
    list1: list[str] = ["Purple", "Red", "Yellow", "Rake"]
    return_dict = alphabetizer(list1)
    assert return_dict == {'p': ['Purple'], 'r': ['Red', "Rake"], 'y': ['Yellow']}


def test_alphabetizer_3() -> None:
    """Testing Edge Case!"""
    with pytest.raises(IndexError):
        list1: list[str] = [""]
        alphabetizer(list1)


def test_update_attendance_1() -> None:
    """Testing Use Case 1!"""
    dict1: dict[str, list[str]] = {"Cars": ["Toyota", "Honda"], "Motorbikes": ["KTM"]}
    update_attendance(dict1, "Motorbikes", "Yamaha")
    assert dict1 == {"Cars": ["Toyota", "Honda"], "Motorbikes": ["KTM", "Yamaha"]}


def test_update_attendance_2() -> None:
    """Testing Use Case 2!"""
    dict1: dict[str, list[str]] = {"Cars": ["Toyota", "Honda"], "Motorbikes": ["KTM"]}
    update_attendance(dict1, "Cars", "Mercedes")
    assert dict1 == {"Cars": ["Toyota", "Honda", "Mercedes"], "Motorbikes": ["KTM"]}


def test_update_attendance_3() -> None:
    """Testing Edge Case!"""
    dict1: dict[str, list[str]] = {"Cars": ["Toyota", "Honda"], "Motorbikes": ["KTM"]}
    update_attendance(dict1, "Motorbikes", "Yamaha")
    assert dict1 == {"Cars": ["Toyota", "Honda"], "Motorbikes": ["KTM", "Yamaha"]}
    dict1["Motorbikes"].pop(0)
    assert dict1 == {"Cars": ["Toyota", "Honda"], "Motorbikes": ["Yamaha"]}