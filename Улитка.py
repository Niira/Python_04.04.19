# Курс основы программирования на Python
# Задание по программированию: Улитка*
# 09.04.2019
#
# Улитка ползет по вертикальному шесту высотой H метров,
# поднимаясь за день на A метров, а за ночь спускаясь на B метров.
# На какой день улитка доползет до вершины шеста?
#
# Формат ввода
#
# Программа получает на вход целые H, A, B. Гарантируется, что A > B ≥ 0.
#
# Формат вывода
#
# Программа должна вывести одно натуральное число.

a = int(input())
b = int(input())
d = int(input())
print(-(-(a - b) // (b - d) - 1))
