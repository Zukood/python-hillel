class FormulaError(Exception):
    pass


print("Введите формулу которая состоит из двух знаков и оператора + или - через пробел")
formula = input("Введите число согласно формуле: ")
formula_input = str.split(formula)
try:
    try:
        if len(formula_input) != 3:
            raise FormulaError("Неверный формат формулы")
        if formula_input[1] not in ("+", "-"):
            raise FormulaError("Неверный оператор")
        num_1 = float(formula_input[0])
        num_2 = float(formula_input[2])
    except ValueError:
        raise FormulaError("Ошибка, элементы должны быть цифры ")
except FormulaError:
    print("FormulaError - ошибка, элементы должны быть цифры!")
else:
    if formula_input[1] == "+":
        result = num_1 + num_2
    else:
        result = num_1 - num_2

    print(round(result, 2))
