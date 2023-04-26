def sum(a,b):
    if b == 0 and a != 0:
        return sum(b, a-1) + 1
    if a == 0 and b != 0:
        return sum(a, b-1) + 1
    if a == 0 and b == 0:
        return 0
    return sum(a-1, b-1) + 1 + 1
    

a = int(input('Введите число a: '))
b = int(input('Введте число b: '))
print(sum(a,b))