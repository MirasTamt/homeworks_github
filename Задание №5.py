# 5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки
# (соотношение прибыли к выручке). Далее запросите численность сотрудников фирмы и
# определите прибыль фирмы в расчете на одного сотрудника.


revenue = int(input("Введите выручку фирмы: "))
expences = int(input("Введите расход фирмы: "))

if revenue > expences:
    income = revenue - expences
    print(f"Фирма работает с прибылью: {income}")
    print(f"Фирма работает с рентабельностью: {income/revenue}%")
    employees = int(input("Введите количество сотрудников: "))
    income_on_employee = income/employees
    print(f"Прибыль фирмы в расчете на одного сотрудника составляет: {income_on_employee}")
else: print("Фирма не прибыльна")