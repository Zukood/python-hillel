mail_form = input("Введите свою почту: ")

if "@" and "." in mail_form:
    print("Yes")
else:
    print("No")