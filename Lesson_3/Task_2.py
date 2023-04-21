some_text = input("Введите текст: ")
some_word = input("Теперь ввведите слово которое нужно найти в этом тексте: ")

if some_word in some_text:
    print("Yes")
else:
    print("No")