a = int(input())
b = int(input())
c = -(-a // b) % 2

print(c)

print('YES' * 0**c, 'NO' * 0**(1 - c), sep='')
