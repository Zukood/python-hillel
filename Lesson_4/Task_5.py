e2g_dict = {"stork": "torch", "hawk": "falke", "woodpecker": "specht", "owl": "eule"}
print("ENGLISH-GERMAN dictionary:")
for eng, ger in e2g_dict.items():
    print(f"English word: {eng} - German word: {ger} ")
print("**************************************")
print(f"Owl in German - {e2g_dict['owl']}")
print("**************************************")
e2g_dict["cat"] = "Katze"
e2g_dict["dog"] = "Hund"
print("ENGLISH-GERMAN dictionary with new words:")
for eng, ger in e2g_dict.items():
    print(f"English word: {eng} - German word: {ger} ")
print("**************************************")
print("Dictionary with new words in list:")
e2g_dict_list = list(e2g_dict.items())
print(e2g_dict_list)

