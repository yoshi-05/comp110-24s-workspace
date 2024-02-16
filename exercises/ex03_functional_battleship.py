"""EX03 - Functional Battleship!"""

__author__ = "730671788"
import random


def input_guess(size_of_grid: int, row_or_column: str) -> int:
    """This function serves the purpose of providing the prompt for column and row."""
    assert row_or_column == "row" or row_or_column == "column"
    ask_question: int = int(input(f"Guess a {row_or_column}: "))
    while ask_question > size_of_grid or ask_question <= 0: 
        ask_question = int(input(f"The grid is only {size_of_grid} by {size_of_grid}. Try again: "))
    return (ask_question)


def print_grid(size_of_grid: int, row_guess: int, column_guess: int, guess_correct_or_nah: bool) -> None:
    """This function serves to print the grid based on the user's inputs."""
    BLUE_BOX: str = "\U0001F7E6"
    RED_BOX: str = "\U0001F7E5"
    WHITE_BOX: str = "\U00002B1C"
    result_box = ""
    if guess_correct_or_nah is True:
        result_box = RED_BOX
    elif guess_correct_or_nah is False:
        result_box = WHITE_BOX
    row_counter: int = 1
    while row_counter <= size_of_grid:
        emoji_for_row: str = ""
        column_counter: int = 1
        if row_guess == row_counter: 
            while column_counter <= size_of_grid:
                if column_guess == column_counter:
                    emoji_for_row += result_box
                else:
                    emoji_for_row += BLUE_BOX
                column_counter += 1
        else:
            while column_counter <= size_of_grid:
                emoji_for_row += BLUE_BOX
                column_counter += 1
        print(emoji_for_row)
        row_counter += 1


def correct_guess(secret_row: int, secret_column: int, row_guess: int, column_guess: int) -> bool:
    """This function serves to establish whether the user's guess is correct."""
    if secret_row == row_guess and secret_column == column_guess:
        return True
    else:
        return False


def main(size_of_grid: int, secret_row: int, secret_column: int) -> None:
    """This function combines all of the other functions to run the game smoothly."""
    user_turn: int = 1
    user_win_or_not: bool = False
    while user_turn <= 5 and user_win_or_not is False:
        print(f"=== Turn {user_turn}/5 ===")
        user_guess_row = input_guess(size_of_grid, "row")
        user_guess_column = input_guess(size_of_grid, "column")
        correct_ = correct_guess(secret_row, secret_column, user_guess_row, user_guess_column)
        print_grid(size_of_grid, user_guess_row, user_guess_column, correct_)
        if correct_ is True:
            print("Hit!")
            print(f"You won in {user_turn}/5 turns!")
            user_win_or_not = True
        else:
            print("Miss!")
            if user_turn >= 5:
                print("X/5 - Better luck next time!")
        user_turn += 1


if __name__ == "__main__":
    grid_size: int = random.randint(3, 5)
    main(grid_size, random.randint(1, grid_size), random.randint(1, grid_size))