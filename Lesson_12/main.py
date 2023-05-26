import argparse
import math


def solve_quadratic_equation(a, b, c):
    """Розв'язує квадратне рівняння ax^2 + bx + c = 0"""
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        return None
    elif discriminant == 0:
        x = -b / (2 * a)
        return x
    else:
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return x1, x2


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Розрахунок квадратного рівняння')
    parser.add_argument('-a', type=float, default=0, help='параметр a')
    parser.add_argument('-b', type=float, required=True, help='параметр b')
    parser.add_argument('-c', type=float, required=True, help='параметр c')
    args = parser.parse_args()

    a = args.a
    b = args.b
    c = args.c

    result = solve_quadratic_equation(a, b, c)
    print('Результат розв\'язку квадратного рівняння:')
    if result is None:
        print('Рівняння не має розв\'язків')
    elif isinstance(result, float):
        print('x =', result)
    else:
        x1, x2 = result
        print('x1 =', x1)
        print('x2 =', x2)
