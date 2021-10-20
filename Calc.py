print("Назови первое число")
x = int(input())

print("Назови второе число")
y = int(input())

print("Назови знак")
sign = input()

if sign == '+':
    res = x + y
    print(f"Результат вычислений: {res}")
elif sign == '-':
    res = x - y
    print(f"Результат вычислений: {res}")
elif sign == '/':
    res = x / y
    print(f"Результат вычислений: {res}")
elif sign == '*':
    res = x * y
    print(f"Результат вычислений: {res}")


def summer(x, y):
    print("Первое число")
    inp_1 = int(input())
    print("Второе число")
    inp_2 = int(input())
    res = inp_1 + inp_2
    print(f"Результат служения: {res}")


