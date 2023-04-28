class DiscriminantError(Exception):
    pass


a = float(input("Введите коэфицент a: "))
b = float(input("Введите коэфицент b: "))
c = float(input("Введите коэфицент c: "))

discriminant = b ** 2 - 4 * a * c
if discriminant < 0:
    raise DiscriminantError("Дискриминант меньше нуля")

x1 = (-b + discriminant ** 0.5) / (2 * a)
x2 = (-b - discriminant ** 0.5) / (2 * a)
print(f"Решение: x1={x1}, x2={x2}")