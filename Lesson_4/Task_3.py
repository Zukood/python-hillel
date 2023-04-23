camel_case_list = ["FirstItem", "FriendsList", "MyTuple"]
snake_case_list = []

for items in camel_case_list:
    snake_case = ''
    for i, char in enumerate(items):
        if char.isupper():
            if i == 0:
                snake_case += char.lower()
            else:
                snake_case += '_' + char.lower()
        else:
            snake_case += char
    snake_case_list.append(snake_case)

print(snake_case_list)
