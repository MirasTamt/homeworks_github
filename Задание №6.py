# 6. Спортсмен занимается ежедневными пробежками. В первый день его
# результат составил a километров. Каждый день спортсмен увеличивал результат на
# 10 % относительно предыдущего. Требуется определить номер дня, на который общий результат сп
# ортсмена составить не менее b километров. Программа должна принимать значения параметров a и
# b и выводить одно натуральное число — номер дня.

a = int(input("Результат первого дня (км): "))
b = int(input("Желаемый результат x дня (км): "))
x = 1

while a < b:
    a = float(a+(a/10))
    x +=1

print(f"x день состоится на {x} день")