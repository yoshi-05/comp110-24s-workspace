"""Example functions to learn defintion and calling syntax"""

def my_max(number1: int, number2: int) -> int:
    """Returns Max Value of out Two Numbers"""
    if number1 >= number2:
        return number1
    else: #number1 < number2
        return number2

max_number: int = my_max(1,10)
other_max_number: int = my_max(11,3)
#print(max_number)
print(other_max_number)