import csv
import yaml

def create():
    flag = 0
    user_list = []
    infra_list = []
    tech_list = []

    with open("C:/Users/aleks/Desktop/dip/input/Properities.csv", encoding='utf-8') as r_file:

        file_reader = csv.reader(r_file, delimiter=';')

        for row in file_reader:
            for i in range(len(row)):
                row[i] = row[i].replace('\ufeff', '')

            if row[0] == "Пользователи":
                flag = 1
            elif row[0] == "Инфраструктура":
                flag = 2
            elif row[0] == "Технические требования":
                flag = 3
            elif row[0] == 'ФИО' or row[0] == 'ID':
                continue
            elif flag == 1:
                user_list.append(row)
            elif flag == 2:
                infra_list.append(row)
            elif flag == 3:
                tech_list.append(row)

    with open('C:/Users/aleks/Desktop/dip/result/Users.csv', 'w', newline='') as csvfile:
        file_writer = csv.writer(csvfile, delimiter=';',
                                 quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for elem in user_list:
            file_writer.writerow(elem)

    with open('C:/Users/aleks/Desktop/dip/result/Infr.csv', 'w', newline='') as csvfile:
        file_writer = csv.writer(csvfile, delimiter=';',
                                 quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for elem in infra_list:
            file_writer.writerow(elem)

    with open('C:/Users/aleks/Desktop/dip/result/Tech.yml', 'w', newline='') as yamlfile:
        to_yaml = {'any_name': tech_list}
        yaml.dump(to_yaml, yamlfile)

    print("Файлы успешно созданы.\n")