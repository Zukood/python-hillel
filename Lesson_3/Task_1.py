#палиндром

some_word = input("Введите случайное слово: ")
some_word_reversed = some_word[::-1]

if some_word == some_word_reversed:
    print("+")
else:
    print("-")

