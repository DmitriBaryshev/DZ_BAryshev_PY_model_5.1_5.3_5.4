# Задание 1
def a():
    print("""Don't compare yourself with anyone in this world…
if you do so, you are insulting yourself.
\t\t\t\t\t\t\t\t\t\tBill Gates""")


a()
# Задание 2
def b(a, b):
    for i in range(a, b+1):
        if i % 2 == 0:
            print(i, end=" ")


b(1, 50)
print()
# Задание 3


def a(length, symbol, filled):
    if filled:
        for i in range(length):
            print(symbol * length)
    else:
        print(symbol * length)
        for i in range(length - 2):
            print(symbol + " " * (length - 2) + symbol)
        print(symbol * length)

# Пример использования функции
a(5, "*", True)
a(5, "*", False)


# Задание 4
def n(a, b, c, d, e):
    return min(a, b, c, d, e)


print(n(3, 6, -5, 500, 400))
# Задание 5
def m(a, b):
    if a > b:
        a, b = b, a
    result = 1
    for i in range(a, b + 1):
        result *= i
    return result


print(m(6, 4))


# Задание 6
def l(a):
    return len(str(a))


print(l(11366))

# Задание 7


def h(n):
    if len(str(n)) != 6:
        return False
    digits = [int(i) for i in str(n)]
    sum1 = sum(digits[:3])
    sum2 = sum(digits[3:])
    return sum1 == sum2


print(h(123420))
print(h(123456))
   