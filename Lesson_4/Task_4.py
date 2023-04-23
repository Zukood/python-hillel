prog_lang = {"Python": "Guido van Rossum", "Java": "James Gosling", "PHP": "Rasmus Lerdorf",
             "JavaScript": "Brendan Eich"}

for lang, dev in prog_lang.items():
    print(f"My favorite programming language is {lang}. It was created by {dev}")

del prog_lang['PHP']
print("Итоговая версия словаря: " + str(prog_lang))