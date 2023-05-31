class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        real_sum = self.real + other.real
        imaginary_sum = self.imaginary + other.imaginary
        return ComplexNumber(real_sum, imaginary_sum)

    def __sub__(self, other):
        real_diff = self.real - other.real
        imaginary_diff = self.imaginary - other.imaginary
        return ComplexNumber(real_diff, imaginary_diff)

    def __str__(self):
        return f"{self.real} + {self.imaginary}i"

#Пример

num1 = ComplexNumber(2, 3)
num2 = ComplexNumber(1, 4)

sum_result = num1 + num2
diff_result = num1 - num2

print(sum_result)   # Вывод: 3 + 7i
print(diff_result)  # Вывод: 1 - 1i
