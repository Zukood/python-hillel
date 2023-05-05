# lst = [23, 2, 3, 0]
#

def change_list(lst):
    if len(lst) < 2:
        print("Cписок должен иметь не меньше 2 элементов")
    else:

        lst[0], lst[-1] = lst[-1], lst[0]
        return lst
#
#
# print(change_list(lst))
