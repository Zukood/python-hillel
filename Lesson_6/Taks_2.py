def square(side):
    perimeter = 4 * side
    area = side ** 2
    diagonal = side * (2 ** 0.5)
    return perimeter, area, diagonal


result = square(2)
result_t = tuple(round(num, 2) for num in result)
print("Периметр, площадь и диагональ квадрата: ", result_t)
