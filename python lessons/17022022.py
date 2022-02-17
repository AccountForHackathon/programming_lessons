import random


def fibonacci(n):
    a = 0
    b = 1

    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(6))


### 1. Написать дома функцию, которая вычислит факториал даного числа. Подсказка: рекурсия
### 2. Написать дома функцию, угадывающее число. Подсказка: binary tree or binary search
### 3. Продолжить игру быки коровы


def cow_bull():    
    comp_num = str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
    print(comp_num)
    guess_num = input("Enter your number ")

    if guess_num == comp_num:
        print("You won!")
    
cow_bull()
