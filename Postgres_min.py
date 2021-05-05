# -*- coding: utf-8 -*-
# неизвестно почему не надо біло добавлять теперь надо
import psycopg2
# import random
# import uuid

connection = psycopg2.connect(
        host="localhost",
        database="vova",
        user="postgres",
        password="VOVABOG1")


def create_table(names):
    try:
        cursor = connection.cursor()

        a = "CREATE TABLE zno("
        b = ""
        for i in names:
                b += i.replace('"', '')
                b += " TEXT, "
        a = a + b
        a += "Year int,"
        a += "PRIMARY KEY (OUTID))"
        cursor.execute(a)
        connection.commit()
        print("Таблица создана")
    except:
        print("Проблема в создании таблицы")
        cursor = connection.cursor()
        cursor.execute("ROLLBACK")
        connection.commit()
        cursor.close()

    return a



# def insert(inserter):
#     cursor = connection.cursor()
#     genius = ""
#     for i in inserter:
#         genius += "INSERT INTO zno VALUES( "
#         i = [str(j) for j in i]
#         genius += i
#         genius += "); \n"
#         print(genius)
#
#     cursor.execute(genius)
#     connection.commit()



# def insert(inserter):
#     cursor = connection.cursor()
#     genius = ''
#     for i in inserter:
#         genius += "INSERT INTO zno VALUES("
#         i[0] = '"' + i[0] + '"'
#         i = (', ').join(i)
#
#         # i = i.replace('"', "'")
#         # genius +=  + i + "'"
#         genius += i
#         genius += ")"
#         print(genius)
#     # cursor.execute(genius)
#     cursor.execute(genius)
#     connection.commit()


def delete_table():
    cursor = connection.cursor()
    try:
        # return a
        cursor.execute("DROP TABLE zno")
        connection.commit()
    except:
        print("Проблема в удалении базы")
        cursor.execute("ROLLBACK")
        connection.commit()
        cursor.close()


# def select_english():
#     cursor = connection.cursor()
#     # return a
#     a = cursor.execute("SELECT ENGBALL100 from zno WHERE ENGTEST = 'Англійська мова'")
#     a = cursor.fetchall()
#     connection.commit()
#     # print(a)
#     return a

def select_all_oblast():
    try:
        cursor = connection.cursor()
        # return a
        a = cursor.execute("SELECT UKRPTREGNAME from zno WHERE ENGTEST = 'Англійська мова'")
        a = cursor.fetchall()
        connection.commit()
    # print(a)
    except:
        cursor = connection.cursor()
        print("Проблема в получении областей")
        cursor.execute("ROLLBACK")
        connection.commit()
        cursor.close()
    return a


# def Select_avg_in_oblast(i):
#     cursor = connection.cursor()
#     # return a
#     print(i)
#     if i == "null":
#         return None
#     a = cursor.execute("SELECT AVG(CAST(ENGBALL100 as float8)) from zno WHERE ENGTEST = 'Англійська мова' and UKRPTREGNAME = %s", (i,))
#     a = cursor.fetchone()
#     connection.commit()
#     # print(a)
#     return a


def Select_min_in_oblast(i):
    try:
        cursor = connection.cursor()
        # return a
        print(i)
        # if i == "null":
        #     return None
        a = cursor.execute("SELECT min(ENGBALL100)  from zno WHERE ENGTEST = 'Англійська мова' and UKRPTREGNAME = %s and ENGBALL100 != 'null' and ENGBALL100 != '0,0'", (i,))
        a = cursor.fetchall()
        connection.commit()
        # print(a)
    except:
        print("Проблема в получении студентов")
        cursor = connection.cursor()
        cursor.execute("ROLLBACK")
        connection.commit()
        cursor.close()
    return a


# def select_english():
#     cursor = connection.cursor()
#     # return a
#     cursor.execute("Select * from zno")
#     a = cursor.fetchone()
#     connection.commit()
#     print(a)
#     return a


def insert_with_place_holder(inserter, year: int):
    try:
        cursor = connection.cursor()
        genius = ""
        list_of_varyables = []
        for i in inserter:
            # print(i)
        # i[0] = '"' + i[0] + '"'
            genius += "INSERT INTO zno VALUES( "
            list_of_varyables += [str(j) for j in i]
            # print(len(i))
            genius += (len(i) - 1) * "%s,"
            genius += "%s,"
            genius += str(year)
            genius += "); \n"
        # print(genius)
        cursor.execute(genius, list_of_varyables)
        # cursor.execute("INSERT INTO zno VALUES('EDDDC0A3-C615-4101-96B3-9F1A4C654A2C', '14809269-9F28-454C-8B3B-01DE067C91F3\', '1999', 'жіноча', 'Житомирська область', 'Новоград-Волинський район', 'смт Городниця', 'Випускник минулих років', 'місто', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, 'Англійська мова', 'Зараховано', 197.0, null, 'Загальноосвітня школа І-ІІІ ступенів №21 м. Житомира', 'Житомирська область', 'м.Житомир. Корольовський район міста', 'Корольовський район міста', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)")
        # cursor.execute("INSERT INTO zno VALUES( 'EDDDC0A3-C615-4101-96B3-9F1A4C654A2C', '14809269-9F28-454C-8B3B-01DE067C91F3', '1999', 'жіноча', 'Житомирська область', 'Новоград-Волинський район', 'смт Городниця', 'Випускник минулих років', 'місто', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'Англійська мова', 'Зараховано', '197.0', 'null', 'Загальноосвітня школа І-ІІІ ступенів №21 м. Житомира', 'Житомирська область', 'м.Житомир. Корольовський район міста', 'Корольовський район міста', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null');")
        connection.commit()
    except:
        print("Проблема в добавлении строчек")
        cursor = connection.cursor()
        cursor.execute("ROLLBACK")
        connection.commit()
        cursor.close()



# try:
delete_table()
# except:
#     print("Толи таблички нету, то ли база недоступна скоро узнаем")