import random
from connection import *
import time

# функция для генерации значений и записи в бд
def pills(totalareamin, totalareamax, areamin, areamax, numbersmin, numbersmax, blistermin, blistermax, id_jugement):
    a=[]
    tmp = f'SELECT COUNT(ID_object) FROM Object WHERE ID_jugement={id_jugement};'
    tmp = execute_read_query(connection, tmp)[0][0]
    if (tmp % 30) != 0 or (tmp < 50):
        random_area = random.uniform(areamin, areamax)
        random_total_area = random.uniform(totalareamin, totalareamax)
        random_area_blister = random.uniform(blistermin, blistermax)
        test = 0
        numbers = numbersmin
    else:
        random_type_error = random.randint(1, 5)
        random_pill = random.randint(1, 10)
        test= -1
        random_area_pill = random.uniform(areamin, areamax)
        match random_type_error:
            case 1:
                random_area_blister = random.uniform(blistermax, blistermax + 10000)
                random_area = random.uniform(areamin, areamax)
                random_total_area = random.uniform(totalareamin, totalareamax)
                numbers = numbersmin
            case 2:
                random_area = random.uniform(0, areamin)
                random_total_area = random.uniform(0, totalareamin)
                random_area_blister = random.uniform(blistermin, blistermax)
                numbers = random.randint(1, numbersmin - 1)
                random_area_pill = random.uniform(0, areamin)
            case 3:
                random_area = random.uniform(areamin, areamax)
                random_total_area = random.uniform(totalareamin, totalareamax)
                random_area_blister = random.uniform(blistermin, blistermax)
                numbers = numbersmin
                random_area_pill = random.uniform(0, areamin)
            case 4:
                random_total_area = random.uniform(0, totalareamin)
                random_area = random.uniform(areamin, areamax)
                random_area_blister = random.uniform(blistermin, blistermax)
                numbers = random.randint(1, numbersmin - 1)
                random_area_pill = random.uniform(0, areamin)
            case 5:
                random_total_area = random.uniform(0, totalareamin)
                random_area = random.uniform(areamin, areamax - 100)
                random_area_blister = random.uniform(blistermin, blistermax)
                numbers = random.randint(1, numbersmin - 1)
                random_area_pill = random.uniform(0, areamin)
        tmp = f'INSERT INTO Error_pill (number_of_pill, area_pill, ID_error, ID_jugement) VALUES ({random_pill}, {random_area_pill}, {random_type_error}, {id_jugement});'
        execute_query(connection, tmp)
    a.append([random_area, random_total_area, test, random_area_blister])
    tmp = f'INSERT INTO Object (area, total_area, number_of_labels, area_blister, jugement, ID_jugement, time) VALUES ({random_area}, {random_total_area}, {numbers}, {random_area_blister}, {test}, {id_jugement}, NOW());'
    execute_query(connection, tmp)
    a=[]
    #time.sleep(1)

# функция для генерации значений 51 раз (если таблица пустая)
def gnrt(totalareamin, totalareamax, areamin, areamax, numbersmin, numbersmax, blistermin, blistermax, id_jugement):
    for i in range(51):
        pills(totalareamin, totalareamax, areamin, areamax, numbersmin, numbersmax, blistermin, blistermax, id_jugement)

#gnrt(2200, 2400, 22000, 24000, 10, 10, 35000, 36000, 1)