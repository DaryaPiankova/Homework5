def my_function(a,b):
    if b == 1:
        return a
    return my_function(a,b-1) * a


a = int(input('Введите число a: '))
b = int(input('Введте число b: '))
print(my_function(a,b))