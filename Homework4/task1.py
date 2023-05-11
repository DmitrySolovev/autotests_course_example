# Напишите функцию which_triangle(a, b, c),
# На вход поступают длины трёх сторон треугольника: a, b, c
# Программа выводит какой это треугольник type_triangle: "Равносторонний", "Равнобедренный", "Обычный".
# Либо "Не треугольник", если по переданным параметрам невозможно построить треугольник
# Например 1, 1, 1 --> "Равносторонний"

def which_triangle(a, b, c):
    if (a + b <= c) or (b + c <= a) or (c + a <= b):
        type_triangle = "Не треугольник"
        return type_triangle
    elif a == b and b == c:
        type_triangle = "Равносторонний"
        return type_triangle
    elif (a == b and a != c) or (a == c and a != b) or (b == c and b != a):
        type_triangle = "Равнобедренный"
        return type_triangle
    else:
        type_triangle = "Обычный"
        return type_triangle

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


data = [
    (3, 3, 3),
    (1, 2, 2),
    (3, 4, 5),
    (3, 2, 3),
    (1, 2, 3)
]

test_data = [
    "Равносторонний", "Равнобедренный", "Обычный", "Равнобедренный", "Не треугольник"
]


for i, d in enumerate(data):
    assert which_triangle(*d) == test_data[i], f'С набором {d} есть ошибка, не проходит проверку'
    print(f'Тестовый набор {d} прошёл проверку')
print('Всё ок')
