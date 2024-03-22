#stats: list[int] = [7, 8, 9]
#index: int = 0
#total: int = 100
#while index < len(stats):
    #total -= stats[index]
    #index += 1
#print(total)


#stats: list[int] = [7, 8, 9]
#index: int = 0
#total: int = 100
#for elem in stats:
#    total -= elem
#print(total)


#stats: list[int] = [7, 8, 9]
#index: int = 0
#total: int = 100
#for idx in range(0, len(stats)):
#    total -= stats[idx]
#print(total)


#def odd_and_even(list1: list[int]) -> int:
#    return_list: list[int] = []
#    x: int = 0
 #   while x < len(list1):
  #      if list1[x] % 2 == 1 and x % 2 == 0:
   #         return_list.append(list1[x])
    #    x += 1
    #return return_list
#print(odd_and_even ([7 , 8 , 10 , 10 , 5 , 12 , 3 , 2 , 11 , 8]))


def short_words(list1: list[str]) -> list[str]:
    return_list: list[int] = []
    for word in list1:
        if len(word) < 5:
            return_list.append(word)
        else:
            print(f"{word} is too long!")
    return return_list
