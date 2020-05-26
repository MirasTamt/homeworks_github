import json
my_list =[]
with open('firms.txt','r+') as file:
    content = file.readlines()
    # print(content)
    for firm in content:
        my_list.append(firm.split(' '))
        # print(my_list)
    firm1_result = int(my_list[0][2])-int(my_list[0][3])
    firm2_result =int(my_list[1][2])-int(my_list[1][3])
    firm3_result =int(my_list[2][2])-int(my_list[2][3])
    firm4_result = int(my_list[3][2])-int(my_list[3][3])
    print(f'Profit of firm_1 is: {firm1_result}\nProfit of firm_2 is: {firm2_result}\nProfit of firm_3 is: {firm3_result}\nProfit of firm_4 is: {firm4_result}\n')
    average_profit =(firm1_result+firm2_result+firm3_result+firm4_result)/4
    print(f'Average profit among firms is: {average_profit}')
    my_firms =[{my_list[0][0] : firm1_result, my_list[1][0]:firm2_result,my_list[2][0]:firm3_result,my_list[3][0]:firm4_result},{'Average profit':average_profit}]
    print(my_firms)

with open('json_firms.txt','w') as file_json:
    json.dump(my_firms,file_json)