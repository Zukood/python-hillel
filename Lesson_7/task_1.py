import csv


exchange_rate = 37


with open('test_file.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)

    with open('salaries_uah.csv', 'w', newline='') as outfile:
        fieldnames = ['Employee', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)

        writer.writeheader()

        for row in reader:
            employee = row['']
            salaries = [int(salary) * exchange_rate for salary in list(row.values())[1:]]

            writer.writerow({'Employee': employee, 'Jan': salaries[0], 'Feb': salaries[1], 'Mar': salaries[2],
                             'Apr': salaries[3], 'May': salaries[4], 'Jun': salaries[5], 'Jul': salaries[6],
                             'Aug': salaries[7], 'Sep': salaries[8], 'Oct': salaries[9], 'Nov': salaries[10],
                             'Dec': salaries[11]})

print('Salaries converted and saved to salaries_uah.csv')
