# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк, количества слов в каждой строке.

with open('my_file.txt','r') as file:
    for i,line in enumerate(file,1):
        print(f'number of line: {i}, number of letters in one line:{len(line)-1}')

