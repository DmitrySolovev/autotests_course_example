# Дан текстовый файл test_file/task1_data.txt
# Он содержит текст, в словах которого есть цифры.
# Необходимо удалить все цифры и записать получившийся текст в файл test_file/task1_answer.txt

try:
    with open('test_file/task1_data.txt', 'r', encoding='utf-8') as file:
        origin_text = file.read()
finally:
    file.close()

new_text = ''
for char in origin_text:
    if char not in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0'):
        new_text += char

try:
    with open('test_file/task1_answer.txt', 'w', encoding='utf-8') as new_file:
        new_file.write(new_text)
finally:
    new_file.close()


# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


with open("test_file/task1_answer.txt", 'r', encoding='utf-8') as file1:
    with open("test_file/task1_ethalon.txt", 'r', encoding='utf-8') as file2:
        answer = file1.readlines()
        ethalon = file2.readlines()
        assert answer == ethalon, "Файл ответа не совпадает с эталонном"
print('Всё ок')
