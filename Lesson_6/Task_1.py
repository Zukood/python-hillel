n = int(input("Введіть натуральне число: "))

while n > 1 and n % 2 == 0:
    n //= 2

if n == 1:
    print("YES")
else:
    print("NO")