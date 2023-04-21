some_text = input("Введит текст на английском языке: ")

if some_text.startswith("abc"):
    some_text = "www" + some_text[3:]
else:
    some_text = some_text + "zzz"
print(some_text)

