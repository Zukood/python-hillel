def to_dict(lst):
    return dict([(item, item) for item in lst])


my_list = [1, 2, 3, 4, 5]

my_dict = to_dict(my_list)
print(my_dict)
