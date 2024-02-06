"""EX02 - One Shot Battleship!"""

__author__ = "730671788"

size_of_grid: int = 4
secret_row: int = 3
secret_column: int = 2

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"


reset = 1
reset2 = 1

row_input_of_player: int = int(input("Guess a row: "))
while reset == 1:
    if row_input_of_player > size_of_grid or row_input_of_player < 1:
        row_input_of_player = int(input(f"The grid is only {size_of_grid} by {size_of_grid}. Try again: "))
        if row_input_of_player > 0 and row_input_of_player <= size_of_grid:
            reset = 2
    else:
        reset = 2 

column_input_of_player: int = int(input("Guess a column: "))
while reset2 == 1:
    if column_input_of_player > size_of_grid or column_input_of_player < 1:
        column_input_of_player = int(input(f"The grid is only {size_of_grid} by {size_of_grid}. Try again: "))
        if column_input_of_player > 0 and column_input_of_player <= size_of_grid:
            reset2 = 2
    else:
        reset2 = 2

result_box = ""
if row_input_of_player == secret_row and column_input_of_player == secret_column:
    result_box = RED_BOX
else:
    result_box = WHITE_BOX

row_counter: int = 1

while row_counter <= size_of_grid:
    emoji_for_row: str = ""
    column_counter: int = 1
    if row_input_of_player == row_counter: 
        while column_counter <= size_of_grid:
            if column_input_of_player == column_counter:
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

if secret_row == row_input_of_player:
    if secret_column == column_input_of_player:
        print("Hit!")
    elif secret_column != column_input_of_player:
        print("Close! Correct row, wrong column.")
elif column_input_of_player == secret_column:
    if secret_row != row_input_of_player:
        print("Close! Correct column, wrong row.")
else:
    print("Miss!")