
import json

with open("group_people.json") as f:
    json_file = json.load(f)

max_group_id = ""
max_female_count = 0

for group in json_file:
    group_id = group["id_group"]
    female_count = 0

    for person in group["people"]:
        if person["gender"] == "Female" and person["year"] > 1977:
            female_count += 1

    if female_count > max_female_count:
        max_female_count = female_count
        max_group_id = group_id

print("Идентификатор группы:", max_group_id)
print("Количество женщин после 1977 года:", max_female_count)






