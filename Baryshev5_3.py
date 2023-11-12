# Задание 1
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

num1 = 24
num2 = 36
print("Наибольший общий делитель чисел", num1, "и", num2, ":", gcd(num1, num2))
# задание 2
import random

def generate_number():
    return str(random.randint(1000, 9999))

def check_guess(secret_num, guess, attempts):
    cows = 0
    bulls = 0
    for i in range(4):
        if guess[i] == secret_num[i]:
            bulls += 1
        elif guess[i] in secret_num:
            cows += 1
    if bulls == 4:
        print("Поздравляю, вы угадали число! Количество попыток:", attempts)
    else:
        print("Быки:", bulls, "Коровы:", cows)
        new_guess = input("Введите следующее четырехзначное число: ")
        check_guess(secret_num, new_guess, attempts+1)

def main():
    secret_number = generate_number()
    print("Добро пожаловать в игру 'Быки и коровы'! Попробуйте угадать четырехзначное число.")
    user_guess = input("Введите четырехзначное число: ")
    check_guess(secret_number, user_guess, 1)

main()