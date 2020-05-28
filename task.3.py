# Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income). \
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).


class Worker:
    def __init__(self, name, surname,position,income):
        self.name =(name)
        self.surname =(surname)
        self.position =(position)
        self._income ={'Wage': income, 'Bonus': income*1.2}

class Position(Worker):
    def get_full_name(self):
        print(f'{str(self.name).title()} {str(self.surname).title()}. Position: {str(self.position).title()}')
    def get_total_income(self):
        print('Monthly salary package is {}RUB, Annual bonus is {}RUB'.format(self._income['Wage'],self._income['Bonus']))


worker_unit = Position('Ilya','Sokolov','Manager',30000)
worker_unit.get_full_name()
worker_unit.get_total_income()