import socket
from connection import *

ip = "169.254.0.10"
port = 9876

# создаём сокет для подключения
sock = socket.socket()
connection1 = sock.connect((ip,port))
def get_jugement():
    tmp = f'SELECT * FROM Jugement WHERE ID_jugement=1;'
    tmp = execute_read_query(connection, tmp)
    areamin = tmp[0][1]
    areamax = tmp[0][2]
    totalareamin = tmp[0][3]
    totalareamax = tmp[0][4]
    numbersmin = tmp[0][5]
    numbersmax = tmp[0][6]
    blistermin = tmp[0][7]
    blistermax = tmp[0][8]
    id_jugement = tmp[0][0]
    return totalareamin, totalareamax, areamin, areamax, numbersmin, numbersmax, blistermin, blistermax, id_jugement

# получение данных с сервера
while True:
    type_of_pills = 1 # потом меняем
    data = sock.recv(1024).decode('UTF-8')
    msg = data.split(' ')
    k = 0
    while k < len(msg) - 1:
        if msg[k] == '':
            msg.pop(k)
        else:
            k+=1
    random_area = int(msg[1])
    random_total_area = int(msg[2])
    random_area_blister = int(msg[4])
    test = int(msg[0])
    numbers = int(msg[3])
    jug_color = int(msg[5])
    jug_pills = [int(msg[6]), int(msg[7]), int(msg[8]), int(msg[9]), int(msg[10]), int(msg[11]), int(msg[12]), int(msg[13]), int(msg[14]), int(msg[15])]
    area_pills = [int(msg[16]), int(msg[17]), int(msg[18]), int(msg[19]), int(msg[20]), int(msg[21]), int(msg[22]), int(msg[23]), int(msg[24]), int(msg[25])]
    tmp_mas = []
    for i in range(0, len(jug_pills)):
        if jug_pills[i] == -1:
            tmp_mas.append(i)
    print(random_area, random_total_area, random_area_blister, test, numbers, jug_color, jug_pills, area_pills)
    tmp = f'INSERT INTO Object (area, total_area, number_of_labels, area_blister, jugement, ID_jugement, time) VALUES ({random_area}, {random_total_area}, {numbers}, {random_area_blister}, {test}, {id_jugement}, NOW());'
    execute_query(connection, tmp)
    if test == -1:
        id_error = 0
        totalareamin, totalareamax, areamin, areamax, numbersmin, numbersmax, blistermin, blistermax, id_jugement = get_jugement()
        if random_area_blister > blistermax or random_area_blister < blistermin:
            id_error = 1
        elif jug_color == -1:
            id_error = 3
            for p in range(0, len(tmp_mas)):
                tmp = f'INSERT INTO Error_pill (number_of_pill, area_pill, ID_error, ID_jugement) VALUES ({tmp_mas[p]}, {area_pills[tmp_mas[p]]}, {id_error}, {type_of_pills});'
                execute_query(connection, tmp)
        elif (random_total_area > totalareamax or random_total_area < totalareamin):
            if (random_area > areamax or random_area < areamin):
                id_error = 4
                for p in range(0, len(tmp_mas)):
                    tmp = f'INSERT INTO Error_pill (number_of_pill, area_pill, ID_error, ID_jugement) VALUES ({tmp_mas[p]}, {area_pills[tmp_mas[p]]}, {id_error}, {type_of_pills});'
                    execute_query(connection, tmp)
            else:
                id_error = 5
                for p in range(0, len(tmp_mas)):
                    tmp = f'INSERT INTO Error_pill (number_of_pill, area_pill, ID_error, ID_jugement) VALUES ({tmp_mas[p]}, {area_pills[tmp_mas[p]]}, {id_error}, {type_of_pills});'
                    execute_query(connection, tmp)
        else:
            id_error = 2
            for p in range(0, len(tmp_mas)):
                    tmp = f'INSERT INTO Error_pill (number_of_pill, area_pill, ID_error, ID_jugement) VALUES ({tmp_mas[p]}, {area_pills[tmp_mas[p]]}, {id_error}, {type_of_pills});'
                    execute_query(connection, tmp)
