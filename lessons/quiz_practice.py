def find_even(words: list[str]) -> str:
    idx: int = 0
    while idx < len(words):
        if len(words[idx]) % 2 == 0:
            return words[idx]
        idx += 1
    return ""


def remove_first_even(words: list[str]) -> None:
    idx: int = 0
    condition: bool = True
    while (idx < len(words)) and condition:
        if len(words[idx]) % 2 == 0:
            words.pop(idx)
            condition = False
        idx += 1