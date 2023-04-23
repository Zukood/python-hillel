subjects_dict = {"subjects": {"science":
                                  {"physics": ("nuclear physics", "optics", "thermodynamics"),
                                   "computer science": {},
                                   "biology": {}
                                   },
                              "humanities": {},
                              "public": {}}
                 }
print("Ключи science:", list(subjects_dict["subjects"]["science"].keys()))
print("Значение ключа physics:", subjects_dict["subjects"]["science"]["physics"])
