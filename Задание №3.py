user_month = int(input("Введите номер месяца: "))
year = ['Зима',"Весна", "Лето", "Осень"]
year_dict = {'Зима':{1,12,2}, 'Весна': {3,4,5}, 'Лето': {6,8,7},'Осень': {11,9,10}}

if user_month >0 and user_month< 3:
    print(year[0])
elif user_month >= 3 and user_month  <= 5:
    print(year[1])
elif user_month >= 6 and user_month  <= 8:
    print(year[2])
else:
    print(year[3])


def get_key(year_dict, value):
    for k, v in year_dict.items():
        if value in v:
            return k

print(get_key(year_dict, user_month))
