import csv

fw = open('./output/city2.txt', 'w', encoding='utf-8')
def main():
    with open('./query_result.csv', 'r', encoding='utf-8') as f:
        f_csv = csv.reader(f)
        headers = next(f_csv)
        with open('./city.txt', 'r', encoding='utf-8') as ff:
            fi = ff.readlines()
            for index, row in enumerate(f_csv, start=1):
                print(row[0], index)
                print(fi[index])
                list = fi[index].split(',')
                fw.write(row[0] + ' ' + list[0] + ' ' + list[1] + '\n')
main()
