def my_func_01(x, y):
    x = x ** y
    return x


def my_func_02(x, y):
    z = 1
    for y in range(0, y, -1):
        z = z * x
    x = 1 / z
    return x


print(round(my_func_01(36, -2), 10))
print(round(my_func_02(36, -2), 10))
