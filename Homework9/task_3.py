# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases

try:
    with open("test_file/task_3.txt", 'r') as file:
        lst = [line.rstrip() for line in file]
finally:
    file.close()

lst.append('')
sub_lst = []
new_lst = []
for el in lst:
    if el != '':
        sub_lst.append(int(el))
    else:
        new_lst.append(sub_lst)
        sub_lst = []

three_most_expensive_purchases = sum(sorted([sum(i) for i in new_lst], reverse=True)[:3])

assert three_most_expensive_purchases == 202346
