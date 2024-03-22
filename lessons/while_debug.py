"""Practice while loops and debug them"""

#my_number: int = 8675309
#my_number_str: str = str(my_number)
#total: int = 0
#index: int = 0
#while index < len(my_number_str):
    #value: int = int(my_number_str[index])
    #total += value
    #index += 1




x: int = 0 
Same_or_not = True
while x < len(list_) and Same_or_not == True:
    index_of_list: int = list[x]
    if index_of_list == number_:
        Same_or_not = True
        x += 1
    else:
        Same_or_not = False
    if Same_or_not == True:
        print ("True")
    else:
        print ("False")
    