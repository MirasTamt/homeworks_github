# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

with open('file.txt','w') as file:
    user_input ='\n'.join(input('Prompt into file: ').split(' '))
    file.write(user_input)


with open('file.txt') as file:
    for line in file:
        print(line.strip())