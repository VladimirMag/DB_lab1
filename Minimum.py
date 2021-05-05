# программа получает на вход csv фаил с сепаратором ;. Создает таблицу с названиями из файла.
# Добавляет данные превращая их в тип данных строки.
# Получает из этих данных минимальную по английскому языку сред сдавших ЗНО по каждому отдельной области
# измерянная скорость скрипта 1000 строчек в секунду
# Средняя скорость 1 транзакции 0.048 секунды ( 50 строчек)
import csv
import Postgres_min as Con
import time
from pprint import pprint
import pandas


start_time = time.monotonic()
table_names = []
slovar_hranenie = dict()

def creating_table_from_file(file_name, zapysk, table_names, year):
    print("Начинаем добавление")
    zapysk += 1
    with open(file_name, encoding="utf-8") as csv_file:
        a = []
        csv_reader = csv.reader(csv_file, delimiter=';')
        counter = 0
        progresbar = 0
        for indexing, row in enumerate(csv_reader):
            if counter == 50:
                progresbar += 1
                start2_time = time.monotonic()
                Con.insert_with_place_holder(a, year=year)
                print(time.monotonic() - start2_time)
                a = []
                bar = ((progresbar * counter)/1000) * 100  # len(csv_reader)
                if bar >= 100.0:
                    # return table_names
                    break
                print(f"Добавлено {bar:.2f}%")
                counter = 1
            if counter == 0:
                names = row
                table_names += names
                if zapysk == 1:
                    b = Con.create_table(names)
                counter = 1
            else:

                a += [row]
                counter += 1
        else:
            Con.insert_with_place_holder(a, year=year)  #  если выход не по брейку (дошли до конца) добавить оставшееся количество данных в a

    a = Con.select_all_oblast()
    a = set(a)
    # оказывается в сете тоже можно удалять первый найденный елемент
    a.remove(('null',)) if ("null",) in a else print("Нет нала")
    print(a)
    for i in a:
        min_bal = Con.Select_min_in_oblast(*i)
        # for j in min_bal:
        #
        #     try: # пропуск вариантов null
        #         summa_po_oblasti += float(j[0])
        #         counter_po_oblasti += 1
        #     except:
        #         pass
        # slovar_hranenie.update({str(i[0]) + str(year):min_bal})
        slovar_hranenie[str(i[0]) + str(year)] = float(min_bal[0][0].replace(",", "."))
        # sredniy_bal = summa_po_oblasti/counter_po_oblasti
        print(*i, min_bal[0])



    # print(a)
    # median = Con.select_english()
    # print(median)
    # counter = 0
    # a = []
    # for i in median:
    #     for j in i:
    #         if "," in j:
    #             j = j.replace(",", ".")
    #         if j == "null":
    #             counter += 1
    #             continue
    #         elif float(j) <= 100:
    #             counter += 1
    #         else:
    #             a += [float(j)]

    # counter = len(median) - counter
    # print(sum(a)/counter)

    return zapysk, table_names

zapysk = 0

while True:
    filename = input("Введите год для скачки")
    if filename == "1":
        x = sorted(slovar_hranenie)
        for i, el in enumerate(x[::2]):
            z = x[i * 2 + 1] if slovar_hranenie[el] > slovar_hranenie[x[i * 2 + 1]] else el
            del slovar_hranenie[z]
        pprint(slovar_hranenie)
        # df = pandas.Series(slovar_hranenie)
        # df.iloc[0] = "Age,name"
        # df.to_csv("Answer2.csv", header=["20"])
        with open("Answer.csv", 'w', newline='', encoding="UTF-8") as f:
            my_writer = csv.DictWriter(f, fieldnames=slovar_hranenie.keys())
            my_writer.writeheader()
            # for i in slovar_hranenie:
            my_writer.writerow(slovar_hranenie)
        break

        # it_dict = iter(sorted(slovar_hranenie))
        # new_dict = dict()
        # for _ in range(len(slovar_hranenie) // 2):
        #     x1, x2 = next(it_dict), next(it_dict)
        #     y = x1 if slovar_hranenie[x1] > slovar_hranenie[x2] else x2
        #     new_dict[y] = slovar_hranenie[y]
        # pprint(new_dict)


        # print('*1*')
        # x = sorted(slovar_hranenie)
        # pprint(slovar_hranenie)
        # print('*2*')
        # y = map(lambda x1, x2: slovar_hranenie[x1] if slovar_hranenie[x1] > slovar_hranenie[x2] else slovar_hranenie[x2], x[::2], x[1::2])
        # new_dict = {i: slovar_hranenie[i] for i in y}
        # pprint(new_dict)


        # sorted_dict = {}
        #
        # for i in sorted_values:
        #     for k in slovar_hranenie.keys():
        #         if slovar_hranenie[k] == i:
        #             sorted_dict[k] = slovar_hranenie[k]
        #             break


    try:
        zapysk, table_names = creating_table_from_file(filename + ".csv", zapysk, table_names, int(filename))
    except:
        print("База недоступна. Попробуйте позже.")
    # print(zapysk, table_names)
    print("Время работы скрипта", time.monotonic()-start_time)


