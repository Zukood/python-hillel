some_text = input("Введите произвольный текст через пробел: ")

text_to_list = some_text.split()

if len(text_to_list) < 3:
    print("Ошибка: cписок должен содержать как минимум 3 элемента.", "В текущем списке: ", len(text_to_list))
else:
    print(text_to_list[-3:])



