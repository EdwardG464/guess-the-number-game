import random
num = random.randint(0, 100)
print('Добро пожаловать в числовую угадайку')

def is_valid(s):
    return s.isdigit() and 1 <= int(s) <= 100

def check_number():
    while True:
        you_number = input('Введите число от 1 до 100: ')
        if is_valid(you_number):
            return int(you_number)
        else:
            print('А может быть все-таки введем целое число от 1 до 100?')

def sravnenie():
    while True:
        n = check_number()
        if n < num:
            print('Ваше число меньше загаданного, попробуйте еще разок')
        elif n > num:
            print('Ваше число больше загаданного, попробуйте еще разок')
        else:
            print('Вы угадали, поздравляем!')
            print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
            break

sravnenie()