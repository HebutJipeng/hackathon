import csv

CITY_LIST = {}
fw = open('./output/city.txt', 'w', encoding='utf-8')

def Main():
    with open('./data.txt', 'r', encoding='utf-8') as ff:
        lines = ff.readlines()
        for item in lines:
            it = item.split(' ')
            CITY_LIST[it[1]] = [it[3], it[5]]
        # print(CITY_LIST)
    with open('./query_result.csv', 'r', encoding='utf-8') as f:
        f_csv = csv.reader(f)
        headers = next(f_csv)
        for row in f_csv:
            str = row[0].replace('市', '')
            print(row[0].replace('市', ''))
            if CITY_LIST.__contains__(row[0].replace('市', '')):
                print(CITY_LIST[row[0].replace('市', '')])
                list = CITY_LIST[row[0].replace('市', '')]
                str = str + ' ' + list[0] + ' ' + list[1]
            else:
                str = str + ' \n'
            fw.write(str)
Main()
