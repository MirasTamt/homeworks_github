import sys
def salary(hours,fee_hour,remuneration):
    salary_calc =(int(hours)*int(fee_hour))+int(remuneration)
    return salary_calc
hours = sys.argv[1]
fee_hour = sys.argv[2]
remuneration = sys.argv[3]
print('Qty of hours', hours)
print('Fee per hour', fee_hour)
print('Remuneration package',remuneration)
print('Total Salary:', salary(hours,fee_hour,remuneration))