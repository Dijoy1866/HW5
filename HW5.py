
# Задание 1
a = int(input('Введите число A: '))
b = int(input('Введите число B: '))
c = int(input('Введите число C: '))

if min(a, b, c) > 10 and a%3 == 0 and b%3 == 0:
    print('Yes')
else:
    print('No')


# Задание 2

a = int(input('Введите число a: '))
b = int(input('Введите число b: '))
c = int(input('Введите число c: '))

max = a
if b > max:
    max = b
if c > max:
    max = c

print(f'max: ', max)


# Задания со звездочкой:

number = int(input('Введите 3х значное число:'))
if not 100<= number<=999:
    print('Ошибка, число не входит в диапазон')
    exit()

first_num = number % 10
second_num = number % 100 // 10
third_num = number % 1000 // 100
final_num = first_num * 100 + second_num * 10 + third_num
print(final_num)

