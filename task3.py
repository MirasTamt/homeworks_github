# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.

salar =[]
salary_list =[]
with open('salaries.txt', 'r+', encoding='utf-8') as salaries:
    for line in salaries:
        salary_list.append(line.split(' = '))
    for salary in salary_list:
        salar.append(int(salary[1]))
        if int(salary[1])<20000:
            print(f'Less than 20kRUB earns: {salary[0]}')
    print(f'Average salary is: {sum(salar)/len(salar)}RUB')
