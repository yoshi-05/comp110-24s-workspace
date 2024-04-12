from quiz_practice import find_even
from quiz_practice import remove_first_even


def test_find_even_use_case() -> None:
    test_input: list[str] = ["Red", "Bluey", "Yellowy"]
    return_string: str = find_even(test_input)
    assert return_string == ""


def test_remove_first_even_use_case() -> None:
    test_input: list[str] = ["Red", "Blue", "Yellow"]
    remove_first_even(test_input)
    assert test_input == ["Red", "Yellow"]
